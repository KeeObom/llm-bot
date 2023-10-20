from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings

load_dotenv()
embeddings = OpenAIEmbeddings()
text = "What are you eating today?"
doc_embeddings = embeddings.embed_documents([text])

print(doc_embeddings)



