print('dict使用範例')


'''
Dictionary(字典)

Dictionary是無序、沒有索引值且沒有重複的成員的容器，Pair的語法是key: value，一個key對應一個value，key不一定要是字串，但必須是唯一的。
'''

Number = {"five": 5, "ten": 10, "three": 3}
print(Number)		#打印dictionary

#語法是dict[key]，利用key來存取數量。dict[key] = value就可以改變數量。

print(Number["five"])	#5
Number["five"] = 50	#50
print(Number)		#打印dictionary

#增加dictionary
#只要給新的key就會產生新的資料。
Number["eight"] = 8
print(Number)		#打印dictionary




#移除dictionary
#使用pop(key)移除該key值的資料。
Number.pop("eight")
print(Number)		#打印dictionary


#取得所有資料
#使用keys()取得所有key值，回傳是所有key的List。
#取得所有數字
#使用values()取得所有value值，回傳是所有value的List。
#取得所有資料
#使用item()取得所有資料組，回傳是由(key, value)所組成的List。

print(Number.keys())
print(Number.values())
print(Number.items())



