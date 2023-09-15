import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

'''
ChineseZodiacSigns = {'鼠' : 5, '牛' : 32, '虎' : 17, '兔' : 8 }
print(type(ChineseZodiacSigns))
print(ChineseZodiacSigns)
'''


print('------------------------------------------------------------')	#60個

print('字典 操作')
animals = {'鼠' : 5, '牛' : 32, '虎' : 17, '兔' : 8 }

animals = {'鼠' : ('mouse', 4),
           '牛' : ('ox', 48),
           '虎' : ('tiger', 33),
           '兔' : ('rabbit', 8),
           '龍' : ('dragon', 38),
           '蛇' : ('snake', 15),
           '馬' : ('horse', 32),
           '羊' : ('goat', 26),
           '猴' : ('monkey', 22),
           '雞' : ('chicken', 6),
           '狗' : ('dog', 12),
           '豬' : ('pig', 42),
           }

animals['象'] = ('elephant', 100)

print(type(animals))
print(animals)
print(animals['龍'])

print('預設排序')
for key in animals:
    print("{}:{}".format(key, animals[key]))

print('依英文名稱排序')
ani = sorted(animals.items(), key=lambda item:item[1][0])
print('中文名稱', '        英文名稱 ',  ' 體重')
for i in range(len(ani)):
    print(f"{ani[i][0]:8s}{ani[i][1][0]:10s}{ani[i][1][1]:8d}")

   
print('依體重排序')
ani = sorted(animals.items(), key=lambda item:item[1][1])
print('中文名稱', '        英文名稱 ',  ' 體重')
for i in range(len(ani)):
    print(f"{ani[i][0]:8s}{ani[i][1][0]:10s}{ani[i][1][1]:8d}")

print('------------------------------------------------------------')	#60個

animals = ['鼠','牛','虎','兔','龍']
print(animals)
animals.append('蛇')
print(animals)
animals.insert(3,'馬')
print(animals)
animals.remove('虎')
print(animals)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']
print("目前animals串列 : ", animals)

for ani in animals[:]:
    animals.remove(ani)
    print(f"刪除 {ani}")
    print("目前animals串列 : ", animals)

print('------------------------------------------------------------')	#60個

animals = ['鼠','牛','虎','兔','龍','蛇','馬','羊','猴','雞','狗','豬']

print(animals)

for ani in animals:
    print(ani)

print(animals)

print(animals[:3])

print(animals[3:7])


print(animals[7:])


print('------------------------------------------------------------')	#60個

animals = list('鼠牛虎兔龍蛇馬羊猴雞狗豬')

print(animals)
print(animals[9])
print(animals[-1])
print(animals[3:6])
print(animals[5:])
print(animals[:5])
print(animals[:-2])

#測試list之最後5筆資料

print(animals[-5:])

print('------------------------------------------------------------')	#60個

cc = [('mouse', '老鼠', 1), ('panda', '貓熊', 123), ('penguin', '企鵝', 29), ('lion', '獅子', 270), ('tiger', '老虎', 240), ('zebra', '斑馬', 365), ('koala', '無尾熊', 13), ('hippo', '河馬', 996)]
print(type(cc))
print(cc)




print('------------------------------------------------------------')	#60個

# 建立內含字典的字典
animals = {
    '鼠':{
        'cname':'鼠',
        'ename':'mouse',
        'weight':'13'},
    '牛':{
        'cname':'牛',
        'ename':'ox',
        'weight':'82'}}

# 列印內含字典的字典
for animal, animal_info in animals.items( ):
    print("名稱 = ", animal)                    # 列印鍵(key)
    cname = animal_info['cname']
    ename = animal_info['ename']
    print('中文名 :', cname)
    print('英文名 :', ename)
    print("體重       = {animal_info['weight']}")      # 列印值(value)

# 列印字典元素個數
print(f"animals字典元素個數       {len(animals)}")
print(f"animals['鼠']元素個數 {len(animals['鼠'])}")
print(f"animals['牛']元素個數  {len(animals['牛'])}")

print('------------------------------------------------------------')	#60個

word = 'deepmind'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in word}
print(alphabetCount)

word = 'deepmind'
alphabetCount = {alphabet:word.count(alphabet) for alphabet in set(word)}
print(alphabetCount)

print('------------------------------------------------------------')	#60個

#set   集合 ssss 大括號 {} 無順序 不可重複 set元素具有唯一性

cities = { 'Taipei', 'Beijing', 'Tokyo'}
print(type(cities))
print(cities)
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

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
sc.sort(key = lambda x:x[1])
print(sc)

sc = [['John', 80],['Tom', 90], ['Kevin', 77]]
newsc = sorted(sc, key = lambda x:x[1])
print(newsc)


sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)


print('------------------------------------------------------------')	#60個


dict1={"林小明":85, "曾山水":93, "鄭美麗":67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listitem = dict1.items()
for name, score in listitem:
    print("%s 的成績為 %d 分" % (name, score))


dict1={"林小明":85, "曾山水":93, "鄭美麗":67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的成績為 %d 分" % (listkey[i], listvalue[i]))





print('------------------------------------------------------------')	#60個

print('list 使用')
lst = [3, 2, 1, 5, 9, 0]
print(type(lst))
print(lst)
sorted(lst)
print(lst)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





'''

container

parsers = {'clinic' : DSLParser, 'python': PythonParser}


    test_cases = (
        ({"before": {"session": 0}, "after": {"session": 1}}, "LoginEvent"),
        ({"before": {"session": 1}, "after": {"session": 0}}, "LogoutEvent"),
        ({"before": {"session": 1}, "after": {"session": 1}}, "UnknownEvent"),
    )

    test_cases = (
        *BaseTestOCP.test_cases,
        ({"after": {"transaction": "Tx001"}}, "TransactionEvent"),
        ({"after": {"not-a-transaction": "Tx001"}}, "UnknownEvent"),
    )





'''
