# ch32_4.py
import facebook

token = "EAAIZCihE7RSkBAKnGeo0AKdvoZB5n64xpQs2nJNxSywAMf5s7JDX6ADKvBBZABLeMrNKtAsaKBOmMmg2yDEaoXZA9pnFPC2OWQVoe7TLPFAFmJhS9sfpZCVq1UWIjmZAJS3YtMGBqomWScofJEhC5ulZCMIYoZC6as29rP86WHA4WMzB7DKuq5wLa6KxzrzDBbXeZA0SMZBwWxkwZDZD"
graph = facebook.GraphAPI(access_token=token, version='3.1')

idsList = ['1116138285252667_1113470975519398',
           '1116138285252667_1112637295602766']           
mypost = graph.get_objects(ids=idsList)

for ids in idsList:
    post = mypost[ids]                  # 取得特定id發文物件
    print("列出發文資料內容 : ", post)
    print("發文日期 : ", post['created_time'])
    print("發文內容 : ", post['message'])
    print("發文的id : ", post['id'])
    print()


















