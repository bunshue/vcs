'''
import requests

r=requests.get("http://www.e-happy.com.tw")
r.encoding='utf-8'
print("下載完畢!")
if (r.status_code==200):
    print(1111)
    print(r.text)
    print(r.raw.read(100))
'''


import os

print(__file__)

print(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

DIRS = os.path.join(BASE_DIR, 'templates')
NAME = os.path.join(BASE_DIR, 'db.sqlite3')
AAAA = os.path.join(BASE_DIR, 'static')

print(DIRS)
print(NAME)
print(AAAA)

username = 'david'
password = '1234'
if username=='david' and password=='1234':
    print('歡迎光臨本網站！')
else:
    print('帳號或密碼錯誤！')



import sys
print(sys.version_info)
print(sys.version_info[0])
if sys.version_info[0] >= 3:
    print('python 新版')
else:
    print('python 舊版')
    
if sys.version < '3':
    print('python 舊版')
else:
    print('python 新版')

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/human2.jpg'

name = filename.split('/')
print(len(name))
print(name)
print(type(name))

ccc = name.reverse()
print(ccc)




