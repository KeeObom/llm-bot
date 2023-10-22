from dotenv import load_dotenv
from langchain import OpenAI, SQLDatabase #, SQLDatabaseChain
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()

dburi = "sqlite:///academy/salary.db"
db = SQLDatabase.from_uri(dburi)
llm = OpenAI(temperature=0)

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True)
db_chain.run("How many rows in in the responses table of this db?")
db_chain.run("What is the highest, lowest and average pay for the responses?")
db_chain.run("What Authority Name are the top 3 earners from?")
db_chain.run("Describe the responses table")


