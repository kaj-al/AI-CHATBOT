import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
lm = ChatOpenAI(model="openai/gpt-4o", base_url="https://openrouter.ai/api/v1", max_tokens=1000)

st.title("CHITCHAT")
st.markdown("A QnA chatbot")

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for msg in st.session_state.msgs:
    role = msg["role"]
    content = msg["content"]
    st.chat_message(role).markdown(content)

question = st.chat_input("Question please...")
if question:
    st.session_state.msgs.append({"role":"user","content":question})
    st.chat_message("user").markdown(question)
    ans = lm.invoke(question)
    st.chat_message("ai").markdown(ans.content)
    st.session_state.msgs.append({"role":"ai","content":ans.content})

