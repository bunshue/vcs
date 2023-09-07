import sys

'''
各種python專用的語法 字典 串列 元組 集合

字典 dddd 大括號 {}
串列 llll
元組 tttt
集合 ssss

'''


print('字典 dddd ST------------------------------------------------------------')	#60個

'''
Dictionary(字典)
Dictionary是無序、沒有索引值且沒有重複的成員的容器，Pair的語法是key: value，一個key對應一個value，key不一定要是字串，但必須是唯一的。
'''

print('------------------------------------------------------------')	#60個

print('建立空字典')
animal = {}
print("空字典", animal)

animal = {
    'mouse':'老鼠',
    'panda':'貓熊',
    'penguin':'企鵝',
    'lion':'獅子',
}

print('增加字典內容')     #只要給新的key就會產生新的資料。
animal['tiger'] = '老虎'
animal['zebra'] = '斑馬'
animal['koala'] = '無尾熊'
animal['hippo'] = '河馬'

print('刪除字典內容')
del animal['penguin']

#移除dictionary
#使用pop(key)移除該key值的資料。
#animal.pop('penguin')

print(type(animal))
#打印字典
print(animal)
#語法是dict[key]，利用key來存取數量。dict[key] = value就可以改變數量。
print(animal['tiger'])

#取得所有資料
#使用keys()取得所有key值，回傳是所有key的List。
#取得所有數字
#使用values()取得所有value值，回傳是所有value的List。
#取得所有資料
#使用item()取得所有資料組，回傳是由(key, value)所組成的List。

print(animal.keys())
print(animal.values())
print(animal.items())

print('字典裡內容一一列出')
for key in animal:
    print(key + ": " + animal[key])

for ename, cname in animal.items():
    print("{:15s}{:15s}".format(ename, cname))

for ename in animal.keys():
    print(f"{ename},{animal[ename]}")

print('排序再顯示')
for ename in sorted(animal.keys()):
    print(f"{ename},{animal[ename]}")

print('排序 反相 再顯示')
for ename in sorted(animal.keys(),reverse=True):
    print(f"{ename},{animal[ename]}")

print('顯示values')
for cname in animal.values():
    print(cname)

animal_name = 'lion'
if animal_name in animal:
    print('有此動物 :', animal_name, '=>', animal[animal_name])
else:
    print('查無此動物 :', animal_name)

animal_name = 'dinosour'
if animal_name in animal:
    print('有此動物 :', animal_name, '=>', animal[animal_name])
else:
    print('查無此動物 :', animal_name)

print("目前字典元素數量     = ", len(animal))

print("將 字典 寫入檔案")
filename = 'C:/_git/vcs/_1.data/______test_files2/dict.txt'

with open(filename,'w') as fp:
    #將字典轉成字串寫入檔案
    fp.write(str(animal))
    
print("寫入檔案 : " + filename)


animal.clear()

print("目前字典內容:", animal)
print("目前字典元素數量     = ", len(animal))

print('------------------------------------------------------------')	#60個

# 建立內含字串的字典
sports = {'Curry':['籃球', '美式足球'],
          'Durant':['棒球'],
          'James':['美式足球', '棒球', '籃球']}

print(type(sports))
print(sports)

# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items():
          print("%s 喜歡的運動是: " % name)
# 列印value,這是串列
          for sport in favorite_sport:
              print("   ", sport)

print('------------------------------------------------------------')	#60個

# 建立內含字典的字典
wechat_account = {'cshung':{
                        'last_name':'洪',
                        'first_name':'錦魁',
                        'city':'台北'},
                  'kevin':{
                        'last_name':'鄭',
                        'first_name':'義盟',
                        'city':'北京'}
                 }

print(type(wechat_account))
print(wechat_account)

# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account['cshung']))
print("wechat_account['kevin']元素個數  ", len(wechat_account['kevin']))

print('------------------------------------------------------------')	#60個

fruits = {'Apple':20, 'Orange':25}
ret_value1 = fruits.get('Orange')
print("Value = ", ret_value1)
ret_value2 = fruits.get('Grape')
print("Value = ", ret_value2)
ret_value3 = fruits.get('Grape', 10)
print("Value = ", ret_value3)

print('------------------------------------------------------------')	#60個

# key在字典內
fruits = {'Apple':20, 'Orange':25}
ret_value = fruits.setdefault('Orange')
print("Value = ", ret_value)
print("fruits字典", fruits)
ret_value = fruits.setdefault('Orange',100)
print("Value = ", ret_value)
print("fruits字典", fruits)

print('------------------------------------------------------------')	#60個

person = {'name':'John'}
print("原先字典內容", person)

