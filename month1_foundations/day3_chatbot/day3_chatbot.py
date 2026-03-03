import requests
import json

# ── Config ──────────────────────────────────────────────────────────────────
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL      = "mistral"

# ── Personalities (system prompts) ──────────────────────────────────────────
PERSONALITIES = {
    "1": {
        "name": "🏴‍☠️ Pirate",
        "prompt": (
            "You are a salty old pirate captain. Speak in pirate slang — use "
            "words like 'arr', 'matey', 'landlubber', 'Davy Jones', etc. "
            "Keep answers helpful but always in character."
        ),
    },
    "2": {
        "name": "🤖 Robot",
        "prompt": (
            "You are a robot from the year 3000. Speak in a very literal, "
            "logical way. Refer to humans as 'carbon-based units'. Occasionally "
            "mention your internal processing or memory banks."
        ),
    },
    "3": {
        "name": "🧙 Wizard",
        "prompt": (
            "You are an ancient and wise wizard. Speak in a mystical, "
            "old-English style. Use words like 'thee', 'thou', 'hath', 'verily'. "
            "Refer to technology as if it were magic."
        ),
    },
}

# ── Temperature presets ──────────────────────────────────────────────────────
TEMPERATURES = {
    "1": ("🧊 Precise  (0.2)", 0.2),
    "2": ("⚖️  Balanced (0.7)", 0.7),
    "3": ("🔥 Creative (1.2)", 1.2),
}


def chat(messages: list, temperature: float) -> str:
    """Send messages to Ollama and return the assistant reply."""
    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature},
    }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()
    return response.json()["message"]["content"]


def pick_personality() -> tuple[str, str]:
    """Let the user choose a personality and return (name, system_prompt)."""
    print("\n── Choose a personality ────────────────────────")
    for key, p in PERSONALITIES.items():
        print(f"  {key}. {p['name']}")
    choice = input("Enter number: ").strip()
    p = PERSONALITIES.get(choice, PERSONALITIES["1"])
    print(f"  → {p['name']} selected!")
    return p["name"], p["prompt"]


def pick_temperature() -> float:
    """Let the user choose a temperature preset and return the float value."""
    print("\n── Choose a temperature ────────────────────────")
    for key, (label, _) in TEMPERATURES.items():
        print(f"  {key}. {label}")
    choice = input("Enter number: ").strip()
    label, temp = TEMPERATURES.get(choice, TEMPERATURES["2"])
    print(f"  → {label} selected!")
    return temp


def main():   
    print("=" * 50)
    print("   Day 3 — Personality Chatbot with Ollama")
    print("=" * 50)

    while True:
        print(f"\nChatting with BOT |  type 'quit' to exit type 'option' change the personality and temperature\n")
        print("-" * 50)
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("option"):            
            name, system_prompt = pick_personality()
            temperature = pick_temperature()
            # Seed the conversation with the system prompt
            messages = [{"role": "system", "content": system_prompt}]
            print(f"\nChatting with {name}  |  type 'quit' to exit type 'option' change the personality and temperature \n")
            print("-" * 50)
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            reply = chat(messages, temperature)
        except requests.RequestException as e:
            print(f"[Error] Could not reach Ollama: {e}")
            continue

        messages.append({"role": "assistant", "content": reply})
        print(f"\n{name}: {reply}\n")


if __name__ == "__main__":
    main()
