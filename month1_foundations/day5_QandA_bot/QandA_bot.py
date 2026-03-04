"""
Generic CLI Q&A Bot using Ollama.
Ask questions on ANY topic you choose.
"""

import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "mistral"


def chat(history, user_message):
    history.append({"role": "user", "content": user_message})

    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": history,
        "stream": False
    })

    data = response.json()
    assistant_message = data["message"]["content"]
    history.append({"role": "assistant", "content": assistant_message})

    return assistant_message, history


def main():
    print("=" * 50)
    print("        Generic CLI Q&A Bot")
    print("=" * 50)

    topic = input("\nEnter a topic you want to explore: ").strip()

    system_prompt = {
        "role": "system",
        "content": f"You are an expert on {topic}. Answer all questions clearly and concisely. If a question is unrelated to {topic}, politely redirect the user back to the topic."
    }

    history = [system_prompt]

    print(f"\n Bot is ready! Ask me anything about '{topic}'.")
    print("Type 'reset' to change topic, 'quit' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        if user_input.lower() == "reset":
            topic = input("\nEnter new topic: ").strip()
            system_prompt = {
                "role": "system",
                "content": f"You are an expert on {topic}. Answer all questions clearly and concisely. If a question is unrelated to {topic}, politely redirect the user back to the topic."
            }
            history = [system_prompt]
            print(f"\nTopic changed! Ask me anything about '{topic}'.\n")
            continue

        response, history = chat(history, user_input)
        print(f"\nBot: {response}\n")


if __name__ == "__main__":
    main()