# 'age'鍵不存在
age = person.setdefault('age')
print("增加age鍵 ", person)
print("age = ", age)

# 'sex'鍵不存在
sex = person.setdefault('sex', 'Male')
print("增加sex鍵 ", person)
print("sex = ", sex)

print('------------------------------------------------------------')	#60個

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}                         # 空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()            # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:                
        if ch in ".,?":
            songLower = songLower.replace(ch,'')
print("不再有標點符號的歌曲")    
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()        
print("以下是歌曲串列")
print(songList)                     # 列印歌曲串列

# 將歌曲串列處理成字典 
for wd in songList:                 
        if wd in mydict:            # 檢查此字是否已在字典內
            mydict[wd] += 1         # 累計出現次數
        else:
            mydict[wd] = 1          # 第一次出現的字建立此鍵與值
    
print("以下是最後執行結果")
print(mydict)                       # 列印字典

print('------------------------------------------------------------')	#60個

abc = 'abcdefghijklmnopqrstuvwxyz'
encry_dict = {}
front3 = abc[:3]
end23 = abc[3:]
subText = end23 + front3
encry_dict = dict(zip(abc, subText))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

#msgTest = input("請輸入原始字串 : ")
msgTest = 'catdogelephant'

cipher = []
for i in msgTest:                       # 執行每個字元加密
    v = encry_dict[i]                   # 加密
    cipher.append(v)                    # 加密結果
ciphertext = ''.join(cipher)            # 將串列轉成字串

print("原始字串 ", msgTest)
print("加密字串 ", ciphertext)

print('------------------------------------------------------------')	#60個

print('摩斯密碼字典')
morse_code = {'A':'.-', 'B':'-...', 'C':'-.-.','D':'-..','E':'.',
              'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
              'K':'-.-', 'L':'.-..','M':'--', 'N':'-.','O':'---',
              'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
              'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
              'Z':'--..'}

print(type(morse_code))

#wd = input("請輸入大寫英文字: ")
wd = 'ABCDEFGHIJK'

for c in wd:
    print(morse_code[c])

print('------------------------------------------------------------')	#60個

adict = {'book':10, 'pen':3, 'earser':6, 'ruler':2}
print('打印字典的內容1')
for key, value in adict.items():
    if value < 5:
      print("({},{})".format(key, value))
print('打印字典的內容2')
print(adict)

print('------------------------------------------------------------')	#60個

#字典(dictionary)的資料型態
mydict = {'a':3, 'b':2, 'c':5}
print(mydict['a'])
mydict['d'] = 7
print(mydict)

print('------------------------------------------------------------')	#60個

print("字典測試 1")

dict1 ={
    "david":85,
    "lion":93,
    "mouse":67
    }

#name = input("輸入學生姓名：")
name = 'david'
if name in dict1:  
    print(name + "的成績為 " + str(dict1[name]))
else:  
    score = input("輸入學生分數：")
    dict1[name] = score
    print("字典內容：" + str(dict1))
    
print('------------------------------------------------------------')	#60個
    
print("字典測試 2")
#item
dict1={"金牌":26, "銀牌":34, "銅牌":30}
item1 = list(dict1.items())
for name, num in item1:
    print("得到的 %s 數目為 %d 面" % (name, num))

print('------------------------------------------------------------')	#60個

print("字典測試 3")
#key-value
dict1={"金牌":26, "銀牌":34, "銅牌":30}
listkey = list(dict1.keys())
listvalue = list(dict1.values())
for i in range(len(listkey)):
    print("得到的 %s 數目為 %d 面" % (listkey[i], listvalue[i]))
print('------------------------------------------------------------')	#60個

print("字典測試 4")
dict1 = {"A":"內向穩重", "B":"外向樂觀", "O":"堅強自信", "AB":"聰明自然"}
#name = input("輸入要查詢的血型:")
name = 'O'
blood = dict1.get(name)
if blood == None:  
    print("沒有「" + name + "」血型！")
else:  
    print(name + " 血型的個性為：" + str(dict1[name]))

print('------------------------------------------------------------')	#60個

print('dict使用範例')

class_101 = dict() #記錄學生座號及姓名
chi_score = dict() #記錄國文成績
eng_score = dict() #記錄英文成績
mat_score = dict() #記錄數學成績

subjects = ["國文", "英文", "數學"]
scores  = [chi_score, eng_score, mat_score]

class_101[1] = 'apple'
class_101[2] = 'banana'
class_101[4] = 'cat'
class_101[8] = 'dog'
print(class_101)

print('輸入國文成績')
subject_no = 0
no = 1
scores[subject_no][no] = 80
no = 2
scores[subject_no][no] = 85
no = 4
scores[subject_no][no] = 78
no = 8
scores[subject_no][no] = 88

