import os
import sys
import time
import random


print('------------------------------------------------------------')	#60個

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8 }
print(type(animals))
print(animals)

print('------------------------------------------------------------')	#60個

print('字典 操作')
animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8 }

animals = {'鼠' : ('mouse', 3),
           '牛' : ('ox', 48),
           '虎' : ('tiger', 33),
           '兔' : ('rabbit', 8),
           '龍' : ('dragon', 38),
           '蛇' : ('snake', 16),
           '馬' : ('horse', 36),
           '羊' : ('goat', 29),
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

# 建立內含字典的字典
animals = {
    '鼠':{
        'cname':'鼠',
        'ename':'mouse',
        'weight':'3'},
    '牛':{
        'cname':'牛',
        'ename':'ox',
        'weight':'48'}}

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

dict1={"林小明" : 85, "曾山水" : 93, "鄭美麗" : 67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listitem = dict1.items()
for name, score in listitem:
    print("%s 的成績為 %d 分" % (name, score))

dict1={"林小明" : 85, "曾山水" : 93, "鄭美麗" : 67}
dict1["黃明品"] = 71
dict1["陳莉莉"] = 98
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("%s 的成績為 %d 分" % (listkey[i], listvalue[i]))

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
