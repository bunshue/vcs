
print('------------------------------------------------------------')	#60個

'''
A+B可以連接A和B字串。

Collections(容器)
Python提供四種Collections，分別是List、Tuple、Set、Dictionary

Collections總整理

Python提供四種Collections，分別是List、Tuple、Set、Dictionary，每個Collection都有各自的特色和使用時機，下面這些不用背起來，經常使用自然就會習慣了。

    列表(List)：有序且可更改的容器，允許重複的成員。
    組合(Tuple)：有序且不可更改的容器，允許重複的成員。
    集合(Set)：無序且未索引的容器，沒有重複的成員。
    字典(Dict)：無序且未索引的容器，沒有重複的成員，資料格式為key: value。
'''




print('------------------------------------------------------------')	#60個
print('List')

print('list使用範例')

print('一維list')
mylist = ["A", "B", "C", "D", "E"]

print('一一取出list內的值')
for elem in mylist:
    print(elem)

print('直接印出list')
print(mylist)

'''
#list排序

import SelectionSort 

lst = [3, 4, 1, 2, 0]
SelectionSort.selectionSort(lst)
print(lst)
'''

print('二維list')

data = list()
#         id_num, name, money
data.append((1, 'Banana', 777)) #裡面用()包起來的, 是一個tuple
data.append((2, 'Eagle', 111))
data.append((3, 'Giraffe', 222))
data.append((4, 'Cat', 444))
data.append((5, 'Apple', 333))
data.append((6, 'India', 555))
data.append((7, 'Happy', 999))
data.append((8, 'Frog', 666))
data.append((9, 'Dog', 888))
print(data)

data = list()
data1 =[5, 'Apple', 333]    #一維list
data2 =[1, 'Banana', 777]
data3 =[4, 'Cat', 444]
data4 =[9, 'Dog', 888]
data5 =[2, 'Eagle', 111]
data6 =[8, 'Frog', 666]
data7 =[3, 'Giraffe', 222]
data8 =[7, 'Happy', 999]
data9 =[6, 'India', 555]

#用9個一維list 組成一個2維list
data = [data1, data2, data3, data4, data5, data6, data7, data8, data9]
print(data)

print('二維list排序 依第0項排序')
data.sort(key = lambda e: (e[0]))
print(data)

print('二維list排序 依第1項排序')
data.sort(key = lambda e: (e[1]))
print(data)

print('二維list排序 依第2項排序, 並反相')
print(sorted(data, key = lambda t: (t[2]), reverse = True))

print('三維list')
dates = [
    [
        [ 1,  3,  5,  7],
        [ 9, 11, 13, 15],
        [17, 19, 21, 23],
        [25, 27, 29, 31]
    ],
    [
        [ 2,  3,  6,  7],
        [10, 11, 14, 15],
        [18, 19, 22, 23],
        [26, 27, 30, 31]
    ],
    [
        [ 4,  5,  6,  7],
        [12, 13, 14, 15],
        [20, 21, 22, 23],
        [28, 29, 30, 31]
    ],
    [
        [ 8,  9, 10, 11],
        [12, 13, 14, 15],
        [24, 25, 26, 27],
        [28, 29, 30, 31]
    ],
    [
        [16, 17, 18, 19],
        [20, 21, 22, 23],
        [24, 25, 26, 27],
        [28, 29, 30, 31]
    ]
]

print('印出三維list')
for i in range(5):
    for j in range(4):
         for k in range(4):
             print(format(dates[i][j][k], '4d'), end = " ")
         print()

person_data = [
    (110, 48226, 46644, 94870),
    (109, 48618, 47046, 95664),
    (108, 48532, 47018, 95550),
    (107, 48298, 46587, 94885),
    (106, 48156, 46295, 94451),
    (105, 48060, 46042, 94102),
    (104, 47861, 45482, 93343),
    (103, 47305, 44582, 91887),
    (102, 47333, 44628, 91961),
    (101, 47304, 44587, 91891)]

person_data.reverse()
print(type(person_data))
print(person_data)

print(len(person_data))

print('提取 前n筆資料, 組成一個二維list')
print(type(person_data[:5]))
print(person_data[:5])
print('提取 第n筆資料, tuple')
print(type(person_data[5]))
print(person_data[5])

print('提取 從a開始到b, 間隔c')
a = 0
b = 5
c = 2
print(person_data[a:b:c])


#取第一欄出來 成一個list ??




#一維list
candyCan = ["apple", "strawberry", "grape", "mango"]

print(candyCan)
print(len(candyCan))
print(type(candyCan))

print(candyCan[1])

#如果索引值是負的，則代表倒數第幾個。
print(candyCan[-1])

#就像昨天 Slicing String 一樣，[n:m] 表示從n取到m-1，返回一個新的List。
print(candyCan[1:3])

'''
添加資料(append)
插入資料(insert)

合併資料(extend)
使用 extend() 將兩個List合併在一起，就像字串的Concatenation。
'''





