# ch32_5.py
import facebook

token = "EAAIZCihE7RSkBAKnGeo0AKdvoZB5n64xpQs2nJNxSywAMf5s7JDX6ADKvBBZABLeMrNKtAsaKBOmMmg2yDEaoXZA9pnFPC2OWQVoe7TLPFAFmJhS9sfpZCVq1UWIjmZAJS3YtMGBqomWScofJEhC5ulZCMIYoZC6as29rP86WHA4WMzB7DKuq5wLa6KxzrzDBbXeZA0SMZBwWxkwZDZD"
graph = facebook.GraphAPI(access_token=token, version='3.1')

mypost = graph.get_object(id='1116138285252667_1113470975519398?fields=message')
print("列出發文資料內容 : ", mypost)
print("發文內容 : ", mypost['message'])














