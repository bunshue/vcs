# 7-5-2 dict 合併: 使用 dict() 與 **

default = {
    'user': 'guest',
    'lang': 'Python',
    'version': 3.7
    }

user1 = {
    'user': 'user 1',
    'version': 3.8,
    'platform': 'linux'
    }

new_setting = dict(default, **user1)

print(new_setting)
