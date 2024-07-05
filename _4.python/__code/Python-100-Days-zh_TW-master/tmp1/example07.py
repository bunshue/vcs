

#登錄微信

import itchat

itchat.auto_login()


#查找自己的朋友

friends_list = itchat.get_friends(update=True)
print(len(friends_list))
luohao = friends_list[0]
props = ['NickName', 'Signature', 'Sex']
for prop in props:
    print(luohao[prop])

