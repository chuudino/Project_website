import streamlit as st
from utils import init_page

init_page()
st.title("這是首頁")

st.set_page_config(page_title="Dino's website", layout="wide")
st.title("Welcome~")  # 這是標題

# to view this Streamlit app on a browser, run it with the following
# command:streamlit run d:\Python\Project_website\main.py
