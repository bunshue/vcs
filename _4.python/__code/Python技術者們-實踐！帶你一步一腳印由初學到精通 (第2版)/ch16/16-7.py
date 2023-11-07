import requests

base = 'https://japanwest.api.cognitive.microsoft.com/face/v1.0'    # api
key = '您的金鑰'                                # 你的 key
headers = {'Ocp-Apim-Subscription-Key': key}                            # 請求標頭


def person_list(gid):
    pson_url = base + f'/persongroups/{gid}/persons'    # 查看群組人員的請求路徑
    response = requests.get(pson_url,          # HTTP GET
                            headers=headers)
    if response.status_code == 200:
        print('查詢人員完成')
        return response.json()
    else:
        print("查詢人員失敗:", response.json())         # 印出創建失敗原因


#------------------------------------#
persons = person_list('gp01')   # 查詢群組 gp01 的成員清單
print(persons)
