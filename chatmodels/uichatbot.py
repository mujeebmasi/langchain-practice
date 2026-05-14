import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile"
)

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny assistant.")
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(message)

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(HumanMessage(content=prompt))
    st.session_state.chat_history.append(("user", prompt))

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    st.session_state.chat_history.append(
        ("assistant", response.content)
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        st.markdown(response.content)