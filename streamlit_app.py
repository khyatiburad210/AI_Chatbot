import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

st.title("🤖 AI Chatbot")

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENAI_API_KEY"],
    model="openai/gpt-3.5-turbo",
    temperature=0.7
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    response = llm.invoke([HumanMessage(content=user_input)])
    reply = response.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
