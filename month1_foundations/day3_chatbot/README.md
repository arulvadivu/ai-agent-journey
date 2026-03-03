# 🤖 Local LLM Learning 

A hands-on 5-day project to get comfortable running and building with local LLMs using Ollama and Python.

---

## 🛠️ Setup

### Requirements
- [Ollama](https://ollama.ai) installed and running
- Python 3.8+
- `requests` library

### Install dependencies
```bash
pip install requests
```

### Pull the model
```bash
ollama pull mistral
```

---

## 📁 Files

### `day3_chatbot.py` — Personality Chatbot
A CLI chatbot with selectable personalities and temperature settings.

**Run:**
```bash
python day3_chatbot.py
```

**Features:**
- 3 built-in personalities: Pirate 🏴‍☠️, Robot 🤖, Wizard 🧙
- 3 temperature presets: Precise (0.2), Balanced (0.7), Creative (1.2)
- System prompt injection
- Persistent chat history within a session

---

## 🧠 Concepts Covered

- **Ollama** — running LLMs locally with zero cloud dependency
- **Python API calls** — communicating with Ollama via `requests`
- **System prompts** — shaping model personality and behavior
- **Temperature** — controlling response randomness and creativity
- **Chat history** — maintaining multi-turn conversation context

