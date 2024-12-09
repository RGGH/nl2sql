import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from langchain_community.utilities.sql_database import SQLDatabase 
from langchain.chains import create_sql_query_chain 
from langchain_openai import ChatOpenAI 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.SELECT e.first_name, e.last_name
FROM employees e
ORDER BY e.hire_date ASC
LIMIT 2, 1;INFO)
logger = logging.getLogger(__name__)

# OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    logger.error("OpenAI API key is not set in environment variables.")
    exit(1)

# Database connection details
db_user = os.getenv("DB_USER", "app_user")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_name = os.getenv("DB_NAME", "employees")

if not db_password:
    logger.error("Database password is not set in environment variables.")
    exit(1)

# Create SQLAlchemy engine and session
engine = create_engine(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
Session = sessionmaker(bind=engine)

# Initialize LangChain database
def initialize_langchain_db():
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    return db

db = initialize_langchain_db()

# Initialize LLM and query chain
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
generate_query = create_sql_query_chain(llm, db)

# Generate SQL query from natural language
def generate_sql_query(question: str):
    query = generate_query.invoke({"question": question})
    logger.info(f"Generated SQL Query: {query}")
    return query

# Execute SQL query
def execute_sql_query(query: str):
    try:
        with Session() as session:
            result = session.execute(text(query))
            rows = result.fetchall()
            return rows
    except Exception as e:
        logger.error(f"Error executing query: {e}")
        return []

# Rephrase the result using LangChain
def rephrase_result(question: str, query: str, result: list):
    # Prepare result in a string format for rephrasing
    result_str = "\n".join([str(row) for row in result])

    # Prompt template for rephrasing
    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

        Question: {question}
        SQL Query: {query}
        SQL Result: {result}
        Answer: """
    )

    rephrase_chain = answer_prompt | llm | StrOutputParser()
    response = rephrase_chain.invoke({
        "question": question,
        "query": query,
        "result": result_str
    })
    return response

# Main workflow
if __name__ == "__main__":
    question = "What is the name of the 3rd longest serving employee?"
    logger.info(f"User Question: {question}")

    # Generate and execute the query
    query = generate_sql_query(question)
    rows = execute_sql_query(query)

    if rows:
        # Rephrase the results
        response = rephrase_result(question, query, rows)
        logger.info(f"Rephrased Answer: {response}")
    else:
        logger.info("No results found.")
