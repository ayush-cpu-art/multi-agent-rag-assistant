# 🤖 Multi-Agent RAG Assistant

> A production-ready **Multi-Agent Retrieval-Augmented Generation (RAG) Assistant** built using **FastAPI, React, LangGraph, Groq LLM, and Qdrant**.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 Overview

This project is a **Multi-Agent RAG Assistant** capable of answering questions from uploaded documents using semantic search and Large Language Models.

Unlike a traditional chatbot, the application uses a **LangGraph-based multi-agent workflow**, where specialized agents collaborate to understand the user's query, retrieve relevant information, and generate grounded responses.

---

## ✨ Features

- 📄 Multi-document upload
- 🔍 Semantic search using Sentence Transformers
- 🤖 Multi-Agent workflow using LangGraph
- 🧠 Conversation memory
- ✍️ Query rewriting
- 📚 Source citations
- 👀 Chunk preview
- 🗑 Delete uploaded documents
- 📑 Export conversation to PDF
- 📝 Export conversation to Markdown
- 🌙 Light / Dark theme
- 📋 Copy AI responses
- ⚡ Fast inference using Groq LLM

---

# 🏗 Architecture

```
                React Frontend
                       │
                       ▼
                 FastAPI Backend
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
  LangGraph Workflow           Qdrant Vector DB
         │                           ▲
         ▼                           │
 Planner Agent                       │
         ▼                           │
 Query Rewriter                      │
         ▼                           │
 Retriever ──────────────────────────┘
         ▼
 Answer Agent
         ▼
 Critic Agent
         ▼
      Response
```

---

# 🛠 Tech Stack

| Layer | Technology |
|--------|------------|
| Frontend | React + Vite |
| Backend | FastAPI |
| Workflow | LangGraph |
| LLM | Groq (Llama 3.3 70B Versatile) |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | Qdrant |
| Markdown | react-markdown |
| PDF Export | jsPDF |
| Styling | CSS |

---

# 📂 Project Structure

```
multi-agent-rag-assistant/

├── backend/
│   ├── app/
│   ├── uploads/
│   ├── qdrant_db/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── README.md
└── .gitignore
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/ayush-cpu-art/multi-agent-rag-assistant

cd multi-agent-rag-assistant
```

---

## Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 🔑 Environment Variables

Create:

```
backend/.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

---

# 🚀 API Endpoints

| Method | Endpoint | Description |
|----------|-----------|------------|
| POST | /upload | Upload Documents |
| POST | /chat | Ask Questions |
| GET | /documents | List Documents |
| DELETE | /documents/{id} | Delete Document |
| GET | /chunks/{document_id} | Preview Chunks |

---

# 📸 Screenshots

## Home

> *(Add screenshot here)*

---

## Upload Documents

> *(Add screenshot here)*

---

## Chat

> *(Add screenshot here)*

---

# 🚀 Future Improvements

- Streaming Responses
- Hybrid Search
- OCR Support
- Authentication
- Chat Sessions
- Reranking
- Docker Deployment

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Ayush**

GitHub:
https://github.com/ayush-cpu-art