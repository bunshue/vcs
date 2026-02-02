# ch14_7.py
import requests, bs4, json

url = 'https://www.dcard.tw/'
api = '_api/posts?popular=true'
url_popular = url + api
posts = list(requests.get(url_popular).json())
try:
    print("id   : ", posts[0]['id'])
    print("標題 : ", posts[0]['title'])
    print("內文 : ", posts[0]['excerpt'])
    print("按讚 : ", posts[0]['likeCount'])
    print("回應 : ", posts[0]['commentCount'])
except UnicodeEncodeError:
    print("UnicodeEncodeError")  



    










