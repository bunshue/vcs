# ch21_5.py
import json

jsonObj = '{"b":80, "a":25, "c":60}'    # json物件
dictObj = json.loads(jsonObj)           # 轉成Python物件
print(dictObj)
print(type(dictObj))






