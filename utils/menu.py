import streamlit as st
import os


def menu():
    # 初始化 session_state
    if "current_page" not in st.session_state:
        st.session_state.current_page = "首頁"

    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")

    st.sidebar.title("課程")
    st.sidebar.page_link(page="pages/CLASS13.py", label="課程 13", icon="🐆")
    st.sidebar.page_link(page="pages/CLASS14.py", label="課程 14", icon="🎄")
    st.sidebar.page_link(page="pages/CLASS15.py", label="課程 15", icon="🦒")
    st.sidebar.page_link(page="pages/CLASS15_HW.py", label="課程 15 作業", icon="🏋️")
    st.sidebar.page_link(page="pages/CLASS16_1.py", label="課程 16_1", icon="🎇")
    st.sidebar.page_link(page="pages/CLASS16_2.py", label="課程 16_2", icon="🧨")
    st.sidebar.page_link(page="pages/CLASS16_3.py", label="課程 16_3", icon="🎉")
    st.sidebar.page_link(page="pages/CLASS16_4.py", label="課程 16_4", icon="🐶")
    st.sidebar.markdown("---")

    # 新增下拉選單，讀取pages資料夾下的所有檔案當作選項
    st.sidebar.title("下拉選單測試")
    pages_list = os.listdir("pages")
    page_names = ["首頁"]
    for page in pages_list:
        page_names.append(page.split(".")[0])
    selected_page = st.sidebar.selectbox(
        "選擇頁面：", page_names, index=page_names.index(st.session_state.current_page)
    )
    if st.sidebar.button("傳送"):
        st.session_state.current_page = selected_page
        if selected_page == "首頁":
            st.switch_page("main.py")
        else:
            st.switch_page(f"pages/{selected_page}.py")
