# ch21_10.py
import json

fn = 'login21_10.json'
try:
    with open(fn) as fnObj:
        login = json.load(fnObj)   
except Exception:
    login = input("請輸入帳號 : ") 
    with open(fn, 'w') as fnObj:
        json.dump(login, fnObj)
        print("系統已經記錄你的帳號 ")
else:
    print(f"{login} 歡迎回來")

