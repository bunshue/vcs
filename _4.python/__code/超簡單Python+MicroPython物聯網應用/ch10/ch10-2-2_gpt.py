# main.py
from xtools import connect_wifi_led
import urequests

# 連接WiFi
connect_wifi_led()

# 取得JSON資料
url = "https://fchart.github.io/json/Example3.json"
response = urequests.get(url)
json_data = response.json()
response.close()

# 顯示JSON資料
print(json_data)
