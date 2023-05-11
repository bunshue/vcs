import facebook,random
token="EAADAqsBw2wsBAMNJ8lD9fLyBoffOriCnnmy8spPnJSYMU88YMh3HY1DaIUdm9HQZASBvPuCY5ZBHJrMnjGHaufLu73Fd1Vlf9uWud54mnTRS2ZCZCyKavt06xthCniuYtZBbXkloWwbRgKwRPzNoyZCJDkB8amCudmuRbMCFrxCFmrJC73MTXxZArMUJsm5R9upkB8KzLCTWwZDZD"
graph = facebook.GraphAPI(access_token=token,version='3.0')
object_id='105081412905972_1963934413687320'

# 按讚
likeslist=[]
post = graph.get_object(id=object_id + '?fields=likes.limit(1000)')
#print(post)

try:
    likes = post['likes']['data']
    #print(likes)
    print('共有', len(likes), '人按讚:')
    for like in likes:
        print (like['name'],end="、")
        likeslist.append(like['name'])
         
    #抽獎  
    no = random.randint(0,len(likeslist)-1)
    print("\n\n恭喜 {}XX，得到 iPhone7 Plus 壹台!".format(likeslist[no][0:1]))
except:
    print("此篇文章沒有人按讚!")