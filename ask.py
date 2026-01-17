import os
# We use langchain_classic to fix the "ModuleNotFoundError"
from langchain_classic.chains import RetrievalQA 
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

# 1. Connect to your local database
print("--- Connecting to Database ---")
embeddings = OllamaEmbeddings(model="llama3")
vectorstore = Chroma(persist_directory="./db", embedding_function=embeddings)

# 2. Setup the Brain (Llama 3)
print("--- Warming up Llama 3 ---")
llm = ChatOllama(model="llama3")

# 3. Create the Assistant (using the classic chain)
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever()
)

# 4. The Search Loop
while True:
    query = input("\nAsk a question about your docs (or type 'exit'): ")
    
    if query.lower() == 'exit':
        break

    print("Searching...")
    # Invoke the chain to get the answer
    result = qa_chain.invoke({"query": query})
    
    print("\n--- AI ANSWER ---")
    print(result["result"])