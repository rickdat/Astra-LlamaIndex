# Demonstrate Vector Search using Astra and OpenAI

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
keyspace = ""
table = ""
query = ""  # If no custom query, leave it as empty string

reader = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace, table, vector_column="item_vector", vector_value='0.15, 0.1, 0.1, 0.35, 0.55', vector_count=1)
documents = reader.vector_search()

index = ListIndex.from_documents(documents)

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("what does the deep learning display do?")

# visualize in console or web
print(response)
display(Markdown(f"<b>{response}</b>"))
