# _*_ coding: utf-8 _*_
# 程式 12-2 (Python 2 Version)

import facebook

token = 'CAACEdEose0cBADXaSgOx9nIezMshtC90oP2T4g3B5cRmBy4mBjnXccxEFzclIK1b9FzMSIJCX4sATcwqe5KhArKz4FYVOIbPo8WBpNujABZBCftZAMqnYthZCRoQVTWXSDpoELE4qW2h7twozPxUVKZBIo1lNADP9xtokGCPpOTIvZBXTe2B058fWlr9yQCEjSzF8viOHJ2DDWiYBZAxZBF'

g = facebook.GraphAPI(access_token=token)

posts = g.get_connections(id='me', connection_name='posts')

posts = posts['data']

for p in posts:

	if 'likes' in p and 'message' in p:
		print '\n', p['created_time'], '的'
		print '訊息：', p['message']
		likes = p['likes']['data']
		print '共有', len(likes), '人按讚，分別是：'
		for like in likes:
			print like['name'], 
		print '\n------------------------'
