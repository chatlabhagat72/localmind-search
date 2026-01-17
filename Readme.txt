# 🧠 LocalMind Doc-Search

A private, local RAG (Retrieval-Augmented Generation) system that lets you chat with your PDF documents using **Llama 3** and **Streamlit**. 

Unlike standard AI tools, this system runs **100% locally**. Your data never leaves your machine, ensuring total privacy for your sensitive documents.

---

## 🚀 Features
- **Total Privacy:** No cloud APIs, no data leaks.
- **Fast Search:** Uses ChromaDB vector storage for instant document retrieval.
- **User-Friendly UI:** Clean chat interface built with Streamlit.
- **Powered by Ollama:** High-performance local inference with Llama 3.

---

## 🛠️ Tech Stack
- **Language:** Python
- **LLM:** [Ollama](https://ollama.com/) (Llama 3)
- **Framework:** LangChain
- **Database:** ChromaDB (Vector Store)
- **Frontend:** Streamlit

---

## 📋 Prerequisites
Ensure you have the following installed:
1. **Python 3.10+**
2. **Ollama:** [Download here](https://ollama.com/)
   - Pull the model: `ollama pull llama3`

---

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/localmind-search.git](https://github.com/YOUR_USERNAME/localmind-search.git)
   cd localmind-search