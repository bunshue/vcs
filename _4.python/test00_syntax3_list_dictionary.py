'''
一個list 裡面每個元件都是 dictionary

'''
price_data = [
{"name":"112/03/13","data":[{"name":"98 無鉛汽油","y":32.7,"GroupID":7}]},
{"name":"112/03/20","data":[{"name":"98 無鉛汽油","y":32.4,"GroupID":6}]},
{"name":"112/03/27","data":[{"name":"98 無鉛汽油","y":31.9,"GroupID":5}]},
{"name":"112/04/03","data":[{"name":"98 無鉛汽油","y":32.4,"GroupID":4}]},
{"name":"112/04/10","data":[{"name":"98 無鉛汽油","y":33.0,"GroupID":3}]},
{"name":"112/04/17","data":[{"name":"98 無鉛汽油","y":33.3,"GroupID":2}]},
{"name":"112/04/24","data":[{"name":"98 無鉛汽油","y":33.1,"GroupID":1}]},
{"name":"112/03/13","data":[{"name":"95 無鉛汽油","y":30.7,"GroupID":7}]},
{"name":"112/03/20","data":[{"name":"95 無鉛汽油","y":30.4,"GroupID":6}]},
{"name":"112/03/27","data":[{"name":"95 無鉛汽油","y":29.9,"GroupID":5}]}
];

print('資料型態 :\t', type(price_data))
print('資料長度 :\t', len(price_data))
print('資料內容')
for info in price_data:
    print(type(info))
    print(info)
    print('日期:', info['name'])
    #print(info['data'])
    for infos in info['data']:
        print(type(infos))
        print(infos)
        print('油品:', infos['name'])
        print('價格:', infos['y'])

'''
    
    for data in item['data']:
        if(data['name'] == '超級/高級柴油'):
            new_line = 0
            continue
        else:
            new_line = 1
        print("date:" + item['name'])   #第一層的 name 為日期
        print(data['name'] + ":" + str(data['y']))  #後面再接一層 array data 其中的 name 為產品名, 而 y 為單價
    if (new_line == 1):
        print("================")
'''








print('一維list')
candyCan = ["apple", "strawberry", "grape", "mango"]
print(type(candyCan))

candyCan[1] = "peach"
print(candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan.append("banana")
print(candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

candyCan.insert(1, "orange")
print(candyCan)



candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan[1])
print(candyCan[-1])
print(candyCan[1:3])

candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan)
print(len(candyCan))
print(type(candyCan))

candyCan = ["apple", "strawberry", "grape", "mango"]

print("apple" in candyCan)
print("banana" in candyCan)


candyCan = ["apple", "strawberry", "grape", "mango"]

newCandy = ["banana", "orange"]
temp = candyCan + newCandy
print(temp)
print(candyCan)
print(newCandy)

'''
candyCan = ("apple", "strawberry", "mango", "peach", "grape")

candyCan[1] = "banana"


candyCan = ("apple", "strawberry", "mango", "peach", "grape")

print(candyCan)
print(len(candyCan))

print(candyCan[0])
print(candyCan[1:3])

print(candyCan.count("mango"))
print(candyCan.index("mango"))
'''

print('set 範例')
candyFlavor = {"apple", "strawberry", "mango", "mango"}
print(type(candyFlavor))
print(candyFlavor)

candyFlavor.add("orange")
print(candyFlavor)

candyFlavor.remove("orange")
print(candyFlavor)

newFlavor = {"apple", "banana"}
candyFlavor.update(newFlavor)
print(candyFlavor)


print('dictionary 範例')
candyNumber = {"apple": 5, "strawberry": 10, "mango": 3}
print(type(candyNumber))
print(candyNumber)

print(candyNumber["apple"])
candyNumber["apple"] = 6
print(candyNumber)

candyNumber["banana"] = 8
print(candyNumber)

candyNumber.pop("banana")
print(candyNumber)

print(candyNumber.keys())
print(candyNumber.values())
print(candyNumber.items())



