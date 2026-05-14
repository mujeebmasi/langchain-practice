from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)
messages = [
    SystemMessage(content="You are a funny assistant.")
]

print("______________________________WELCOME TO THE CHATBOT______________________________")
while True:
   
    prompt = input("You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot: ",response.content) 
print(messages)