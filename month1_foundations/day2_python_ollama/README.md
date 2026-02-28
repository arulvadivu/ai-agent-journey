# 🦙 Ollama Chatbot

A local AI chatbot powered by **Ollama + Mistral** with a **FastAPI** backend and a sleek dark UI.

---

## 🏗️ Project Structure

```
project/
├── main.py           # FastAPI backend
├── chatbot_ui.html   # Frontend UI
├── requirements.txt  # Python dependencies
└── README.md
```

---

## ⚙️ Prerequisites

- [Docker](https://www.docker.com/) installed
- Python 3.8+
- pip

---

## 🐳 Step 1: Run Ollama in Docker

```bash
docker run -d \
  -e OLLAMA_ORIGINS="*" \
  -v ollama:/root/.ollama \
  -p 11434:11434 \
  --name ollama \
  ollama/ollama
```

### Pull Mistral Model

```bash
docker exec -it ollama ollama pull mistral
```

### Verify Ollama is Running

```bash
curl http://localhost:11434
```

Expected output: `Ollama is running`

---

## 🐍 Step 2: Setup Python Environment

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Step 3: Run FastAPI Backend

```bash
uvicorn main:app --reload
```

Server starts at: `http://localhost:8000`

---

## 🌐 Step 4: Open the Chatbot

Open your browser and go to:

```
http://localhost:8000
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/`      | Serves the chat UI |
| POST   | `/chat`  | Send a message, get a response |

### Example API Call

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello!"}'
```

### Response

```json
{
  "response": "Hello! How can I help you today?"
}
```

---

## 🏛️ Architecture

```
Browser (chatbot_ui.html)
        ↓
FastAPI Backend (port 8000)
        ↓
Ollama Docker Container (port 11434)
        ↓
Mistral 7B Model
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| LLM | Mistral 7B via Ollama |
| Backend | FastAPI + Uvicorn |
| Frontend | HTML + CSS + JavaScript |
| Container | Docker |

---

## 📦 requirements.txt

```
fastapi
uvicorn
requests
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Ollama not running | `docker start ollama` |
| Model not found | `docker exec -it ollama ollama pull mistral` |
| CORS error | Make sure `OLLAMA_ORIGINS=*` is set in Docker |
| Port in use | Change port: `uvicorn main:app --port 8001` |

---

