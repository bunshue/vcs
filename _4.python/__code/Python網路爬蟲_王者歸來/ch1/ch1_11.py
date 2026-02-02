# ch1_11.py
import json

fn = 'login.json'
login = input("請輸入帳號 : ")
with open(fn, 'w') as fnObj:
    json.dump(login, fnObj)
    print("%s! 歡迎使用本系統! " % login)