print('顯示國文成績')
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print('輸入英文成績')
subject_no = 1
no = 1
scores[subject_no][no] = 84
no = 2
scores[subject_no][no] = 79
no = 4
scores[subject_no][no] = 92
no = 8
scores[subject_no][no] = 82

print('顯示英文成績')
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print('輸入數學成績')
subject_no = 2
no = 1
scores[subject_no][no] = 85
no = 2
scores[subject_no][no] = 91
no = 4
scores[subject_no][no] = 84
no = 8
scores[subject_no][no] = 77

print('顯示數學成績')
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print('顯示總成績')
for no in class_101.keys():
    print("{:<5}:".format(class_101[no]), end="")
    sum = 0
    for subject_no in range(0,3):
        sum = sum + scores[subject_no][no]
        print("{}:{:>3} ".format(subjects[subject_no], scores[subject_no][no]), end="")
    print("總分:{:>3}, 平均:{:.2f}".format(sum, float(sum)/len(scores)))

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('字典 dddd SP------------------------------------------------------------')	#60個


print('集合 ssss ST------------------------------------------------------------')	#60個

print('建立集合')
big_animal = set()
small_animal = set()
big_animal = {'lion', 'tiger'}
small_animal = set(['mouse', 'koala']) # Create a set from a list

print(big_animal)
print(small_animal)

print('在集合中新增元素')
big_animal.add('elephant')
big_animal.add('penguin')
big_animal.add('dinosour')
small_animal.add('penguin')
small_animal.add('bird')
small_animal.add('apple')

print(big_animal)
print(small_animal)

print('在集合中刪除元素')
big_animal.discard('dinosour')
small_animal.remove('apple')

print(big_animal)
print(small_animal)


print('交集 Set Intersection')
animal = big_animal & small_animal
print(animal)
animal = big_animal.intersection(small_animal)
print(animal)

print('聯集 Set Union')
animal = big_animal | small_animal
print(animal)
animal = big_animal.union(small_animal)
print(animal)

print('差集 Set Difference')
animal = big_animal - small_animal
print(animal)
animal = big_animal.difference(small_animal)
print(animal)

print('對稱差集 Set Symmetric Difference')
animal = big_animal ^ small_animal
print(animal)
animal = big_animal.symmetric_difference(small_animal)
print(animal)

print('集合的成員運算子')
print('大象是否在集合1之中?', 'elephant' in big_animal)
print('大象是否在集合2之中?', 'elephant' in small_animal)

print("length is", len(big_animal)) # Use function len
print("max is", max(big_animal)) # Use max
print("min is", min(big_animal)) # Use min
#print("sum is", sum(big_animal)) # Use sum



print('在集合中刪除全部元素')
big_animal.clear()
small_animal.clear()

print(big_animal)
print(small_animal)



print('------------------------------------------------------------')	#60個

#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
both1 = math & physics
print("同時參加數學與物理夏令營的成員 ",both1)
both2 = math.intersection(physics)
print("同時參加數學與物理夏令營的成員 ",both2)

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
allmember1 = math | physics
print("參加數學或物理夏令營的成員 ",allmember1)
allmember2 = math.union(physics)
print("參加數學或物理夏令營的成員 ",allmember2)

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_only1 = math - physics
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only1)
math_only2 = math.difference(physics)
print("參加數學夏令營同時沒有參加物理夏令營的成員 ",math_only2)
physics_only1 = physics - math
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only1)
physics_only2 = physics.difference(math)
print("參加物理夏令營同時沒有參加數學夏令營的成員 ",physics_only2)

print('------------------------------------------------------------')	#60個
#set
math = {'Kevin', 'Peter', 'Eric'}       # 設定參加數學夏令營成員
physics = {'Peter', 'Nelson', 'Tom'}    # 設定參加物理夏令營成員
math_sydi_physics1 = math ^ physics
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics1)
math_sydi_physics2 = math.symmetric_difference(physics)
print("沒有同時參加數學和物理夏令營的成員 ",math_sydi_physics2)

print('------------------------------------------------------------')	#60個

print('集合 ssss SP------------------------------------------------------------')	#60個


print('串列 llll ST------------------------------------------------------------')	#60個

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

print('串列 llll SP------------------------------------------------------------')	#60個



print('元組 tttt ST------------------------------------------------------------')	#60個


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




print('元組 tttt SP------------------------------------------------------------')	#60個


print('各種容器轉換 比較 ST------------------------------------------------------------')	#60個



empty_dict = {}                      # 這是建立空字典
empty_set = set()                    # 這是建立空集合
fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列

print('------------------------------------------------------------')	#60個




