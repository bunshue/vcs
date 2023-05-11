import requests,json

url="https://graph.facebook.com/v3.2/me/posts?fields=message%2Ccreated_time&until=2016-09-01&since=2016-01-01&access_token=EAADAqsBw2wsBAL9vAlc8YZBZBpIClS2c0xBs0CdCOK1wZBW8lZCISy2CY2qUyG6waEYTNQhSZB45zb5ky8B9mk4SdZC8qZBUUdHmJnpB1q7owbmOt0mIC0SGhAHBFEZBZAMqRvvTFfJcWSvkKjXiP3l9qZCrlPyadqO6JUYDpsTmEtPR59CtR9upr0HdHesJIEMLlCNg0xP5c04AZDZD"
data = json.loads(requests.get(url).text) # 讀取資料並轉成 json 

for d in data['data']: # 讀取 Key 名稱為 data 的定典資料 
    if 'message' in d: # 確認 message 存在
        print("message:{}".format(d['message']))
        print("created_time:{}".format(d['created_time']))
        print("id:{}".format(d['id']))
        print()