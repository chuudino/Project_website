import streamlit as st
from utils import init_page
from openai import OpenAI
import os
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 初始化頁面
init_page()
st.title("聊天室")

# 初始化聊天歷史
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "你是一個有幫助的助手,請用繁體中文回答。"}]

# 顯示聊天歷史
for message in st.session_state.messages:
    if message["role"] != "system": # 不顯示系統訊息
        with st.chat_message(message["role"]):
            st.write(message["content"])

# 取得使用者輸入的訊息
if message := st.chat_input("請輸入訊息"):
    # 顯示使用者的訊息
    with st.chat_message("user"):
        st.write(message)
    # 儲存訊息到歷史
    st.session_state.messages.append({"role": "user", "content": message})

# 取得使用者輸入的訊息
if message :=st.chat_input("請輸入訊息"):

# …省略…

    try:
        completion =client.chat.completions.create(model="gpt-4o", messages = st.session_state.messages,))
        assistant_response=completion.choices[0].message.content
        # 顯示助手回覆
        with st.chat_message("assistant"):
            st.write(assistant_response)
        # 儲存助手回覆到歷史
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
    except Exception as e:
        st.error(f"發生錯誤: {str(e)}")