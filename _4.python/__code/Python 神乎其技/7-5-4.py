# 7-5-4 dict 合併: 使用聯集算符 (注意: 限 Python 3.9+)

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

new_setting = default | user1

print(new_setting)

default |= user1

print(default)