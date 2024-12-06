import streamlit as st

st.set_page_config(page_title="Dino's website", layout="wide")
st.write("# columns練習")

col1, col2 = st.columns(2)
with col1:
    st.write("這是列1")
    st.button("點擊", key="btn")
with col2:
    st.write("這是列2")
    st.button("點擊", key="btn1")
st.write("---")
col1, col2 = st.columns([1, 2])
with col1:
    st.write("這是列1")
    st.button("點擊", key="btn2")
with col2:
    st.write("這是列2")
    st.button("點擊", key="btn3")
st.write("---")
col1, col2, col3 = st.columns([1, 2, 3])
with col1:
    st.write("這是列1")
    st.button("點擊", key="btn4")
with col2:
    st.write("這是列2")
    st.button("點擊", key="btn5")
with col3:
    st.write("這是列3")
    st.button("點擊", key="btn6")
st.write("---")
col1, col2 = st.columns(2)
with col1:
    st.button("點擊", key="btn7")
    st.button("點擊", key="btn8")
    st.button("點擊", key="btn9")
with col2:
    st.write("這是列2")
    st.write("這是列2")
    st.write("這是列2")
st.write("---")
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        # st.button("點擊", key=f"btn{i+10}")
        if st.button("點擊", key=f"btn{i+10}"):
            st.write("點擊了")
            st.balloons()
    with col2:
        st.write(f"這是列2")
    st.write("---")
