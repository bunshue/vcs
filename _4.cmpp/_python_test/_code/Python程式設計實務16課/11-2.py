# _*_ coding: utf-8 _*_
# 程式 11-2 (Python 3 version)

from firebase import firebase

db_url = 'https://python01.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)
users = fdb.get('/user', None)
print("資料庫中找到以下的使用者")
for key in users:
    print(users[key]['name'])
