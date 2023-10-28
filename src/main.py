import json
import re
import time
# import requests
import os
import logging
import sys

# import numpy as np
# import openai
# import pandas as pd

# from PyPDF2 import PdfReader
from query_engines import simple_query_engine
from setup_utils import setup_openAI, setup_logging


if __name__ == '__main__':
    setup_openAI()
    setup_logging()

    query_engine = simple_query_engine()

    # Q&A Iteration loop
    question = input("Please enter your question or enter q to quit:\n") 
    while question != 'q':
        response = query_engine.query(question)
        print(response)
        question = input("Please enter your question or enter q to quit:\n") 