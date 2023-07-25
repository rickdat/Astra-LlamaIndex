# LlamaAstra Library 

## Overview
This Python library called **LlamaAstra**, an extension to LlamaIndex, allows you to seamlessly connect to [DataStax's Astra](https://www.datastax.com/products/datastax-astra) Databases. It empowers your applications with the capabilities to perform vector search, generate and execute custom queries. 

The library also provides tools to auto-generate CQL queries from natural language and ingest data into your Astra Database.

### Key functionalities and features

* Connect to Astra Databases: Simply provide your client and connection details and establish a seamless connection to your Astra Database.
* Vector Search: Directly perform vector search on your Astra Database.
* Custom Query Search: Execute any CQL queries on your Astra Database.
* Automatically Generate Queries from Natural Language: The library can auto-generate CQL queries based on user's natural language input.
* Ingest Data: Easily ingest data into your Astra Database.

Check the [source code of the library here](https://github.com/rickdat/Astra-LlamaIndex/blob/main/astra-llamaindex-library.py).

## Getting Started

### Prerequisites

You need to have Python installed (preferably Python 3.6 or higher). Libraries like openAI, llama_index, IPython and the cassandra-driver also need to be installed. 

### Get Started

```bash
git clone https://github.com/rickdat/Astra-LlamaIndex
```

```bash
pip install cassandra-driver, openai, llama-index
```

## Usage
Import the library as shown below:
```python
from astra-llamaindex-library import SimpleAstraReader
```

##
Code explanation can be found [here](https://github.com/rickdat/Astra-LlamaIndex/blob/main/docs/usage.md)

## Code Examples

To get started, please visit our code examples [here](https://github.com/rickdat/Astra-LlamaIndex/tree/main/code-examples).


## Issues
If you encounter any issues, please report them at our [issue tracker](https://github.com/rickdat/Astra-LlamaIndex/issues).
