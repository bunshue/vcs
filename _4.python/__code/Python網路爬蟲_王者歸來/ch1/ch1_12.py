# ch1_12.py
import json

fn = 'login.json'
with open(fn, 'r') as fnObj:
    login = json.load(fnObj)
    print("%s! 歡迎回來使用本系統! " % login)

