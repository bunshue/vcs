import os
import sys
import time
import random


print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
del fruits['西瓜']
print("新fruits字典內容:", fruits)
   

print("------------------------------------------------------------")  # 60個

fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25}
print("舊fruits字典內容:", fruits)
fruits.clear( )
print("新fruits字典內容:", fruits)
 

print("------------------------------------------------------------")  # 60個

soldier0 = {}           # 建立空字典
print("空小兵字典", soldier0)
soldier0['tag'] = 'red'
soldier0['score'] = 3
print("新小兵字典", soldier0)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_13.py

# ch9_13.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
cfruits = fruits.copy( )
print("位址 = ", id(fruits), "  fruits元素 = ", fruits)
print("位址 = ", id(cfruits), "  fruits元素 = ", cfruits)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_14.py

# ch9_14.py
fruits = {'西瓜':15, '香蕉':20, '水蜜桃':25, '蘋果':18}
noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60}
empty_dict = {}
print("fruits字典元素數量     = ", len(fruits))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))

print("------------------------------------------------------------")  # 60個

players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
print("Stephen Curry是 %s 的球員" % players['Stephen Curry'])
print("Kevin Durant是 %s 的球員" % players['Kevin Durant'])
print("Paul Gasol是 %s 的球員" % players['Paul Gasol']) 

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_17.py

# ch9_17.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name, team in players.items( ):
    print("\n姓名: ", name)
    print("隊名: ", team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_18.py

# ch9_18.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in players.keys( ):
    print("姓名: ", name)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_19.py

# ch9_19.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in players:
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_20.py

# ch9_20.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for name in sorted(players.keys( )):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_21.py

# ch9_21.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in players.values( ):
    print(team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_21_1.py

# ch9_21_1.py
players = {'Stephen Curry':'Golden State Warriors',
           'Kevin Durant':'Golden State Warriors',
           'Lebron James':'Cleveland Cavaliers',
           'James Harden':'Houston Rockets',
           'Paul Gasol':'San Antonio Spurs'}
for team in set(players.values( )):
    print(team)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_22.py

# ch9_22.py
soldier0 = {'tag':'red', 'score':3, 'speed':'slow'}         # 建立小兵
soldier1 = {'tag':'blue', 'score':5, 'speed':'medium'}
soldier2 = {'tag':'green', 'score':10, 'speed':'fast'}
armys = [soldier0, soldier1, soldier2]                      # 小兵組成串列
for army in armys:                                          # 列印小兵
    print(army)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_23.py

# ch9_23.py
armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print("小兵數量 = ", len(armys))

print("------------------------------------------------------------")  # 60個

armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'blue'
        soldier['score'] = 5
        soldier['speed'] = 'medium'
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

print("------------------------------------------------------------")  # 60個

# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items( ):
          print("%s 喜歡的運動是: " % name)
# 列印value,這是串列
          for sport in favorite_sport:
              print("   ", sport)

print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印內含字典的字典
for account, account_info in wechat_account.items( ):
    print("使用者帳號 = ", account)                   # 列印鍵(key)
    name = account_info['last_name'] + " " + account_info['first_name']
    print("姓名       = ", name)                      # 列印值(value)
    print("城市       = ", account_info['city'])      # 列印值(value)


print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}}
# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account['cshung']))
print("wechat_account['kevin']元素個數  ", len(wechat_account['kevin']))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python零基礎最強入門之路-王者歸來\ch9\ch9_29.py

# ch9_29.py
# 將串列轉成字典
seq1 = ['name', 'city']         # 定義串列
list_dict1 = dict.fromkeys(seq1)
print("字典1 ", list_dict1)
list_dict2 = dict.fromkeys(seq1, 'Chicago')
print("字典2 ", list_dict2)
# 將元組轉成字典
seq2 = ['name', 'city']         # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print("字典3 ", tup_dict1)
tup_dict2 = dict.fromkeys(seq2, 'New York')
print("字典4 ", tup_dict2)

print("------------------------------------------------------------")  # 60個

fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)
ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)
ret_value3 = fruits.get('Grape', 10)
print("Value = ", ret_value3)

print("------------------------------------------------------------")  # 60個

