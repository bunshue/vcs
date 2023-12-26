# ch21_9.py
import json

fn = 'login.json'
with open(fn, 'r') as fnObj:
    login = json.load(fnObj)
    print(f"{login}! 歡迎回來使用本系統! ")


