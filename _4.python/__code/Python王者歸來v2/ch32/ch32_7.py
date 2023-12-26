# ch32_7.py
import facebook

token = "EAAIZCihE7RSkBABhXYIw4tJiBWtBZCzSgxws8kH0Ia0nmXJQLIosh3F5JZBtZCgb1Y7IbtSJW40Lzy5awL7ZAgZBmrzFgxJkQjZCqdm0FCrinwZCh1F6mwZCNCdx0DXnKDlrw7HHs2O0QjosayoTvx1zrQu1VihimzZAmWgQZC6mZB1ojn98GEL9xtNdFOxLOwJ8D6KYFQn5ZA6hhlQZDZD"
graph = facebook.GraphAPI(access_token=token,version='3.1')
friends = graph.get_connections(id='me',connection_name='friends')

print(friends)
print("我的臉書朋友總數 : ", friends['summary']['total_count'])















