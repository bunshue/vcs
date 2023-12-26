# ch32_8.py
import facebook

token = "EAAIZCihE7RSkBABhXYIw4tJiBWtBZCzSgxws8kH0Ia0nmXJQLIosh3F5JZBtZCgb1Y7IbtSJW40Lzy5awL7ZAgZBmrzFgxJkQjZCqdm0FCrinwZCh1F6mwZCNCdx0DXnKDlrw7HHs2O0QjosayoTvx1zrQu1VihimzZAmWgQZC6mZB1ojn98GEL9xtNdFOxLOwJ8D6KYFQn5ZA6hhlQZDZD"
graph = facebook.GraphAPI(access_token=token,version='3.1')
idsList = '1116138285252667_1113470975519398?fields=likes.summary(true)'
mylikes = graph.get_object(id=idsList)

# 這篇貼文必須本人有按讚
likes = mylikes['likes']['data']
for like in likes:
    print("按讚人 : ", like['name'])   

num = mylikes['likes']['summary']
print("按讚總人數 : ", num['total_count'])
















