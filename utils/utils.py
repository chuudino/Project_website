import streamlit as st
from .menu import menu


def init_page():
    st.set_page_config(page_title="Dino's website", page_icon="🦖", layout="wide")
    menu()
