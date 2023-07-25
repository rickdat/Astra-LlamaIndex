# Execute a custom query and load the result into a LlamaIndex Index object. 
# Create the database objects before executing the query.

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
query = "SELECT * FROM vsearch.products ORDER BY item_vector ANN OF [0.15, 0.1, 0.1, 0.35, 0.55] LIMIT 1;"  # If no custom query, leave it as empty string

reader = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace)
documents = reader.load_data(query)

index = ListIndex.from_documents(documents)

# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("what does the deep learning display?")

# visualize in console or web
print(response)
display(Markdown(f"<b>{response}</b>"))