import random
import time


print('set 和 list 速度比較')
NUMBER_OF_ELEMENTS = 500

# Create a list
lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

# Create a set from the list
s = set(lst)

# Test if an element is in the set
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in s
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("To test if", NUMBER_OF_ELEMENTS, 
    "elements are in the set\n",
    "The runtime is", runTime, "milliseconds")

# Test if an element is in the list
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("\nTo test if", NUMBER_OF_ELEMENTS, 
    "elements are in the list\n",
    "The runtime is", runTime, "milliseconds")

# Remove elements from a set one at a time
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    s.remove(i)
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("\nTo remove", NUMBER_OF_ELEMENTS, 
    "elements from the set\n",
    "The runtime is", runTime, "milliseconds")

# Remove elements from a list one at a time
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    lst.remove(i)
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("\nTo remove", NUMBER_OF_ELEMENTS, 
    "elements from the list\n",
    "The runtime is", runTime, "milliseconds")


print('各種容器轉換 比較 SP------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



import sys

print('------------------------------------------------------------')	#60個

empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

print('------------------------------------------------------------')	#60個

x = set('DeepStone mean Deep Learning')
print(x)
print(type(x))

print('------------------------------------------------------------')	#60個

fruits1 = ['apple', 'orange', 'apple', 'banana', 'orange']
x = set(fruits1)                # 將串列轉成集合
fruits2 = list(x)               # 將集合轉成串列
print("原先串列資料fruits1 = ", fruits1)
print("新的串列資料fruits2 = ", fruits2)

print('------------------------------------------------------------')	#60個

# 方法1
fruits = set("orange")
print("字元a是屬於fruits集合?", 'a' in fruits)
print("字元d是屬於fruits集合?", 'd' in fruits)
# 方法2
cars = {"Nissan", "Toyota", "Ford"}
boolean = "Ford" in cars
print("Ford in cars", boolean)
boolean = "Audi" in cars
print("Audi in cars", boolean)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('字典範例')
cocktail = {
    'Blue Hawaiian':{'Rum','Sweet Wine','Cream','Pineapple Juice','Lemon Juice'},
    'Ginger Mojito':{'Rum','Ginger','Mint Leaves','Lime Juice','Ginger Soda'},
    'New Yorker':{'Whiskey','Red Wine','Lemon Juice','Sugar Syrup'},
    }
print(type(cocktail))

# 列出含有Lemon Juice的酒
print("含有Lemon Juice的酒 : ")
for name, formulas in cocktail.items():
    if 'Lemon Juice' in formulas:
        print(name)
# 列出含有Rum但是沒有薑的酒
print("含有Rum但是沒有薑的酒 : ")
for name, formulas in cocktail.items():
    if 'Rum' in formulas and not ('Ginger' in formulas):
        print(name)

print('------------------------------------------------------------')	#60個







s = list("3874950382")
print(s)
numbers = list()
for c in s:
    numbers.append(int(c))
print(sum(numbers))


print('------------------------------------------------------------')	#60個

s = list("3874950382")
print(s)
print(sum(map(int, s)))


print('------------------------------------------------------------')	#60個

def draw_bar(n):
    return "*"*n

s = [2, 5, 4, 7, 5, 4]
for bar in map(draw_bar, s):
    print(bar)

print('------------------------------------------------------------')	#60個



s = [2, 5, 4, 7, 5, 4]
for bar in map(lambda n: "*"*n, s):
    print(bar)




print('------------------------------------------------------------')	#60個

b = list('子丑寅卯辰巳午未申酉戌亥')
c = list('鼠牛虎兔龍蛇馬羊猴雞狗豬')
print(zip(b,c))
for item in zip(b, c):
    print(item)
print([item for item in zip(b, c)])


print('------------------------------------------------------------')	#60個


a = list('甲乙丙丁戊己庚辛壬癸')
b = list('子丑寅卯辰巳午未申酉戌亥')
for i in a:
    for j in b:
        print((i, j))

print('------------------------------------------------------------')	#60個

a = list('甲乙丙丁戊己庚辛壬癸')
b = list('子丑寅卯辰巳午未申酉戌亥')
years = list()
a_index = 0
b_index = 0
for i in range(60):
    years.append((a[a_index], b[b_index]))
    a_index += 1
    if a_index >= 10: 
        a_index = 0
    b_index += 1
    if b_index >= 12:
        b_index = 0
print(years)

print('------------------------------------------------------------')	#60個

a = list('甲乙丙丁戊己庚辛壬癸'*6)
b = list('子丑寅卯辰巳午未申酉戌亥'*5)
years = list(zip(a, b))
print(years)

print('------------------------------------------------------------')	#60個



