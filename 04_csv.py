from dotenv import load_dotenv
from langchain import OpenAI
#from langchain.document_loaders.csv_loader import CSVLoader
from langchain.agents import create_csv_agent

load_dotenv()

filepath = "academy/salary.csv"
llm = OpenAI(temperature=0)
agent = create_csv_agent(llm, filepath, verbose=True)
# Questions to ask
agent.run("What are the percentages of the various Titles for the repondents?")
agent.run("Who is the accountant with the highest paid overtime?")
