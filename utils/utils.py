import streamlit as st
from .menu import menu


def init_page():
    st.set_page_config(
        page_title="Singular 範例頁面",
        page_icon=":shark:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    menu()
