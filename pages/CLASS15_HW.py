import streamlit as st
import requests
import os
import dotenv

dotenv.load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

############################定義常數############################
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
UNITS = "metric"
LANG = "zh_tw"

############################主程式############################
st.title("天氣查詢")
city_name = st.text_input("請輸入城市名稱")
send_Url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"

response = requests.get(send_Url)
info = response.json()
if "main" in info:
    city = info["name"]
    temp = info["main"]["temp"]
    description = info["weather"][0]["description"]
    icon_code = info["weather"][0]["icon"]

    icon_url = f"{ICON_BASE_URL}{icon_code}.png"
    icon_response = requests.get(icon_url)
    if icon_response.status_code == 200:
        icon_image = icon_response.content
        image_path = f"images/weather_icon.png"
        with open(image_path, "wb") as f:
            # with 開啟檔案可以在程式結束後自動關閉檔案，as f 則是將檔案開啟後存到變數中
            # wb 是寫入模式，可以寫入二進位檔案，也可以寫入文字檔案
            f.write(icon_image)  # 寫入檔案
        st.success("圖片下載成功")
    else:
        st.warning("圖片下載失敗")

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"城市：{city}")
        st.write(f"溫度：{temp}℃")
        st.write(f"描述：{description}")
    with col2:
        if os.path.exists(image_path):
            size = st.number_input("請輸入圖片大小", value=100, step=10, key="size")
            st.image(image_path, width=size)
        else:
            st.warning("圖片不存在")

else:
    st.warning("查詢失敗")
