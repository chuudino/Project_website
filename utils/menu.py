import streamlit as st
import os
import random
import emojis

# 定義一些可用的 emoji 表情符號
emojis = list(emojis.db.get_emoji_aliases().values())


def menu():
    if "pages_list" not in st.session_state:
        pages_list = os.listdir("pages")
        page_names = ["首頁"]
        for page in pages_list:
            page_names.append(page.split(".")[0])

        # 為每個頁面名稱加上隨機 icon
        st.session_state.pages_list = []
        for name in page_names:
            st.session_state.pages_list.append(f"{name} {random.choice(emojis)}")

    if "current_page" not in st.session_state:
        st.session_state.current_page = st.session_state.pages_list[0]

    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")

    st.sidebar.title("課程")
    selected_page_with_emoji = st.sidebar.selectbox(
        "選擇頁面：",
        st.session_state.pages_list,
        index=st.session_state.pages_list.index(st.session_state.current_page),
    )
    # 取得實際的頁面名稱（去除 emoji）
    selected_page = selected_page_with_emoji.split(" ")[0]

    if st.sidebar.button("傳送"):
        st.session_state.current_page = selected_page_with_emoji
        if selected_page == "首頁":
            st.switch_page("main.py")
        else:
            st.switch_page(f"pages/{selected_page}.py")
