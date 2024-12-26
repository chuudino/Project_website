import streamlit as st

def menu():
 st.sidebar.title("選單")
 st.sidebar.page_link(page="main.py", label="首頁", icon=" ")
 st.sidebar.markdown("---")
 st.sidebar.title("課程")
 st.sidebar.page_link(page="pages/class13.py", label="課程 13", icon=" ")
 st.sidebar.page_link(page="pages/class14.py", label="課程 14", icon=" ")
 st.sidebar.markdown("---")

st.set_page_config(page_title="Dino's website", page_icon: " ",layout="wide", initial_sidebar_state="auto")