import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 設定為寬版佈局
st.set_page_config(page_title="大虎尾地圖", layout="wide")

st.title('大虎尾地圖')

# 2. 建立 Folium 地圖
map_center = [23.706415, 120.427451]
m = folium.Map(location=map_center, zoom_start=13)

# 3. 加圖釘（示範）
pins = [
    {"lat": 23.7097, "lng": 120.4432, "title": "虎尾鎮圖釘", "description": "這是一個圖釘", "image_url": "https://..."}
]
for pin in pins:
    folium.Marker(
        location=[pin["lat"], pin["lng"]],
        popup=folium.Popup(
            f'<b>{pin["title"]}</b><br>'
            f'{pin["description"]}<br>'
            f'<img src="{pin["image_url"]}" width="200" />',
            max_width=300
        )
    ).add_to(m)

# 4. 顯示地圖，滿版寬度 + 自訂高度
st_folium(m, use_container_width=True, height=800)
