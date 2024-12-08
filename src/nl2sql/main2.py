import os
import logging
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker
from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("OpenAI API key is not set in environment variables.")
    exit(1)


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Securely load OpenAI API key from environment variables
if not openai_api_key:
    logger.error("OpenAI API key is not set in environment variables.")
    exit(1)

# Set up MySQL connection details securely using environment variables
db_user = os.getenv("DB_USER", "app_user")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "testdb")

if not db_password:
    logger.error("Database password is not set in environment variables.")
    exit(1)

# Create a connection to MySQL database
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
Session = sessionmaker(bind=engine)

# Inspect database tables
def inspect_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    logger.info(f"Usable Tables: {tables}")

    # Get detailed table info
    for table in tables:
        columns = inspector.get_columns(table)
        logger.info(f"Table: {table}")
        for column in columns:
            logger.info(f"  Column: {column['name']} | Type: {column['type']}")

inspect_tables()

# Initialize LangChain database connection
def initialize_langchain_db():
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    logger.info(f"Dialect: {db.dialect}")
    logger.info(f"Usable Tables: {db.get_usable_table_names()}")
    logger.info(f"Table Info: {db.table_info}")
    return db

db = initialize_langchain_db()

# Create SQL query using LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
generate_query = create_sql_query_chain(llm, db)

# Generate the SQL query from the natural language question
def generate_sql_query(question: str):
    query = generate_query.invoke({"question": question})
    logger.info(f"Generated SQL Query: {query}")
    return query

query = generate_sql_query("What is Alice's email address?")

# Execute the query using a session
def execute_query(query):
    try:
        with Session() as session:
            result = session.execute(text(query))
            rows = result.fetchall()
            return rows
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        return []

rows = execute_query(query)

# Display results
if rows:
    logger.info("Query Result:")
    for row in rows:
        logger.info(row)
else:
    logger.info("No results found.")

