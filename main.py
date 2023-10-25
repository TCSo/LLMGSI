import json
import re
import time
import requests
import os

import numpy as np
import openai
import pandas as pd

from PyPDF2 import PdfReader
from llama_index import VectorStoreIndex, SimpleDirectoryReader

os.environ["OPENAI_API_KEY"] = "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"

# documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
# index = VectorStoreIndex.from_documents(documents)