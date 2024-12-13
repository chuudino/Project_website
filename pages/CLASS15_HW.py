import gzip
import json
import streamlit as st
import requests
import os
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import dotenv


# 讀取城市列表
def load_city_list(file_path):
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        return json.load(f)


dotenv.load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

############################定義常數############################
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
UNITS = "metric"
LANG = "zh_tw"
forecast_URL = "https://api.openweathermap.org/data/2.5/forecast?"

############################主程式############################
st.title("天氣查詢")

# city_name = st.text_input("請輸入城市名稱")
# 載入城市列表
city_list = load_city_list("current.city.list.json.gz")

city_dict = {f"{city['name']}, {city['country']}": city["id"] for city in city_list}
# for city in city_list:
#     city_name = f"{city['name']}, {city['country']}"
#     city_id = city["id"]
# 建立下拉選單
city_name = st.selectbox("選擇城市", list(city_dict.keys()))
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
        # st.success("圖片下載成功")
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

st.write("---")
st.title("氣溫預測圖")
send_Url = f"{forecast_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
# st.write(send_Url)
response = requests.get(send_Url)
info = response.json()
xlist = []
ylist = []
if "list" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        time = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime(
            "%m/%d %H"
        )
        xlist.append(time)
        ylist.append(temp)
        weather_description = forecast["weather"][0]["description"]
        # st.write(f" {dt_txt}\n溫度: {temp}℃\n天氣狀況: {weather_description}")

    ############################繪製圖表############################
    font = FontProperties(fname="LXGWWenKaiTC-Regular.ttf", size=20)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(xlist, ylist)
    ax.set_xlabel("時間", fontproperties=font)
    ax.set_ylabel("溫度", fontproperties=font)
    ax.set_title("天氣預報", fontproperties=font)
    plt.xticks(rotation=45)
    plt.tight_layout()  # 調整圖片的大小
    plt.savefig("images/forecast.png")
    st.image("images/forecast.png")
else:
    st.warning("找不到該城市或無法獲取天氣資訊")
