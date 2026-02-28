import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"  # Change to your installed model

def send_message(prompt: str) -> str:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["response"]

prompts = [
    "What is the capital of France?",
    "Explain quantum entanglement in one sentence.",
    "Write a haiku about coding.",
    "What are the three laws of thermodynamics?",
    "Give me a fun fact about octopuses."
]

for i, prompt in enumerate(prompts, 1):
    print(f"\n{'='*50}")
    print(f"Prompt {i}: {prompt}")
    print(f"{'='*50}")
    try:
        response = send_message(prompt)
        print(f"Response: {response}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Ollama. Make sure it's running with: ollama serve")
    except Exception as e:
        print(f"Error: {e}")
