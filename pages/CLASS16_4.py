import streamlit as st
from utils import init_page

init_page()
st.title("轉發功能")

# 不會幫使用者開新分頁
# 內部轉發
# if st.button("一般按鈕+switch_page=轉發到課程 16_3"):
#     st.switch_page("pages/CLASS16_3.py")

# 如果你想要使用 link_button，轉發到自己網站的分頁時，不可以有.py的字串
# 而且會幫使用者開新分頁
# st.link_button("link_button=轉發到課程 16_3", "CLASS16_3")

# 內部轉發與外部轉發的差異
# 內部轉發: 不會幫使用者開新分頁，網頁不用重新載入，只載入變動的部分，cookie 會保留
# 外部轉發: 會幫使用者開新分頁，網頁會重新載入，cookie 會重新產生
