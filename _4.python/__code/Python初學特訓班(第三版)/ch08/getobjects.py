import facebook
token="EAADAqsBw2wsBANvemU2wZAtWJmGQS9blphxQEkTw9lAP8kdPe1vpurAsN7SgVnxjEWeSBQ1WI0ZBZBxhpyWIFauFNm2ZAZAFE3WAGhrQQYwFuaMGbVyWuzPJZCREZBSrf4STZBgXqxSZAFgFim3kZCOb3Fc3XITCs9b2FBYouJNOtPvTHo7yZCOHbg35IYB0jZC8jW0ZD"
graph = facebook.GraphAPI(access_token=token,version='3.0')

post_ids = ['100002286941783_1160478487371705','100002286941783_1020234718062750']
posts = graph.get_objects(ids=post_ids)
for post_id in post_ids:
    p=posts[post_id]  # 讀取每篇貼文
    print(p["id"])
    print(p["message"])
    print()