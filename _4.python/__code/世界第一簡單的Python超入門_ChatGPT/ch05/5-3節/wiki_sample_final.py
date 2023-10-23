import requests

# 郵遞區號
zipcode = "1000001"

# API 端點
api_endpoint = f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}"

# 進行查詢
response = requests.get(api_endpoint)

# 檢查回應狀態
if response.status_code == 200:
    # 解析回應內容
    data = response.json()

    # 驗證 API 回應狀態
    if data['status'] == 200:
        # 取出第一筆地址資訊
        address_info = data['results'][0]

        # 印出完整郵遞區域
        print(f"{address_info['address1']} {address_info['address2']} {address_info['address3']}")
    else:
        print("API 回應錯誤，訊息：", data['message'])
else:
    print("API 查詢失敗，狀態碼：", response.status_code)
