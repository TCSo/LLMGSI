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
from setup import setup_openAI

setup_openAI()

# documents = SimpleDirectoryReader("YOUR_DATA_DIRECTORY").load_data()
# index = VectorStoreIndex.from_documents(documents)