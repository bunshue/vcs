'''
tuple 範例

'''

print('------------------------------------------------------------')	#60個

animal = ('mouse', 'panda', 'lion', 'tiger')    # 定義元組元素是字串
print("animal元組長度是 %d " % len(animal))
for i in range(len(animal)):
    print(animal[i])    # 列印元組animal[i]

print('------------------------------------------------------------')	#60個

animal = ('mouse', 'panda', 'lion', 'tiger')    # 定義元組元素是字串
print("原始animal元組元素")
for animal_name in animal:
    print(animal_name)

print('------------------------------------------------------------')	#60個

animal = ('mouse', 'panda', 'lion', 'tiger', 'hippo')    # 定義元組元素是字串
print(animal[1:3])
print(animal[:2])
print(animal[1:])
print(animal[-2:])
print(animal[0:5:2])
      
print('------------------------------------------------------------')	#60個

tuple_animal = ('mouse', 'panda', 'lion', 'tiger', 'hippo')    # 定義元組元素是字串
list_animal = list(tuple_animal)              # 將元組改為串列
list_animal.append('elephant')          # 增加元素
print("列印元組", tuple_animal)
print("列印串列", list_animal)

print('------------------------------------------------------------')	#60個

list_animal = ['mouse', 'panda', 'lion', 'tiger', 'hippo']      # 定義串列元素是字串
tuple_animal = tuple(list_animal)            # 將串列改為元組
print("列印串列", list_animal)
print("列印元組", tuple_animal)

#tuple禁止使用append
#tuple_animal.append('elephant')         # 增加元素 --- 錯誤錯誤

print('------------------------------------------------------------')	#60個

animal = ('mouse', 'panda', 'lion', 'tiger', 'hippo')    # 定義元組元素是字串

print("animal最大值是", max(animal))
print("animal最小值是", min(animal))

print('------------------------------------------------------------')	#60個

dist = 384400                   # 地球到月亮距離
speed = 1225                    # 馬赫速度每小時1225公里
total_hours = dist // speed     # 計算小時數
data = divmod(total_hours, 24)  # 商和餘數
print("divmod傳回的資料型態是 : ", type(data))
print("總供需要 %d 天" % data[0])
print("%d 小時" % data[1])

print('------------------------------------------------------------')	#60個

fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)                 # 執行zip
print('zipData資料類型', type(zipData))     # 列印zip資料類型
player = list(zipData)                      # 將zip資料轉成串列
print('player 資料類型', type(player))      # 列印player資料類型
print(player)                               # 列印串列

print('player0 資料類型', type(player[0]))      # 列印player資料類型
print('player1 資料類型', type(player[1]))      # 列印player資料類型
print('player2 資料類型', type(player[2]))      # 列印player資料類型

print('------------------------------------------------------------')	#60個

fields = ['台北', '台中', '高雄']
info = [80000, 50000, 60000]
zipData = zip(fields, info)                 # 執行zip
sold_info = list(zipData)                   # 將zip資料轉成串列
for city, sales in sold_info:
    print('{} 銷售金額是 {}'.format(city, sales))

print('------------------------------------------------------------')	#60個







tuple1 = ("green", "red", "blue") # Create a tuple
print(tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5]) # Create a tuple from a list
print(tuple2)

print("length is", len(tuple2)) # Use function len
print("max is", max(tuple2)) # Use max
print("min is", min(tuple2)) # Use min
print("sum is", sum(tuple2)) # Use sum

print("The first element is", tuple2[0]) # Use indexer

tuple3 = tuple1 + tuple2 # Combine 2 tuples
print(tuple3)

tuple3 = 2 * tuple1 # Multiple a tuple
print(tuple3)

print(tuple2[2 : 4]) # Slicing operator
print(tuple1[-1])

print(2 in tuple2) # in operator

for v in tuple1:
    print(v, end = " ")
print()
    
list1 = list(tuple2) # Obtain a list from a tuple
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print(tuple4)
print(tuple4 == tuple5) # Compare two tuples 
