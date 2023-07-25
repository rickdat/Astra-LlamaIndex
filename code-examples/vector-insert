# Demonstrate Vector data insert

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
table = "products"
vector_column = "item_vector"

# Initialize a reader
data_insert = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace, table, vector_column)

# Define some test vectors. The dictionary keys should be your row IDs and the dictionary values should be another
# dictionary containing column names as keys and the corresponding values to be inserted.

vectors = {
    "8": {"name": "SourceTable application", "description": "Sourcetable new platform was created with Astra and LlamaIndex","item_vector": [0.1, 0.15, 0.3, 0.12, 0.05]},
    "9": {"name": "SourceTable teams", "description": "John and Andrew created the new Sourcetable platform","item_vector": [0.1, 0.15, 0.3, 0.12, 0.05]},
}

# Insert the vectors
data_insert.insert_vectors(vectors)
