import os
import pinecone
from langchain.vectorstores import Pinecone
from app.chat.embeddings.openai import embeddings

pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

host = os.getenv("PINECONE_HOST")
index = pinecone.Index(os.getenv("PINECONE_INDEX_NAME"), host)

# Initialize the Pinecone vector store with the required 'text_key' argument
vector_store = Pinecone(
    index,
    embeddings,
    text_key=os.getenv("PINECONE_INDEX_NAME")
)