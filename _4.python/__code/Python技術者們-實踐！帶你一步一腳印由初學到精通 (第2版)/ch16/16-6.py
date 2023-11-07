import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    # api
pson_url = f'{base}/persongroups/gp01/persons'   # 新增人員的請求路徑
key = '您的金鑰'                                # 你的 key
headers_json = {'Ocp-Apim-Subscription-Key': key,                       # 請求標頭
                'Content-Type': 'application/json'}
body = {'name': '周詠',                      # 建立請求主體內容
        'userData': '苗栗人'}
body = str(body).encode('utf-8')             # 請求主體的編碼

response = requests.post(pson_url,          # HTTP POST
                         headers=headers_json,
                         data=body)
if response.status_code == 200:
    print('新增人員完成: ', response.json())
else:
    print("新增失敗:", response.json())         # 印出創建失敗原因
