import streamlit as st
from langchain_classic.chains import RetrievalQA
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

# Page Configuration
st.set_page_config(page_title="LocalMind Search", page_icon="🧠")
st.title("🧠 LocalMind Doc-Search")
st.markdown("---")

# 1. Setup the Brain (Ollama) and the Memory (ChromaDB)
@st.cache_resource # This keeps the app fast by loading the DB only once
def load_system():
    embeddings = OllamaEmbeddings(model="llama3")
    vectorstore = Chroma(persist_directory="./db", embedding_function=embeddings)
    llm = ChatOllama(model="llama3")
    
    # Create the Retrieval QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    return qa_chain

qa_system = load_system()

# 2. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Input
if prompt := st.chat_input("Ask something about your documents..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = qa_system.invoke(prompt)
            answer = response["result"]
            st.markdown(answer)
            
    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": answer})