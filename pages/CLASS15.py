import streamlit as st
import os

st.set_page_config(page_title="Dino's website", layout="wide")

if "ans" not in st.session_state:
    st.session_state["ans"] = 1

if "size" not in st.session_state:
    st.session_state["size"] = 100  # 設定預設值

size = st.session_state["size"]  # 縮短名稱, 因為session_state是字典
ans = 1

if st.button("點擊"):
    ans += 1
    st.session_state["ans"] += 1

st.write(f"一般變數ans的值為{ans}")
st.write(f"st.session_state['ans']的值為{st.session_state['ans']}")

st.write("---")
images_folder = "images"
images = os.listdir(images_folder)
st.write(images)

st.write("---")
st.title("圖片")
st.image("images/apple.png", width=300)

st.write("---")
st.title("下拉選單")
opt = st.selectbox("請選擇", ["選項1", "選項2", "選項3"])
st.write(opt)

st.write("---")
images_folder = "images"
images = os.listdir(images_folder)
st.title("綜合練習")

col1, col2 = st.columns(2)
with col1:
    with st.expander("點擊展開/收起"):
        image = st.selectbox("請選擇圖片", images)
        st.number_input("請輸入圖片大小", value=100, step=10, key="size")

with col2:
    st.image(f"{images_folder}/{image}", width=st.session_state["size"])
