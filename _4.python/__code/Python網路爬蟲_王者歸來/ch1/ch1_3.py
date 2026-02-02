# ch1_3.py
import json

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs',
          }
jsonObj1 = json.dumps(players)                      # 未用排序將字典轉成json物件
jsonObj2 = json.dumps(players, sort_keys=True)      # 有用排序將字典轉成json物件
print("未用排序將字典轉換成json的物件", jsonObj1)
print("使用排序將字典轉換成json的物件", jsonObj2)
print("有排序與未排序物件是否相同    ", jsonObj1 == jsonObj2 )
print("json物件在Python的資料類型 ", type(jsonObj1))


