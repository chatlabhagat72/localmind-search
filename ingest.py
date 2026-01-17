import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. Load the PDF (Make sure your file is named data.pdf in the docs folder)
print("Loading document...")
loader = PyPDFLoader("./docs/data.pdf")
docs = loader.load()

# 2. Split the text into small chunks
# This helps the AI find specific answers without getting overwhelmed
print("Splitting text into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(docs)

# 3. Create the searchable database (Vector Store)
# We use llama3 to turn the text into "math" (embeddings)
print("Creating database... This may take a minute.")
vectorstore = Chroma.from_documents(
    documents=splits, 
    embedding=OllamaEmbeddings(model="llama3"),
    persist_directory="./db"
)

print("✅ Finished! Your document is now indexed and ready to search.")