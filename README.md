# New Python Library: LlamaAstra API 

## Overview
This Python library called **LlamaAstra**, an extension to LlamaIndex, allows you to seamlessly connect to [DataStax's Astra](https://www.datastax.com/products/datastax-astra) Databases. It empowers your applications with the capabilities to perform vector search, generate and execute custom queries. 

The library also provides tools to auto-generate CQL queries from natural language and ingest data into your Astra Database.

### Key functionalities and features

* Connect to Astra Databases: Simply provide your client and connection details and establish a seamless connection to your Astra Database.
* Vector Search: Directly perform vector search on your Astra Database.
* Custom Query Search: Execute any CQL queries on your Astra Database.
* Automatically Generate Queries from Natural Language: The library can auto-generate CQL queries based on user's natural language input.
* Ingest Data: Easily ingest data into your Astra Database.

Check the [source code of the library here](https://github.com/username/projectname).

## Getting Started

### Prerequisites

You need to have Python installed (preferably Python 3.6 or higher). Libraries like openAI, llama_index, IPython and the cassandra-driver also need to be installed. 

### Installation

```bash
Clone the repo
```

```bash
pip install llama_astra
```

## Usage
First, import the library as shown below:
```python
from NewLlamaIndexAstraIntegration import SimpleAstraReader
```

### Establish Connection
To establish a connection to your Astra Database, use the `SimpleAstraReader` class.

```python
reader = SimpleAstraReader(your_bundle_path, your_client_id, your_client_secret, your_keyspace, your_table)
```

### Execute a Query
To execute a query and load the result into a LlamaIndex Index object, use the `load_data()` method.

```python
documents = reader.load_data(your_query)
```

### Generating CQL Query from Natural Language
To generate a CQL query from the user's natural language input, call the `query_generator()` methods. 

```python
generate= SimpleAstraReader(bundle_path, client_id, client_secret, keyspace, table, vector_column,user_input="your query in natural language")
print(generate.query_generator())
```
### Insert Vectors into Database
To insert vector data, you can use the `insert_vectors(vectors)` method.

```python
data_insert.insert_vectors(your_vectors_dictionary)
```

For more detailed examples, please visit [here](https://github.com/username/projectname/examples).

## Example Files
The [examples](https://github.com/username/projectname/examples) directory includes several examples that demonstrate the usage of LlamaAstra.

## Documentation
For more detailed documentation, refer to the [official documentation here](https://github.com/username/projectname/docs).

## Contributing
We welcome all contributors! Please read our [contributing guide](https://github.com/username/projectname/CONTRIBUTING.md) for more details on how to get started.

## Issues
If you encounter any issues, please report them at our [issue tracker](https://github.com/username/projectname/issues).

## License
LlamaAstra is available under the [MIT License](https://github.com/username/projectname/LICENSE.md).
