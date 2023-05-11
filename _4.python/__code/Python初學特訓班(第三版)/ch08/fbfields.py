import facebook
token="EAADAqsBw2wsBACCQX740hgH0dZBZAdWVZArkUkPhe1YZCuWpblnvdsam8uLlLcWTjprZBVuH48WEARHLBZCDYHvDaejjsfyJ83Hc7jWQxkkZBmEiH4IENME7jCKtShClZBkNOCWi5yGHWyDYSu9ze7kJ7ynrmPfDcZCx9iGjQ0qwIRItvgv5TB2Qeg3nL0ZAwRxybGrwLPup4qRAZDZD"
graph = facebook.GraphAPI(access_token=token,version='3.0')

post = graph.get_object(id='100002286941783_1160478487371705')
#print(post)
print('訊息：{}'.format(post['message']))
#
#
post = graph.get_object(id='100002286941783_1126322320787322?fields=likes')
#print(post)

likes = post['likes']['data']
print('共有', len(likes), '人按讚，：按讚者：')
for like in likes:
    print (like['name'],end="、")
print()

post = graph.get_object(id='100002286941783_1126322320787322?fields=comments')
comments = post['comments']['data']
print('共有', len(comments), '留言，：留言者：')
for comment in comments:
     print ("{}:{}".format(comment['from']['name'], comment['message']))
