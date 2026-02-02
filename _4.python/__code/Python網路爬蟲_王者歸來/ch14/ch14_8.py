# ch14_8.py
import requests, bs4, json

url = 'https://www.dcard.tw/'
api = '_api/posts?popular=true'
url_popular = url + api
posts = list(requests.get(url_popular).json())
print(len(posts))
for post in posts:
    try:
        print("id   : ", post['id'])
        print("標題 : ", post['title'])
        print("內文 : ", post['excerpt'])
        print("按讚 : ", post['likeCount'])
        print("回應 : ", post['commentCount'])
    except UnicodeEncodeError:
        print("UnicodeEncodeError")  



    










