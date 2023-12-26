# ch15_36.py
import requests

try:
    # 嘗試發出網絡請求
    response = requests.get('http://example.com')
    # 如果請求返回了錯誤響應, 會引發 HTTPError
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    # 處理 HTTP 錯誤
    print(f"HTTP Error: {e}")
except requests.exceptions.ConnectionError as e:
    # 處理連接錯誤
    print(f"Connection Error: {e}")
except requests.exceptions.Timeout as e:
    # 處理請求超時錯誤
    print(f"Timeout Error: {e}")


