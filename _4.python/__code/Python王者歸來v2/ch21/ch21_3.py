# ch21_3.py
import json

dictObj = {'b':80, 'a':25, 'c':60}                  # 字典
jsonObj1 = json.dumps(dictObj)                      # 為排序將字典轉成json物件
jsonObj2 = json.dumps(dictObj, sort_keys=True)      # 有排序將字典轉成json物件
print("未用排序將字典轉換成json的物件", jsonObj1)
print("使用排序將字典轉換成json的物件", jsonObj2)
print("有排序與未排序物件是否相同    ", jsonObj1 == jsonObj2 )
print("json物件在Python的資料類型 ", type(jsonObj1))


