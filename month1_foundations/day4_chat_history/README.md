# 🤖 Multi-Turn CLI Chatbot with Ollama

A simple conversational chatbot that runs entirely on your local machine using Ollama and Python. Supports multi-turn conversation memory, system prompts, and chat history reset.

---

## Requirements

- [Ollama](https://ollama.ai) installed and running
- Python 3.8+
- `requests` library

---

## Installation

**1. Install Ollama and pull Mistral:**
```bash
ollama pull mistral
```

**2. Install Python dependency:**
```bash
pip install requests
```

**3. Make sure Ollama is running:**
```bash
ollama serve
```

---

## Usage

```bash
python chat.py
```

Once running:

| Command | Action |
|---|---|
| Type a message + Enter | Send message to assistant |
| `reset` | Clear conversation history |
| `quit` | Exit the chatbot |

---

## How It Works

The script maintains a conversation `history` list — a sequence of messages with roles (`system`, `user`, `assistant`). On every turn, the full history is sent to the Ollama API so the model has context of the entire conversation.

```
User types message
       ↓
Appended to history
       ↓
Full history sent to Ollama API
       ↓
Response appended to history
       ↓
Printed to terminal
```

---

## Configuration

Edit these constants at the top of `chat.py` to customise behaviour:

```python
OLLAMA_URL = "http://localhost:11434/api/chat"  # Ollama server URL
MODEL      = "mistral"                          # Model to use
```

To change the assistant's personality, edit the system prompt in `main()`:

```python
system_prompt = {"role": "system", "content": "You are a helpful assistant."}
```

---

## Project Structure

```
chat.py       # Main chatbot script
README.md     # This file
```

---

## License

MIT
