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
    ans = lm.invoke(st.session_state.msgs)
    st.chat_message("ai").markdown(ans.content)
    st.session_state.msgs.append({"role":"ai","content":ans.content})

st.markdown("""
    <style>
        html,body,[data-testid="stAppViewContainer"].section.main {
            background: linear-gradient(135deg, #0f172a, #1e293b) ! important;
            color:white important;
        }
        .main-title {
            font-size: 40px; font-weight: 700; color: white; text-align: center; margin-bottom: 10px;
        }
        .sub-title {
            text-align: center; color: #cbd5e1: margin-bottom: 30px;
        }
        .chat-container {
            background-color: #1e293b; padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
        }
        .stChatMessage { 
            border-radius: 12px !important; padding: 10px !important;
        }
        .stTextInput>div>div>input { 
            background-color: #334155; 
            color: white: 
            border-radius: 10px;
        }
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

