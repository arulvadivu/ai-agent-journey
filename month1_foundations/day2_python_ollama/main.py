from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow all origins (for local dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return FileResponse("chatbot_ui.html")

@app.post("/chat")
def chat(req: ChatRequest):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": req.message,
        "stream": False
    })
    response.raise_for_status()
    return {"response": response.json()["response"]}
