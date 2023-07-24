# Execute a custom query and load the result into an LlamaIndex Index object.

import openai
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
from AstraLlamaIndex import SimpleAstraReader


openai.api_key = ""
bundle_path = ""
client_id = ""
client_secret = ""
keyspace = ""

# Create your table
cql_command = "CREATE TABLE IF NOT EXISTS vsearch.products (id int PRIMARY KEY,name TEXT, description TEXT, item_vector VECTOR<FLOAT, 5>);"  # If no custom query, leave it as empty string
customquery = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace,custom_query=cql_command)
documents = customquery.execute_query()

#Create indexes
cql_command = """CREATE CUSTOM INDEX IF NOT EXISTS ann_index   ON vsearch.products(item_vector) USING 'StorageAttachedIndex'WITH OPTIONS = { 'similarity_function': 'DOT_PRODUCT' };"""
customquery = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace,custom_query=cql_command)
documents = customquery.execute_query()

#Insert Data
cql_command = """
INSERT INTO vsearch.products (id, name, description, item_vector) VALUES ( 1, 'Coded Cleats','ChatGPT integrated sneakers that talk to you', [0.1, 0.15, 0.3, 0.12, 0.05] );"""
customquery = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace,custom_query=cql_command)
documents = customquery.execute_query()

#Insert Data
cql_command = """
INSERT INTO vsearch.products (id, name, description, item_vector) VALUES (2, 'Logic Layers', 'An AI quilt to help you sleep forever', [0.45, 0.09, 0.01, 0.2, 0.11]);
"""
customquery = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace,custom_query=cql_command)
documents = customquery.execute_query()

#Insert Data
cql_command = """
INSERT INTO vsearch.products (id, name, description, item_vector) VALUES (5, 'Vision Vector Frame', 'A deep learning display that controls your mood', 
      [0.1, 0.05, 0.08, 0.3, 0.6]);
"""
customquery = SimpleAstraReader(bundle_path, client_id, client_secret, keyspace,custom_query=cql_command)
documents = customquery.execute_query()
