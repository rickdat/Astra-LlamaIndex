import openai
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from llama_index import ListIndex
from IPython.display import Markdown, display
from AstraLlamaIndex import SimpleAstraReader
import os

openai.api_key = ""
bundle_path = ""
client_id = ""
client_secret = ""
keyspace = "vsearch"

# Initialize a reader
generate= SimpleAstraReader(bundle_path, client_id, client_secret, keyspace, user_input="count the number of rows in the products table")
print(generate.query_generator())
