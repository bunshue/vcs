# 7-5-3 dict 合併: 使用多重解包 (Python 3.5+)

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

new_setting = {**default, **user1}

print(new_setting)

