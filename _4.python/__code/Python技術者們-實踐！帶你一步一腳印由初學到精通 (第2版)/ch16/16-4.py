import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    # api
gp_url = base + '/persongroups/gp01'                                    # 創建群組的請求路徑
key = '您的金鑰'                                # 你的 key
headers_json = {'Ocp-Apim-Subscription-Key': key,       # 請求標頭
                'Content-Type': 'application/json'}
body = {'name': '旗標科技公司',      # 建立請求主體內容
        'userData': '位於台北市'}
body = str(body).encode('utf-8')        # 請求主體的編碼

response = requests.put(gp_url,                 # HTTP PUT
                        headers=headers_json,
                        data=body)
if response.status_code == 200:     # 請求成功返回狀態碼 200
    print("創建群組成功")
else:
    print("創建失敗:", response.json())         # 印出創建失敗原因
