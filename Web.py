import streamlit as st
import folium
from streamlit_folium import st_folium

# 設定地圖的中心點
map_center = [23.706415, 120.427451]  # 雲林縣虎尾鎮立仁國小

# 創建一個 Folium 地圖
m = folium.Map(location=map_center, zoom_start=13)

# 添加圖釘資料
pins = [
    {"lat": 23.7097, "lng": 120.4432, "title": "虎尾鎮圖釘", "description": "這是一個圖釘", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCpM8B3LKtV4p7d_n3PyGvao5rPfUucqN_0A&s"}
]

# 在地圖上添加圖釘
for pin in pins:
    folium.Marker(
        location=[pin["lat"], pin["lng"]],
        popup=folium.Popup(f'<b>{pin["title"]}</b><br>{pin["description"]}<br><img src="{pin["image_url"]}" width="200" />', max_width=300)
    ).add_to(m)

# 使用 Streamlit 顯示地圖
st.title('我的地圖')
st_folium(m, width=700)
