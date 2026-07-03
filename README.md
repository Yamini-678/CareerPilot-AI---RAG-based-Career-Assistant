# 🚀 CareerPilot AI

> **A Retrieval-Augmented Generation (RAG) powered Career Intelligence Assistant built using FastAPI, LangChain, FAISS, Gemini, MongoDB, and Streamlit.**

CareerPilot AI helps users upload their resume, ask resume-specific questions, receive personalized career guidance, generate learning roadmaps, and interact through a multi-turn conversational AI—all powered by Retrieval-Augmented Generation (RAG).

---

# ✨ Features

- 📄 Upload PDF/DOCX Resume
- 🧠 Resume Parsing & Text Extraction
- ✂️ Document Chunking
- 🔍 Semantic Search using FAISS
- 🤖 Resume Question Answering (RAG)
- 💬 Multi-turn Conversational AI
- 🎯 Personalized Career Advice
- 📚 AI Learning Roadmap Generator
- 🗄️ MongoDB Chat History
- ⚡ FastAPI REST APIs
- 🎨 Interactive Streamlit UI

---

# 🏗️ System Architecture

```
                   Resume Upload
                         │
                         ▼
                Text Extraction
                         │
                         ▼
                  Document Chunking
                         │
                         ▼
              Gemini Embedding Model
                         │
                         ▼
                 FAISS Vector Store
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
      Resume Question        Career Guidance
         Retrieval             Learning Plan
              │                     │
              └──────────┬──────────┘
                         ▼
                  Gemini 2.5 Flash
                         │
                         ▼
                   Final Response
```

---

# 🛠️ Tech Stack

### Backend

- FastAPI
- Python

### LLM

- Gemini 2.5 Flash

### RAG

- LangChain
- FAISS
- Google Embeddings

### Database

- MongoDB

### Frontend

- Streamlit

### Document Processing

- PyPDF
- python-docx

---

# 📂 Project Structure

```
CareerPilot-AI
│
├── app
│   ├── llm
│   ├── memory
│   ├── models
│   ├── rag
│   ├── routes
│   ├── services
│   └── main.py
│
├── uploads
├── faiss_index
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/Yamini-678/ResumeRAG-AI---RAG-based-Career-Assistant.git

cd CareerPilot-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GEMINI_API_KEY=your_api_key

MONGODB_URI=your_mongodb_connection_string
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Backend runs at

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run streamlit_app.py
```

---

# 📸 Screenshots


```
assets/home.png
```

---

# 📖 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/upload` | Upload Resume |
| POST | `/ask_resume` | Resume Q&A using RAG |
| POST | `/chat` | Multi-turn Conversation |
| POST | `/career` | Career Advice & Learning Roadmap |

---

# 🎯 Learning Outcomes

This project helped me understand:

- Retrieval-Augmented Generation (RAG)
- Document Chunking
- Embedding Generation
- Vector Databases (FAISS)
- Semantic Search
- Prompt Grounding
- FastAPI Backend Development
- Streamlit Frontend Development
- MongoDB Integration
- Multi-turn LLM Conversations

---

# 🔮 Future Improvements

- Hybrid Search (BM25 + Vector Search)
- Cross-Encoder Reranking
- Multi-Document RAG
- Conversation Summarization
- User Authentication
- Cloud Deployment
- Docker Support

---

# 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

If you find this project useful, consider giving it a ⭐.

---

# 📬 Contact

**Yamini Bisht**

📧 yaminibisht678@gmail.com

🔗 LinkedIn: https://linkedin.com/in/yamini2704

💻 GitHub: https://github.com/Yamini-678

---

⭐ If you found this project interesting, don't forget to star the repository!