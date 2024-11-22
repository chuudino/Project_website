import streamlit as st

st.write("# Welcome to class 13-1!")

with st.expander("點擊展開/收起"):
    st.write("這是expand內容")

st.write("---")

num = st.number_input("輸入一個數字", step=10, max_value=100, min_value=0)
st.write(f"### 您輸入的數字是：{num}")

st.write("---")
text = st.text_input("輸入一個文字")
st.write(f"### 您輸入的文字是：{text}")

st.write("---")
if st.button("點擊", key="btn"):
    st.write("點擊了")
    st.balloons()
if st.button("點擊", key="btn1"):
    st.write("點擊了")
    st.balloons()
