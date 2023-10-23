import requests

# 郵遞區號
zipcode = "100-0001"

# API 端點
api_endpoint = "http://your_api_endpoint"

# 你的 API 金鑰
api_key = "your_api_key"

# 設定查詢參數
params = {
    'apikey': api_key,
    'zipcode': zipcode,
}

# 進行查詢
response = requests.get(api_endpoint, params=params)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 印出郵遞區域
    print(data['area'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)
