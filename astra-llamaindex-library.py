# Importing required modules and libraries
import logging
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.cluster import NoHostAvailable
from typing import Dict, List, Optional
from llama_index.readers.base import BaseReader
from llama_index.readers.schema.base import Document
from cassandra.metadata import KeyspaceMetadata
from llama_index.llms import ChatMessage, OpenAI
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel

# Configuring logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimpleAstraReader(BaseReader):
    """
    The Simple Astra Reader class, which is responsible for reading from Apache Cassandra.
    Inherits from the BaseReader class.
    """
    def __init__(
        self,
        bundle_path: str,
        client_id: str,
        client_secret: str,
        keyspace: str,
        table: Optional[str] = None,
        vector_column: Optional[str] = None,    # Column name to search
        vector_value: Optional[str] = None,     # Vector to search
        vector_count: Optional[int] = None,     # Number of vectors to return
        user_input: Optional[str] = None,       # User input to generate query
        custom_query: Optional[str] = None,     # Custom query
    ) -> None:
        """
        The constructor for the SimpleAstraReader class.
        Initializes with necessary parameters and tries to establish a connection with the cluster.
        """
        self.cloud_config = {
            'secure_connect_bundle': bundle_path
        }
        self.auth_provider = PlainTextAuthProvider(client_id, client_secret)

        try:
            self.cluster = Cluster(cloud=self.cloud_config, auth_provider=self.auth_provider)
            self.session = self.cluster.connect()
            logger.info("Connection established successfully.")
        except NoHostAvailable as e:
            logger.error("No host available. Please check the host details.")
            raise

        # Initializing class variables
        self.keyspace = keyspace
        self.table = table
        self.vector_column = vector_column
        self.vector_value = vector_value
        self.vector_count = vector_count
        self.user_input = user_input
        self.custom_query = custom_query

    def load_data(self, 
        query: Optional[str] = None,)-> List[Document]:
        """
        Method to load data, which calls the execute_query method.
        """
        return self.execute_query()

    def execute_query(
        self, 
        query: Optional[str] = None,
    ) -> List[Document]:
        """
        Method to execute a provided CQL query.
        If no query is provided, it executes a default "SELECT ALL" query on the specified keyspace and table.
        Returns a list of documents.
        """
        if not query:
            query = f"SELECT * FROM {self.keyspace}.{self.table};"
        documents = []
        try:
            cursor = self.session.execute(query)
            print(cursor)
            for item in cursor:
                documents.append(Document(text=str(item)))
                print(str(item))
            return documents
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise


    def vector_search(self):
        """
        Method to perform vector search on the specified keyspace and table.
        Generates a CQL query that orders by the provided vector column and limits the result set to the provided vector count.
        """
        vector_count = str(self.vector_count)
        vector_query= f"SELECT * FROM {self.keyspace}.{self.table} ORDER BY {self.vector_column} ANN OF [{self.vector_value}] LIMIT {vector_count};"
        print(vector_query)
        try:
            return self.execute_query(query=vector_query)
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise

    def insert_vectors(self, vectors: Dict[str, Dict[str, float]]) -> None:
        """
        Method to insert vectors into the specified keyspace and table.
        It takes a dictionary of vectors where dictionary keys are considered as row IDs and the values as the corresponding vectors.
        """
        try:
            keyspace_meta: KeyspaceMetadata = self.cluster.metadata.keyspaces.get(self.keyspace)
            if not keyspace_meta:
                raise ValueError(f"Keyspace '{self.keyspace}' does not exist.")
            table_meta = keyspace_meta.tables.get(self.table)
            if not table_meta:
                raise ValueError(f"Table '{self.table}' does not exist.")
            vector_column = self.vector_column
            if not vector_column:
                raise ValueError("No vector column provided.")
            for row_id, data in vectors.items():
                columns = ', '.join(data.keys())
                values = ', '.join([f"'{v}'" if isinstance(v, str) else str(v) for v in data.values()])
                insert_query = f"INSERT INTO {self.keyspace}.{self.table} (id, {columns}) VALUES ({row_id}, {values});"
                self.session.execute(insert_query)
                print(insert_query)
            logger.info("Vectors inserted successfully.{insert_query}")
        except Exception as e:
            print(insert_query)
            logger.error(f"An error occurred while inserting vectors: {e} {insert_query}")
            raise

    def query_generator(self) -> str:
        """
        Method to generate CQL queries based on user instructions and table definitions.
        Executes the generated query and returns the result.
        """
        table_definitions = {}
        try:
            keyspace_meta: KeyspaceMetadata = self.cluster.metadata.keyspaces.get(self.keyspace)
            if not keyspace_meta:
                raise ValueError(f"Keyspace '{self.keyspace}' does not exist.")

            for table_name, table_meta in keyspace_meta.tables.items():
                table_definitions[table_name] = table_meta.export_as_string()
        except Exception as e:
            logger.error(f"An error occurred: {e}")
            raise
        messages = [
        ChatMessage(role="system", content=f"You are a query interpreter for a Cassandra database, you will receive instructions from users and the definition of the tables where the data is stored. You will reply back only with the CQL query needed. Exclude from the query any settings such as consistency level or table properties. Do not include anything else in your answer but the query ready to be executed. Here are the table definitions: {table_definitions}."),
        ChatMessage(role="user", content=f"Here is the user instruction: {self.user_input}"),]
        prompt_query = OpenAI().chat(messages)
        prompt_query = str(prompt_query).replace("assistant: ", "")
        query_statement = SimpleStatement(prompt_query,
        consistency_level=ConsistencyLevel.LOCAL_QUORUM)
        result=self.session.execute(query_statement)
        result_str = '\n'.join([str(row) for row in result])
        return result_str
