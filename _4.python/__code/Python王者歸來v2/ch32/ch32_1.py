# ch32_1.py
import requests
import json

url = "https://graph.facebook.com/v3.3/me/posts?limit=2&access_token=EAAIZCihE7RSkBAJ3fRRbKyOc7dDa17GkCN2YTH6AS2KJ1yjU8AY4czB5oaXk9CBpPCmtmJ9ZCPCjrILe6TfT4eDkcLoPyyZArHzyIrZAYQmd6mrZCOItIRL65fboQpLjl7vFLPrUuTZAVpp7UwwkEkKShDoHjQ0BFUsVOL8m1lLJKDA2IF6pI0eDPYrfdyOIEvezXLZCRj6fgZDZD"

data = json.loads(requests.get(url).text)   # 下載json資料轉成字典
print(data)








