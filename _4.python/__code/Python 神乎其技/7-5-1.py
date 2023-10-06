# 7-5-1 dict 合併: 使用 update

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

default.update(user1)

print(default)