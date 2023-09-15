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


