# SimpleAstraReader Documentation

The `SimpleAstraReader` class is a reader for Apache Cassandra. It's designed to execute CQL queries, manage data insertions, and perform vector searches in a given keyspace and table.

## Class Initialization

The class is initialized with several parameters:

- `bundle_path`: A string that represents the path to the secure bundle zip file.
- `client_id`: A string that represents the Client ID for DataStax Astra.
- `client_secret`: A string that represents the Client secret for DataStax Astra.
- `keyspace`: A string that specifies the keyspace name to use.
- `table`: An optional string that specifies the table name to read documents from.
- `vector_column`: An optional string that represents the column name for the vector search.
- `vector_value`: An optional string that represents the vector to search.
- `vector_count`: An optional integer that defines the number of vectors to return.
- `user_input`: An optional string that can be used to generate a query.
- `custom_query`: An optional string to define a custom query.

These parameters are used to establish a connection with the Cassandra cluster and set up the details for data operations.

## Methods

The class contains several methods:

### `load_data()`

This method, which accepts an optional query string as an argument, is used to execute the query and load data. It does this by calling the `execute_query()` method.

### `execute_query()`

This method, which also accepts an optional query string as an argument, is responsible for executing a provided CQL query. It returns a list of documents, where each document corresponds to a row in the table. If no query is provided, it executes a default "SELECT ALL" query on the specified keyspace and table.

### `vector_search()`

The `vector_search()` method performs a vector search on the specified keyspace and table. It generates a CQL query that orders by the provided vector column and limits the result set to the provided vector count.

### `insert_vectors()`

This method takes a dictionary of vectors and inserts them into the specified keyspace and table. The dictionary keys are considered as row IDs, and the values are considered as the corresponding vectors.

### `query_generator()`

This method generates CQL queries based on user instructions and table definitions. It also executes the generated query and returns the result.
