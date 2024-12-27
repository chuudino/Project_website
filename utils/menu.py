import streamlit as st


def menu():
    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")

    st.sidebar.title("課程")
    st.sidebar.page_link(page="pages/CLASS13.py", label="課程 13", icon="🐆")
    st.sidebar.page_link(page="pages/CLASS14.py", label="課程 14", icon="🎄")
    st.sidebar.page_link(page="pages/CLASS15.py", label="課程 15", icon="🦒")
    st.sidebar.page_link(page="pages/CLASS15_HW.py", label="課程 15 作業", icon="🐶")
    st.sidebar.page_link(page="pages/CLASS16.py", label="課程 16", icon="🐶")
    st.sidebar.page_link(page="pages/CLASS16_1.py", label="課程 16_1", icon="🎄")
    st.sidebar.page_link(page="pages/CLASS16_2.py", label="課程 16_2", icon="🎄")
    st.sidebar.page_link(page="pages/CLASS16_3.py", label="課程 16_3", icon="🎄")
    st.sidebar.markdown("---")
