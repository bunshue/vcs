# _*_ coding: utf-8 _*_
# 程式 11-1 (Python 3 version)

from firebase import firebase
import time

new_users = [
{'name': 'Richard Ho'},
{'name': 'Tom Wu'},
{'name': 'Judy Chen'},
{'name': 'Lisa Chang'}
]

db_url = 'https://python01.firebaseio.com'
fdb = firebase.FirebaseApplication(db_url, None)
for user in new_users:
    fdb.post('/user', user)
    time.sleep(3)
