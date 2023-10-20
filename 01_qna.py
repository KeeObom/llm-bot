from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain import OpenAI

load_dotenv()
embeddings = OpenAIEmbeddings()

# Loading texts/documents
loader = DirectoryLoader('news', glob="**/*.txt") 
documents = loader.load()

# Splitting Texts like Tokenization
text_splitter = CharacterTextSplitter(chunk_size=2500, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Use the Chroma Vector Store to store embeddings and metadata
vecstore = Chroma.from_documents(texts, embeddings)
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(),
    chain_type="stuff",
    retriever=vecstore.as_retriever()
)

def query(q):
    print("Query: ", q)
    print("Answer: ", qa.run(q))


query("What are the effects of legislations surrounding emissions on the Australia coal market?")
query("What are China's plans with renewable energy?")
query("Is there an export ban on Coal in Indonesia? Why?")
query("Who are the main exporters of Coal to China? What is the role of Indonesia in this?")
