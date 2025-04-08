import folium
import os

# 建立地圖，中心點設在台北市
m = folium.Map(location=[25.0330, 121.5654], zoom_start=12)

# 指定儲存路徑和檔案名稱
folder_path = r"C:\Users\User\Desktop\python_vscode\GraduationProject" # 注意：Windows 路徑使用原始字串
filename = "basic_map.html"
file_path = os.path.join(folder_path, filename)

# 確保資料夾存在，如果不存在則建立
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 儲存成 HTML
m.save(file_path)

print(f"地圖已儲存至：{file_path}")