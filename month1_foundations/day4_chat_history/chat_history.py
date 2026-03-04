
"""
Multi-turn chatbot using Ollama API.

"""

import requests
import json 

OLLAMA_URL="http://localhost:11434/api/chat"
MODEL="mistral"

def chat(history,user_input):    
    history.append({"role":"user","content":user_input})    
    response=requests.post(OLLAMA_URL,json={"model":MODEL,"messages":history,"stream":False})
    data=response.json()
    assistant_message=data["message"]["content"]    
    history.append({"role":"assistant","content":assistant_message})    
    return assistant_message,history

def main():
    print("🤖 Multi-turn Chat (type 'quit or bye' to exit, 'reset' to clear history)\n")
    print("***************************************************************************")
    system_prompt = {"role":"system","content":"you are helpul assistent"}
    history = [system_prompt]   
    while True:
        user_input=input("You : ").strip()
        if not user_input:
            continue
        if user_input.lower() in ('quit','bye'):
            print("Good bye..")
            break
        if user_input.lower() =='reset':
            history=[system_prompt]
            print('\n history cleared')
            continue
        response,history = chat(history,user_input)
        print(f"\nAssistant: {response}\n")
       

    
if(__name__=="__main__"):
   main()


