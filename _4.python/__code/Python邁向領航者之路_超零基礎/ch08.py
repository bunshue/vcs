# ch8_1.py
numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
mixed = ('James', 50)           # 定義元組元素是不同型態資料
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1)
print(fruits)
print(mixed)
print(val_tuple)
# 列出元組資料型態
print("元組mixed資料型態是: ",type(mixed))

print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_2.py

# ch8_2.py
numbers1 = (1, 2, 3, 4, 5)      # 定義元組元素是整數
fruits = ('apple', 'orange')    # 定義元組元素是字串
val_tuple = (10,)               # 只有一個元素的元祖
print(numbers1[0])              # 以中括號索引值讀取元素內容
print(numbers1[4])
print(fruits[0])
print(fruits[1])
print(val_tuple[0])

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_3.py

# ch8_3.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
for key in keys:
    print(key)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_4.py

# ch8_4.py
fruits = ('apple', 'orange')        # 定義元組元素是字串
print(fruits[0])                    # 列印元組fruits[0]
fruits[0] = 'watermelon'            # 將元素內容改為watermelon
print(fruits[0])                    # 列印元組fruits[0]

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_5.py

# ch8_5.py
fruits = ('apple', 'orange')        # 定義元組元素是水果
print("原始fruits元組元素")
for fruit in fruits:
    print(fruit)

fruits = ('watermelon', 'grape')    # 定義新的元組元素
print("\n新的fruits元組元素")
for fruit in fruits:
    print(fruit)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_6.py

# ch8_6.py     
fruits = ('apple', 'orange', 'banana', 'watermelon', 'grape')
print(fruits[1:3])
print(fruits[:2])
print(fruits[1:])
print(fruits[-2:])
print(fruits[0:5:2])
      

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_7.py

# ch8_7.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
print("keys元組長度是 %d " % len(keys))


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_8.py

# ch8_8.py
keys = ('magic', 'xaab', 9099)      # 定義元組元素是字串與數字
list_keys = list(keys)              # 將元組改為串列
list_keys.append('secret')          # 增加元素
print("列印元組", keys)
print("列印串列", list_keys)


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_9.py

# ch8_9.py
keys = ['magic', 'xaab', 9099]      # 定義串列元素是字串與數字
tuple_keys = tuple(keys)            # 將串列改為元組
print("列印串列", keys)
print("列印元組", tuple_keys)
tuple_keys.append('secret')         # 增加元素 --- 錯誤錯誤



print('------------------------------------------------------------')	#60個



#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_10.py

# ch8_10.py
tup = (1, 3, 5, 7, 9)
print("tup最大值是", max(tup))
print("tup最小值是", min(tup))

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_11.py

# ch8_11.py
dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
data = divmod(total_hours, 24)  # 商和餘數
print("divmod傳回的資料型態是 : ", type(data))
print("總供需要 %d 天" % data[0])
print("%d 小時" % data[1])






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_12.py

# ch8_12.py
fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)                 # 執行zip
print('zipData資料類型', type(zipData))     # 列印zip資料類型
player = list(zipData)                      # 將zip資料轉成串列
print('player 資料類型', type(player))      # 列印player資料類型
print(player)                               # 列印串列














print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch08\ch8_13.py

# ch8_13.py
fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)                 # 執行zip
sold_info = list(zipData)                   # 將zip資料轉成串列
for city, sales in sold_info:
    print('{} 銷售金額是 {}'.format(city, sales))


print('------------------------------------------------------------')	#60個




