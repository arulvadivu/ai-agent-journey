# 🤖 Generic CLI Q&A Bot with Ollama

A conversational CLI bot that turns into an expert on **any topic you choose** — powered by Ollama and Mistral running entirely on your local machine. No API keys, no internet required.

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
python bot.py
```

At startup, enter any topic you want to explore. The bot instantly becomes an expert on it.

```
========================================
       🤖 Generic CLI Q&A Bot
========================================

Enter a topic you want to explore: Space & Astronomy

✅ Bot is ready! Ask me anything about 'Space & Astronomy'.
Type 'reset' to change topic, 'quit' to exit.

You: How far is the moon?
Bot: The Moon is approximately 384,400 km from Earth on average...
```

---

## Commands

| Command | Action |
|---|---|
| Type a question + Enter | Ask the bot anything about the topic |
| `reset` | Switch to a new topic |
| `quit` | Exit the bot |

---

## How It Works

The chosen topic is injected into a dynamic system prompt at the start of the session. The bot then answers all questions in the context of that topic and redirects unrelated questions back to it.

```
User enters topic
       ↓
System prompt built dynamically
       ↓
User asks questions
       ↓
Full conversation history sent to Ollama API each turn
       ↓
Response printed to terminal
```

---

## Configuration

Edit these constants at the top of `bot.py`:

```python
OLLAMA_URL = "http://localhost:11434/api/chat"  # Ollama server URL
MODEL      = "mistral"                          # Model to use
```

---

## Example Topics

- Cricket
- Space & Astronomy
- World History
- Cooking & Recipes
- Stock Market Basics
- Docker & DevOps
- Anything you can think of!

---

## Project Structure

```
bot.py        # Main bot script
README.md     # This file
```

---

## License

MIT
