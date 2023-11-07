import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    # api
gp_url = base + '/persongroups/gp01'                                    # 創建群組的請求路徑
key = '您的金鑰'                                # 你的 key
headers = {'Ocp-Apim-Subscription-Key': key}   # 請求標頭
response = requests.get(gp_url,
                        headers=headers)       # HTTP GET
if response.status_code == 200:
    print(response.json())
else:
    print("查詢失敗", response.json())
