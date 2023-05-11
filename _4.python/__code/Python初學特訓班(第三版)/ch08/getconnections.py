import facebook

token="EAADAqsBw2wsBANvemU2wZAtWJmGQS9blphxQEkTw9lAP8kdPe1vpurAsN7SgVnxjEWeSBQ1WI0ZBZBxhpyWIFauFNm2ZAZAFE3WAGhrQQYwFuaMGbVyWuzPJZCREZBSrf4STZBgXqxSZAFgFim3kZCOb3Fc3XITCs9b2FBYouJNOtPvTHo7yZCOHbg35IYB0jZC8jW0ZD"
graph = facebook.GraphAPI(access_token=token,version='3.0')

pages = graph.get_connections(id='me', connection_name='posts')

posts = pages['data']
#print(posts)

for p in posts:
    if 'message' in p:
        print('訊息：{}'.format(p['message']))
        print('貼文日期：{}'.format(p['created_time']))
        print()