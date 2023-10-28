import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

# Creates a basic llamaindex query engine
def simple_query_engine():
    if (not os.path.exists('./storage')):
        documents = SimpleDirectoryReader('./data').load_data()
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist()
    else:
        storage_context = StorageContext.from_defaults(persist_dir='./storage')
        index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    return query_engine