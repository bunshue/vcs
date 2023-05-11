import facebook
token="EAADAqsBw2wsBANvemU2wZAtWJmGQS9blphxQEkTw9lAP8kdPe1vpurAsN7SgVnxjEWeSBQ1WI0ZBZBxhpyWIFauFNm2ZAZAFE3WAGhrQQYwFuaMGbVyWuzPJZCREZBSrf4STZBgXqxSZAFgFim3kZCOb3Fc3XITCs9b2FBYouJNOtPvTHo7yZCOHbg35IYB0jZC8jW0ZD"
graph = facebook.GraphAPI(access_token=token,version='3.0')

post = graph.get_object(id='100002286941783_1020234718062750')
print(post["id"])
if 'message' in post:
    print(post["message"])
else:
    print("缺少 message 欄位")    