import ollama

# Test 1 - Basic response
print("=== Test 1: Basic Question ===")
response = ollama.chat(
    model='mistral',
    messages=[
        {'role': 'user', 'content': 'What is an AI agent in 3 lines?'}
    ]
)
print(response['message']['content'])

# Test 2 - System prompt
print("\n=== Test 2: With System Prompt ===")
response = ollama.chat(
    model='mistral',
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant who explains things simply.'},
        {'role': 'user', 'content': 'What is LangChain?'}
    ]
)
print(response['message']['content'])

# Test 3 - Conversation memory
print("\n=== Test 3: Multi-turn Conversation ===")
messages = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'My name is Sarul.'},
]
response = ollama.chat(model='mistral', messages=messages)
print(response['message']['content'])

# Add assistant response to history
messages.append({'role': 'assistant', 'content': response['message']['content']})
messages.append({'role': 'user', 'content': 'What is my name?'})

response = ollama.chat(model='mistral', messages=messages)
print(response['message']['content'])