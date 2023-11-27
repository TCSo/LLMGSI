import os
import json
import logging
from llama_index import SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index import (
    VectorStoreIndex,
    get_response_synthesizer,
)
from llama_index.retrievers import VectorIndexRetriever, BM25Retriever, QueryFusionRetriever
from llama_index.query_engine import RetrieverQueryEngine
from llama_index.indices.postprocessor import SimilarityPostprocessor

from .setup_utils import *
from llama_index.prompts import PromptTemplate
from llama_index import GPTVectorStoreIndex, download_loader

class GSIQueryEngineInitializer:
    
    def __init__(self):
        if (not os.path.exists('./storage')):
            documents = SimpleDirectoryReader('./data').load_data()
            index = VectorStoreIndex.from_documents(documents)
            index.storage_context.persist()
        else:
            storage_context = StorageContext.from_defaults(persist_dir='./storage')
            index = load_index_from_storage(storage_context)
        
        refine_tmpl = PromptTemplate(
            refine_tmpl_str,
            # function_mappings={"few_shot_examples": few_shot_examples_fn},
        )

        qa_prompt_tmpl = PromptTemplate(
            qa_prompt_tmpl_str,
            # function_mappings={"few_shot_examples": few_shot_examples_fn},
        )
        
        retriever = self.init_retriever(index)
        
        # configure response synthesizer
        response_synthesizer = get_response_synthesizer()

        # assemble query engine
        query_engine = RetrieverQueryEngine(
            retriever=retriever,
            response_synthesizer=response_synthesizer,
            node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)],
        )

        query_engine.update_prompts(
            {"response_synthesizer:text_qa_template": qa_prompt_tmpl, "response_synthesizer:refine_template": refine_tmpl}
        )
        
        self.query_engine = query_engine
    
    def init_retriever(self, index):
        # configure retriever
        vector_retriever = VectorIndexRetriever(
            index=index,
            similarity_top_k=2,
        )

        bm25_retriever = BM25Retriever.from_defaults(
            docstore=index.docstore, similarity_top_k=2
        )

        self.retriever = QueryFusionRetriever(
            [vector_retriever, bm25_retriever],
            similarity_top_k=2,
            num_queries=2,
            use_async=False,
            verbose=True,
        )
        
        # change this to self.retriever
        return vector_retriever
    
    def get_query_engine(self):
        return self.query_engine

qa_prompt_tmpl_str = """\
    Context information is below.
    ---------------------
    You serve as a Graduate Student Instructor at UC Berkeley with extensive \
    experience teaching CS 61A: Structure and Interpretation of Computer Programs. 
    Your role involves responding to students' inquires and providing as many \
    helpful tips as possible.

    Here are some contents that may help you answer the student's question:
    {context_str}
    ---------------------
    Given the context information and not prior knowledge, \
    Please answer the query asking about class content, homework assignments, \
    projects and other logistics related questions.

    Question: {query_str}
    Answer: \
"""

refine_tmpl_str = """\
    The original query is as follows: {query_str}
    We have provided an existing answer: {existing_answer}
    We have the opportunity to refine the existing answer (only if needed) with some more context below.
    ------------
    {context_msg}
    ------------
    Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer.
    Refined Answer: 
"""