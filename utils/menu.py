import streamlit as st
import os
import random
import emojis

# 從 emojis 資料庫獲取所有可用的表情符號
# 這些表情符號將用於為頁面添加隨機圖標
emojis = list(emojis.db.get_emoji_aliases().values())


def menu():
    # 初始化頁面列表
    # 如果session中沒有pages_list，則從pages目錄讀取所有頁面
    # 並為每個頁面添加隨機表情符號
    if "pages_list" not in st.session_state:
        pages_list = os.listdir("pages")
        page_names = ["首頁"]  # 將首頁作為第一個選項
        for page in pages_list:
            page_names.append(page.split(".")[0])

        # 為每個頁面名稱加上隨機表情符號
        # 這樣可以讓選單更生動有趣
        st.session_state.pages_list = []
        for name in page_names:
            st.session_state.pages_list.append(f"{name} {random.choice(emojis)}")

    # 初始化當前頁面
    # 如果沒有選擇頁面，預設顯示首頁
    if "current_page" not in st.session_state:
        st.session_state.current_page = st.session_state.pages_list[0]

    # 在側邊欄創建導航菜單
    # 首頁永遠顯示在最上方，並使用房子圖標
    st.sidebar.page_link(page="main.py", label="首頁", icon="🏠")
    st.sidebar.markdown("---")  # 分隔線

    # 創建課程選單
    # 使用下拉選單讓用戶選擇要訪問的頁面
    st.sidebar.title("課程")
    selected_page_with_emoji = st.sidebar.selectbox(
        "選擇頁面：",
        st.session_state.pages_list,
        index=st.session_state.pages_list.index(st.session_state.current_page),
    )
    # 從帶有表情符號的頁面名稱中提取實際的頁面名稱
    selected_page = selected_page_with_emoji.split(" ")[0]

    # 處理頁面切換
    # 當用戶點擊傳送按鈕時，根據選擇切換到相應頁面
    if st.sidebar.button("傳送"):
        st.session_state.current_page = selected_page_with_emoji
        if selected_page == "首頁":
            st.switch_page("main.py")
        else:
            st.switch_page(f"pages/{selected_page}.py")
