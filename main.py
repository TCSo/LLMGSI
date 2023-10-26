import json
import re
import time
import requests
import os
import logging
import sys

import numpy as np
import openai
import pandas as pd

from PyPDF2 import PdfReader
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from setup import setup_openAI, setup_logging

setup_openAI()
setup_logging()


# check if storage already exists
if (not os.path.exists('./storage')):
    print("Creating index")
    # load the documents and create the index
    documents = SimpleDirectoryReader('./data').load_data()
    index = VectorStoreIndex.from_documents(documents)
    # store it for later
    index.storage_context.persist()
else:
    print("Loading index")
    # load the existing index
    storage_context = StorageContext.from_defaults(persist_dir='./storage')
    index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
response = query_engine.query("Can I use lists for HW1?")
print(response)
