# ch32_2.py
import requests
import json

url = "https://graph.facebook.com/v3.3/me/posts?limit=2&access_token=EAAIZCihE7RSkBAJ3fRRbKyOc7dDa17GkCN2YTH6AS2KJ1yjU8AY4czB5oaXk9CBpPCmtmJ9ZCPCjrILe6TfT4eDkcLoPyyZArHzyIrZAYQmd6mrZCOItIRL65fboQpLjl7vFLPrUuTZAVpp7UwwkEkKShDoHjQ0BFUsVOL8m1lLJKDA2IF6pI0eDPYrfdyOIEvezXLZCRj6fgZDZD"

data = json.loads(requests.get(url).text)   # 下載json資料轉成字典

for info in data['data']:
    print("我的Facebook發文")    
    print("發文日期", info['created_time'])
    print("發文內容", info['message'])
    print("發文的id", info['id'])
    print()











