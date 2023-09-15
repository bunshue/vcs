import os
import sys
import time
import random

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

msg = '''
翠蓋龍旗出建章,鶯啼百囀柳初黃,
昆池冰泮三山近,阿閣花深九陌香,
徑轉虹梁通紫極,庭含玉樹隱霓裳,
侍臣緩步隨鑾輅,岡上應看集鳳皇,
小苑平臨太液池,金舖約戶鎖蟠螭,
雲中帝座飛華蓋,城上鈞陳繞翠旗,
紫氣旋面雙鳳閣,青松還有萬年枝,
從來清蹕深嚴地,開盡碧桃人未知
'''

print(f"<鳳>出現的次數 : {msg.count('鳳')}")

'''
msg = msg.replace('Linda','Lxx')
print(f"新的msg內容 : {msg}")
'''

print('------------------------------------------------------------')	#60個

x = [[a, b, c] for a in range(1,20) for b in range(a,20) for c in range(b,20)
     if a ** 2 + b ** 2 == c **2]
print(x)


print('------------------------------------------------------------')	#60個


for x in range(0x2160, 0x216a):
  print(chr(x),end=' ')

print()
  
print('------------------------------------------------------------')	#60個


x = 1000000
pi = 0
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i % 100000 == 0:      # 隔100000執行一次
        print(f"當 {i = :7d} 時 PI = {pi:20.19f}")

print('------------------------------------------------------------')	#60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)     # 執行zip
print(type(zipData))            # 列印zip資料類型
player = list(zipData)          # 將zip資料轉成串列
print(player)

print('------------------------------------------------------------')	#60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30']
zipData = zip(fields, info)   # 執行zip
print(type(zipData))          # 列印zip資料類型
player = list(zipData)        # 將zip資料轉成串列
print(player)                 # 列印串列

print('------------------------------------------------------------')	#60個

fields = ['Name', 'Age', 'Hometown']
info = ['Peter', '30', 'Chicago']
zipData = zip(fields, info)     # 執行zip
print(type(zipData))            # 列印zip資料類型
player = list(zipData)          # 將zip資料轉成串列
print(player)                   # 列印串列

f, i = zip(*player)             # 執行unzip
print("fields = ", f)
print("info   = ", i)

print('------------------------------------------------------------')	#60個

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
    print("使用者帳號 = ", account)                    # 列印鍵(key)
    name = account_info['last_name'] + " " + account_info['first_name']
    print(f"姓名       = {name}")                      # 列印值(value)
    print(f"城市       = {account_info['city']}")      # 列印值(value)

print('------------------------------------------------------------')	#60個

# 建立內含字典的字典
wechat = {'cshung':{
               'last_name':'洪',
               'first_name':'錦魁',
               'city':'台北'},
          'kevin':{
               'last_name':'鄭',
               'first_name':'義盟',
               'city':'北京'}}
# 列印字典元素個數
print(f"wechat字典元素個數       {len(wechat)}")
print(f"wechat['cshung']元素個數 {len(wechat['cshung'])}")
print(f"wechat['kevin']元素個數  {len(wechat['kevin'])}")

print('------------------------------------------------------------')	#60個

word = 'deepmind'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabetCount)

word = 'deepmind'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in set(word)}
print(alphabetCount)

print('------------------------------------------------------------')	#60個

cities = { 'Taipei', 'Beijing', 'Tokyo'}
# 增加一般元素
cities.add('Chicago')
print('cities集合內容 ', cities)
# 增加已有元素並觀察執行結果
cities.add('Beijing')
print('cities集合內容 ', cities)

print(type(cities))

A = {n for n in range(1,20,2)}
print(type(A))
print(A)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



