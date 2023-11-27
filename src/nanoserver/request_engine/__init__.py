from .query_engines import GSIQueryEngineInitializer
from .setup_utils import setup_openAI, setup_logging
setup_openAI()
setup_logging()

query_engine = GSIQueryEngineInitializer().get_query_engine()

def query_response(question):
    return query_engine.query(question)