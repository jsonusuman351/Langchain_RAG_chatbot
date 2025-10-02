# 🧠 Full-Stack RAG Chatbot with LangChain & Streamlit

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python) ![LangChain](https://img.shields.io/badge/LangChain-0086CB?style=for-the-badge&logo=langchain) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit) ![ChromaDB](https://img.shields.io/badge/Chroma-5B33F3?style=for-the-badge&logo=chroma) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai) ![LangSmith](https://img.shields.io/badge/LangSmith-FD8C23?style=for-the-badge)

Hey there! Welcome to my most ambitious project yet: a complete, full-stack **Retrieval-Augmented Generation (RAG)** chatbot. After exploring all the individual components of LangChain—from prompts and models to chains and vector stores—I wanted to bring everything together into a real, usable application.

This project is a fully functional system with a **FastAPI backend** that handles all the AI logic and a **Streamlit frontend** that provides a clean, interactive chat interface. It can ingest PDF documents, create a searchable knowledge base, and answer questions based on the content of those documents.

---

### ✨ Core Features & My Architectural Approach

I designed this project with a clean, decoupled architecture, separating the AI backend from the user-facing application.

1.  **Backend API (Powered by FastAPI)**:
    -   I built a robust backend service that exposes several endpoints to manage the RAG pipeline.
    -   **Document Ingestion**: An endpoint to upload PDF files. The API automatically loads, splits, and embeds the document content.
    -   **Vector Store Management**: I used **ChromaDB** as my vector store. The API handles creating and persisting the database, ensuring our knowledge base is saved and reusable.
    -   **Conversational Q&A**: The core `/chat` endpoint takes a user's query and a conversation ID, retrieves relevant context from ChromaDB, and uses a powerful LangChain `Runnable` chain to generate a fact-based answer.
    -   **Chat History Management**: I implemented a simple SQLite database to store and retrieve conversation histories, allowing the chatbot to remember past interactions for more natural, context-aware conversations.

2.  **Frontend Chat Application (Powered by Streamlit)**:
    -   I created a user-friendly frontend that communicates with the FastAPI backend.
    -   It features a sidebar for uploading PDF documents and a main chat interface for interacting with the AI.
    -   The UI displays the conversation in a familiar chat format and even shows the source documents that the AI used to generate its answer.

3.  **Advanced RAG Pipeline**:
    -   Instead of a simple chain, I used the modern **LangChain Expression Language (LCEL)** and `Runnables` to build a sophisticated chain. This chain dynamically fetches chat history, retrieves relevant documents, and formats the final prompt for the LLM.

4.  **Observability with LangSmith**:
    -   To debug and monitor my complex chains, I integrated **LangSmith**. This was a game-changer. It gives me a clear, visual trace of every step in my RAG pipeline, from document retrieval to the final LLM call, making it incredibly easy to see what's happening under the hood.

---

### 📸 Screenshots

Here’s a look at the different components of the project in action.

**The Streamlit Chat Interface:**
*This is the main UI where users can upload a PDF and chat with the AI about its content.*
![Screenshot of the Streamlit application interface]![Image](https://github.com/user-attachments/assets/1c9f7553-0fc1-443b-97c9-da44f7fc5597)
**The FastAPI Backend Running (Uvicorn):**
*This is the engine of the application, handling all the AI logic.*
![Screenshot of the Uvicorn server running the FastAPI backend] ![Image](https://github.com/user-attachments/assets/01c3068e-2350-4828-a27a-60f9b51b4fdd)
![Image](https://github.com/user-attachments/assets/a77c87c1-dafd-4519-9104-65772064ee7d)

**Monitoring with LangSmith:**
*LangSmith provides an amazing view into the inner workings of the RAG chain, showing exactly how the context is retrieved and used.*
![Screenshot of a LangSmith trace showing the RAG chain's execution] ![Image](https://github.com/user-attachments/assets/500de463-04c2-4088-93fe-c40982af4fb1)
![Detailed view of a LangSmith trace showing individual steps] ![Image](https://github.com/user-attachments/assets/a056fd7d-ceb1-429e-ace6-bfc76fd37451)

---

### 🛠️ Tech Stack

-   **Backend**: FastAPI, Uvicorn
-   **Frontend**: Streamlit
-   **Core AI Framework**: LangChain, LCEL
-   **LLM & Embedding Provider**: OpenAI
-   **Vector Database**: ChromaDB
-   **Chat History Database**: SQLite
-   **Observability**: LangSmith
-   **Core Libraries**: `pydantic`, `python-dotenv`, `PyPDF`

---

### ⚙️ Setup and Installation

This project has two main components: the backend API and the frontend app. They need to be run separately.

#### Part 1: Setting Up the Backend API

1.  **Navigate to the API directory:**
    ```bash
    cd api
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # It is recommended to use Python 3.10 or higher
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables:**
    -   In the `api/` directory, create a file named `.env`.
    -   Add your API keys to this file. You'll need keys for OpenAI and LangSmith.
        ```env
        OPENAI_API_KEY="your-openai-api-key"
        LANGCHAIN_API_KEY="your-langsmith-api-key"
        LANGCHAIN_TRACING_V2="true"
        LANGCHAIN_PROJECT="your-langsmith-project-name" 
        ```

#### Part 2: Setting Up the Frontend App

1.  **Open a new terminal.**
2.  **Navigate to the App directory:**
    ```bash
    cd app
    ```
3.  **Create and activate a separate virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

---

### 🚀 How to Run the Application

You need to run both the backend and the frontend in separate terminals.

1.  **Run the Backend API:**
    -   In the first terminal (for the `api` directory), run this command to start the Uvicorn server:
        ```bash
        uvicorn main:app --reload --port 8000
        ```
    -   The API will be running at `http://localhost:8000`.

2.  **Run the Streamlit Frontend:**
    -   In the second terminal (for the `app` directory), run this command:
        ```bash
        streamlit run streamlit_app.py
        ```
    -   This will open the application in a new tab in your web browser. Now you can upload a PDF and start chatting!

---

### 🔬 Project Structure

I've organized the project into two distinct parts: `api` for the backend logic and `app` for the frontend interface.

<details>
<summary>Click to view the project layout</summary>

```
langchain_rag_chatbot/
│
├── api/
│   ├── main.py             # FastAPI application logic
│   ├── langchain_utils.py  # Core LangChain RAG implementation
│   ├── chroma_utils.py     # Functions for interacting with ChromaDB
│   ├── db_utils.py         # Functions for the SQLite chat history
│   ├── pydantic_models.py  # Pydantic models for API requests
│   ├── requirements.txt
│   └── .env                # (You need to create this)
│
└── app/
    ├── streamlit_app.py    # The main Streamlit UI
    ├── chat_interface.py   # UI components for the chat
    ├── sidebar.py          # UI components for the sidebar and uploader
    ├── api_utils.py        # Functions to call the FastAPI backend
    ├── requirements.txt
    └── venv/
```
</details>

---

---