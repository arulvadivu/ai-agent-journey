import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def send_message(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

print("🤖 Chatbot Ready! (type 'quit' to exit)")
print("=" * 40)

while True:
    user_input = input("\nYou: ").strip()
    
    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye! 👋")
        break
    
    if not user_input:
        continue

    print("Bot: Thinking...")
    response = send_message(user_input)
    print(f"Bot: {response}")
