# ch14_9.py
import requests, bs4, json

def printing():                         # 列印熱門貼文
    global counter
    for post in posts:
        try:
            counter += 1
            print('貼文熱門編號 : ', counter)     
            print("id           : ", post['id'])
            print("標題         : ", post['title'])
            print("內文         : ", post['excerpt'])
            print("按讚         : ", post['likeCount'])
            print("回應         : ", post['commentCount'])
        except UnicodeEncodeError:
            print("UnicodeEncodeError")            
            
url = 'https://www.dcard.tw/'
api = '_api/posts?popular=true'
url_popular = url + api
posts = list(requests.get(url_popular).json())
counter = 0
printing()                              # 印第1組前30熱門
last_id = posts[-1]['id']               # 第1組最後一筆熱門id
num_page = 2
for i in range(num_page):               # 印第2-3組前30熱門
    posts = list(requests.get(url_popular+'&before='+str(last_id)).json())
    printing()
    last_id = posts[-1]['id']           # 最後一筆熱門的id





    










