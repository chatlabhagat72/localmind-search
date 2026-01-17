[🧠 LocalMind Doc-Search_ Private RAG Chat with Your Documents.md](https://github.com/user-attachments/files/24686767/LocalMind.Doc-Search_.Private.RAG.Chat.with.Your.Documents.md)
# 🧠 LocalMind Doc-Search: Private RAG Chat with Your Documents

## Introduction

**LocalMind Doc-Search** is a powerful, private, and entirely local **Retrieval-Augmented Generation (RAG)** system designed to let you chat with your personal PDF documents. Built on the principle of **total data privacy**, this application ensures that your sensitive information never leaves your machine, as it operates without relying on any external cloud APIs or services.

Leveraging the power of **Llama 3** for intelligent responses and **Streamlit** for a user-friendly chat interface, LocalMind transforms your local document collection into a searchable, conversational knowledge base.

## ✨ Features

*   **Total Privacy:** Operates 100% locally. Your documents and queries are processed entirely on your machine, guaranteeing no data leaks or external transmission.
*   **Local LLM Power:** Utilizes the high-performance **Llama 3** model via **Ollama** for state-of-the-art natural language understanding and generation.
*   **Fast Retrieval:** Employs **ChromaDB** as a vector store for efficient indexing and instant retrieval of relevant document chunks.
*   **User-Friendly Interface:** A clean and intuitive chat interface built with **Streamlit** for a seamless user experience.
*   **Modular Architecture:** Clear separation between document ingestion (`ingest.py`) and the chat application (`app.py`).

## 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python | Core programming language. |
| **LLM** | Ollama (Llama 3) | Local large language model for generation and embeddings. |
| **Framework** | LangChain | Orchestration framework for the RAG pipeline. |
| **Vector Store** | ChromaDB | Local database for storing document embeddings. |
| **Frontend** | Streamlit | Web framework for the interactive chat interface. |
| **Document Loading** | PyPDFLoader | Used in `ingest.py` to load and parse PDF files. |

## 📋 Prerequisites

Before running the application, ensure you have the following installed and configured:

1.  **Python 3.10+**
2.  **Ollama:** The local LLM server.
    *   Download and install Ollama from the [official website](https://ollama.com/).
    *   Pull the required Llama 3 model by running the following command in your terminal:
        ```bash
        ollama pull llama3
        ```

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/chatlabhagat72/localmind-search.git
cd localmind-search
```

### 2. Install Dependencies

It is highly recommended to use a virtual environment.

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required Python packages
pip install -r requirements.txt
```

## 🚀 Usage

The application is run in two distinct phases: **Document Ingestion** and **Chat Application**.

### Phase 1: Document Ingestion

First, you must process your PDF document to create a searchable vector database.

1.  **Prepare Document:** Create a directory named `docs` in the root of the project and place your PDF file inside it, naming it `data.pdf`.
    ```
    localmind-search/
    ├── docs/
    │   └── data.pdf  <-- Your document goes here
    ├── ingest.py
    ├── app.py
    └── ...
    ```

2.  **Run Ingestion Script:** Execute the `ingest.py` script. This will load the PDF, split it into chunks, generate embeddings using Llama 3, and save the vector store to a local directory named `.db`.

    ```bash
    python ingest.py
    ```
    *   *Note: This process may take a few minutes depending on the size of your document and the speed of your machine.*

### Phase 2: Running the Chat Application

Once the database is created, you can start the Streamlit application to begin chatting with your document.

1.  **Start the App:**
    ```bash
    streamlit run app.py
    ```

2.  **Access the UI:** The command will automatically open the Streamlit web interface in your browser (usually at `http://localhost:8501`).

3.  **Start Chatting:** You can now ask questions related to the content of your `data.pdf`. The RAG system will retrieve the most relevant sections and use Llama 3 to formulate an accurate answer.

## 📂 Project Structure

| File/Directory | Description |
| :--- | :--- |
| `app.py` | The main Streamlit application file. Contains the chat interface logic and the RAG chain setup. |
| `ingest.py` | Script for document processing. Loads PDF, chunks text, creates embeddings, and persists the ChromaDB vector store. |
| `ask.py` | (Presumed) A command-line interface or helper script for direct querying (not used in the Streamlit flow). |
| `requirements.txt` | Lists all necessary Python dependencies. |
| `.db/` | Directory where the ChromaDB vector store is persisted after running `ingest.py`. |
| `docs/` | Directory for storing the source PDF document (`data.pdf`). |

## 🤝 Contributing

We welcome contributions to improve LocalMind Doc-Search! If you have suggestions for features, bug fixes, or improvements, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/amazing-feature`).
3.  Commit your changes (`git commit -m 'Add some amazing feature'`).
4.  Push to the branch (`git push origin feature/amazing-feature`).
5.  Open a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. (Assuming MIT License, as it is common for open-source projects. If a LICENSE file exists, the user should verify this.)

***

*by chatlabhagat *
