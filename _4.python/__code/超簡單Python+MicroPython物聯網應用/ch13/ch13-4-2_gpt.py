# 匯入所需模組
import urequests as requests
import ujson as json
from xtools import connect_wifi_led

# 定義Firebase資料庫URL和鍵路徑
firebase_url = 'https://iot-distance-?????-default-rtdb.firebaseio.com/'
key_path = 'Team-IOT/Members/M3.json'

# 連接WiFi
connect_wifi_led()

# 從Firebase讀取資料的函式
def read_firebase_data():
    try:
        # 發送HTTP GET請求
        response = requests.get(firebase_url + key_path)
        
        # 檢查請求是否成功
        if response.status_code == 200:
            # 解析JSON資料
            data = response.json()
            return data
        else:
            print('Failed to get data. Status code:', response.status_code)
            return None
    except Exception as e:
        print('Error reading data from Firebase:', e)
        return None

# 這裡不需要主程式，只定義了所需的函式和步驟
print(read_firebase_data())