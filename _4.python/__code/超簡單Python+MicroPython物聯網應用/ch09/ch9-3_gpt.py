import network
import urequests
from ch9_1_gpt import connect_wifi, SSID, PASSWORD

# 連接到WiFi
connect_wifi(SSID, PASSWORD)

# 定義要訪問的URL
url = "https://fchart.github.io/json/Example.json"

# 發送GET請求並獲取JSON數據
response = urequests.get(url)
data = response.json()

# 顯示獲取到的JSON數據
print(data)

# 關閉HTTP連接
response.close()
