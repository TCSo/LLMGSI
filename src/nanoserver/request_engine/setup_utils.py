import os
import logging
import sys

# Setup openAI config for llamaindex to use
def setup_openAI():
    os.environ["OPENAI_API_KEY"] = "sk-"

# Setup basic logging 
def setup_logging():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))