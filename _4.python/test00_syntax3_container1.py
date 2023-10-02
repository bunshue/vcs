import sys

"""
各種python專用的語法 字典 串列 元組 集合

dict  字典 dddd 大括號 {} 無順序 不可重複 = 集合 + list  d = {"key :value", "key :value", ...}
lsit  串列 llll 中括號 [] 有順序 允許重複 list中的data type不用一致
tuple 元組 tttt 小括號 () 有順序 允許重複 不可變清單	常數list
set   集合 ssss 大括號 {} 無順序 不可重複 set元素具有唯一性


Collections(容器)
Python提供四種Collections，分別是List、Tuple、Set、Dictionary

Collections總整理

Python提供四種Collections，分別是List、Tuple、Set、Dictionary，每個Collection都有各自的特色和使用時機，下面這些不用背起來，經常使用自然就會習慣了。

    列表(List)：有序且可更改的容器，允許重複的成員。
    組合(Tuple)：有序且不可更改的容器，允許重複的成員。
    集合(Set)：無序且未索引的容器，沒有重複的成員。
    字典(Dict)：無序且未索引的容器，沒有重複的成員，資料格式為key: value。



empty_dict = {}                      # 這是建立空字典
empty_set = set()                    # 這是建立空集合

empty_dict = {}                      # 這是建立空字典
print("列印類別 = ", type(empty_dict))

empty_set = set()                    # 這是建立空集合
print("列印類別 = ", type(empty_set))

Dictionary(字典)
Dictionary是無序、沒有索引值且沒有重複的成員的容器，Pair的語法是key: value，一個key對應一個value，key不一定要是字串，但必須是唯一的。

"""



a_dict = {}
print(type(a_dict))

a_list = []
print(type(a_list))


table1 = [] #list
table2 = {} #dict
print(type(table1))
print(type(table2))



print('字典 dddd ST------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('建立空字典')
animal = {}
print("空字典", animal)

animal = {
    'mouse':'鼠',
    'ox':'牛',
    'tiger':'虎',
    'rabbit':'兔',
}

print('增加字典內容')     #只要給新的key就會產生新的資料。
animal['dragon'] = '龍'
animal['snake'] = '蛇'
animal['horse'] = '馬'
animal['goat'] = '羊'

print('刪除字典內容')
del animal['snake']

#移除dictionary
#使用pop(key)移除該key值的資料。
#animal.pop('snake')

print(type(animal))
#打印字典
print(animal)
#語法是dict[key]，利用key來存取數量。dict[key] = value就可以改變數量。
print(animal['dragon'])

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

animal_name = 'dragon'
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

animals = {
    '鼠':['生性樂觀', '適應力強', '坐言起行'],
    '牛':['思想細密', '目標清晰', '老實可靠', '活潑機智', '永不言倦'],
    '虎':['胸懷大志', '生性獨立', '著重行動', '挑戰自己']
    }

print(type(animals))
print(animals)

# 列印key名字 + 字串'喜歡的運動'
for name, character in animals.items():
          print("動物 %s 的特性是 : " % name)
# 列印value,這是串列
          for ch in character:
              print("   ", ch)

print('------------------------------------------------------------')	#60個

# 建立內含字典的字典
animals = {
    '鼠':
    {
        '特性1':'生性樂觀',
        '特性2':'適應力強',
        '特性3':'坐言起行'
    },
    '牛':
    {
        '特性1':'思想細密',
        '特性2':'目標清晰',
        '特性3':'老實可靠',
        '特性4':'活潑機智',
        '特性5':'永不言倦'
    }
    }

print(type(animals))
print(animals)

# 列印字典元素個數
print("animals字典元素個數       ", len(animals))
print("animals['鼠']元素個數 ", len(animals['鼠']))
print("animals['牛']元素個數  ", len(animals['牛']))

print('------------------------------------------------------------')	#60個

animals = {'鼠' : 3, '牛' : 48}
ret_value1 = animals.get('牛')
print("Value = ", ret_value1)
ret_value2 = animals.get('虎')
print("Value = ", ret_value2)
ret_value3 = animals.get('虎', 10)
print("Value = ", ret_value3)

print('------------------------------------------------------------')	#60個

# key在字典內
animals = {'鼠' : 3, '牛' : 48}
ret_value = animals.setdefault('牛')
print("Value = ", ret_value)
print("animals字典", animals)
ret_value = animals.setdefault('牛',100)
print("Value = ", ret_value)
print("animals字典", animals)

print('------------------------------------------------------------')	#60個

animal_mouse = {'name' : 'mouse'}
print("原先字典內容", animal_mouse)

# 'cname'鍵不存在
#cname = animal_mouse.setdefault('cname')    #未填入值
cname = animal_mouse.setdefault('cname', '鼠')    #有填入值
print("增加cname鍵 ", animal_mouse)
print("cname = ", cname)

# 'weight'鍵不存在
weight = animal_mouse.setdefault('weight', 3)
print("增加weight鍵 ", animal_mouse)
print("weight = ", weight)

print('------------------------------------------------------------')	#60個

print('字典 操作')
animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}
print(type(animals))
print(animals)

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

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}

print('打印字典的內容1')
for key, value in animals.items():
    if value < 5:
      print("({},{})".format(key, value))

print('打印字典的內容2')
print(animals)

print('------------------------------------------------------------')	#60個

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}

#字典(dictionary)的資料型態
print(animals['鼠'])
animals['兔'] = 6
print(animals)

print('------------------------------------------------------------')	#60個

print("字典測試 1")

animals = {
    "mouse" : 3,
    "ox" : 48,
    "tiger" : 33
    }

ani = 'tiger'
if ani in animals:  
    print(ani + "的體重為 " + str(animals[ani]))
    
print('------------------------------------------------------------')	#60個
    
print("字典測試 2")

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}
print('字典 轉 串列')
item1 = list(animals.items())
for animal, weight in item1:
    print("動物 %s 的體重為 %d" % (animal, weight))

print('------------------------------------------------------------')	#60個

print("字典測試 3")

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}
listkey = list(animals.keys())
listvalue = list(animals.values())
for i in range(len(listkey)):
    print("動物 %s 的體重為 %d" % (listkey[i], listvalue[i]))

print('------------------------------------------------------------')	#60個

print("字典測試 4")

animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8, '龍' : 38}
name = '鼠'
weight = animals.get(name)
if weight == None:  
    print("沒有 " + name + " 動物")
else:  
    print("找到動物" + name + ", 體重為 :" + str(animals[name]))

print('------------------------------------------------------------')	#60個

animals={"鼠" : 3, "牛" : 48, "虎" : 33}
animals["兔"] = 8
animals["龍"] = 38
animals_item = animals.items()
for name, weight in animals_item:
    print("%s 的體重為 %d" % (name, weight))

animals={"鼠" : 3, "牛" : 48, "虎" : 33}
animals["兔"] = 8
animals["龍"] = 38
animals_key = list(animals.keys())
animals_value = list(animals.values())
for i in range(len(animals_key)):
    print("%s 的體重為 %d" % (animals_key[i], animals_value[i]))

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
animals = {'鼠': 3, '牛': 48, '虎': 33}
print(type(animals))
print(animals)

print(animals['鼠'])
animals['鼠'] = 5
print(animals)

animals['兔'] = 8
print(animals)

animals.pop('兔')
print(animals)

print(animals.keys())
print(animals.values())
print(animals.items())

print('------------------------------------------------------------')	#60個

print('字典範例')

animals = {
    '鼠' : {'生性樂觀', '適應力強', '坐言起行'},
    '牛' : {'思想細密', '目標清晰', '老實可靠', '活潑機智', '永不言倦'},
    '虎' : {'胸懷大志', '生性獨立', '著重行動', '挑戰自己'},
    '兔' : {'性情溫馴', '挑戰自己', '坐言起行', '頭腦清晰'},
    '龍' : {'積極進取', '胸懷大志', '行動敏捷', '性情溫馴'},
    '蛇' : {'才智非凡', '永不言倦', '情感豐富'},
    '馬' : {'活潑機智', '積極進取', '目標清晰', '積極進取'},
    '羊' : {'心思慎密', '溫柔體貼', '永不言倦', '有第六感', '挑戰自己'},
    '猴' : {'有幽默感', '頭腦清晰', '思考周詳', '行動敏捷', '生性獨立'},
    '雞' : {'思想細密', '頭腦靈活', '胸懷大志', '永不言倦', '有第六感', '性情溫馴', '適應力強'},
    '狗' : {'坐言起行', '直覺敏銳', '生性樂觀', '尊師重道', '直覺敏銳', ''},
    '豬' : {'活潑機智', '生性獨立', '適應力強', '性情溫馴'},
    }

print(type(animals))

print("含有 適應力強 的動物 :")
for name, character in animals.items():
    if '適應力強' in character:
        print(name)

print("含有 適應力強 但是不含 生性樂觀 的動物 : ")
for name, character in animals.items():
    if '適應力強' in character and not ('生性樂觀' in character):
        print(name)

print('------------------------------------------------------------')	#60個

print('字典的用法')

animals = {
    '鼠': 'mouse',
    '牛': 'ox',
    '虎': 'tiger',
}

print(type(animals))
print(animals)

for cname, ename in animals.items():
    name = '%s %s' % (cname, ename)
    print(name)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('字典 dddd SP------------------------------------------------------------')	#60個


print('集合 ssss ST------------------------------------------------------------')	#60個

#大動物 : [牛虎龍馬豬][羊猴][象] 8
#小動物 : [鼠兔蛇雞狗][羊猴][龜] 8
    
print('建立集合')
big_animal = set()
small_animal = set()
big_animal = {'牛', '虎', '龍', '馬', '馬', '馬'}
small_animal = set(['鼠', '兔', '蛇', '雞', '雞', '雞']) #由串列轉集合

print('大動物 :', big_animal)
print('小動物 :', small_animal)

print('在集合中新增元素')
big_animal.add('豬')
big_animal.add('羊')
big_animal.add('猴')
big_animal.add('象')

new_small_animals = {'狗', '羊', '猴', '龜'}
small_animal.update(new_small_animals)

print('大動物 :', big_animal)
print('小動物 :', small_animal)

print('在集合中刪除元素')
big_animal.discard('象')
small_animal.remove('龜')

print('大動物 :', big_animal)
print('小動物 :', small_animal)

print('比較兩集合是否相等')
print(big_animal == small_animal)

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
print('龍 是否在集合1之中?', '龍' in big_animal)
print('龍 是否在集合2之中?', '龍' in small_animal)

print("length is", len(big_animal)) # Use function len
print("max is", max(big_animal)) # Use max
print("min is", min(big_animal)) # Use min
#print("sum is", sum(big_animal)) # Use sum

print('在集合中刪除全部元素')
big_animal.clear()
small_animal.clear()

print('大動物 :', big_animal)
print('小動物 :', small_animal)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

animal_list = ['鼠', '牛', '虎', '兔', '龍']
print('原 串列')
print(animal_list)

print('串列 轉 集合')
animal_set = set(animal_list)
print(animal_set)

print('集合長度 :', len(animal_set))
print('最大 :', max(animal_set))
print('最小 :', min(animal_set))

print('集合 轉 串列')
animal_list = list(animal_set)
print(animal_list)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('集合 ssss SP------------------------------------------------------------')	#60個


print('串列 llll ST------------------------------------------------------------')	#60個

print('一維 串列')

print('建立串列')

animals = ['鼠', '牛', '虎', '兔', '龍']

print('原串列 :', animals)
print('串列 增加項目')
animals.append('蛇')
animals.append('蛇')
animals.append('蛇')
new_animals = ['馬', '羊']
animals = animals + new_animals
print('新串列 :', animals)
print('改變第1項的值')
animals[1] = '豬'
print(animals)

print('在第1項的位置安插一個項目')
print('原串列 :', animals)
animals.insert(1, '猴')
print('新串列 :', animals)

print('牛 是否在 串列 裏?', "牛" in animals)
print('豬 是否在 串列 裏?', '豬' in animals)

print('一維 串列')
animals = ['鼠', '牛', '虎', '兔', '龍']

print('一一取出 串列 內的值')
for ani in animals:
    print(ani)

print('直接印出 串列')
print(animals)

print('顛倒排序串列')
animals.reverse()   # 顛倒排序串列
print(animals)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']
print("目前animals串列 : ", animals)
animals.append('蛇')
print("目前animals串列 : ", animals)
animals.insert(3,'馬')
print("目前animals串列 : ", animals)
animals.remove('虎')
print("目前animals串列 : ", animals)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']
print("目前animals串列 : ", animals)

for ani in animals[:]:
    animals.remove(ani)
    print(f"刪除 {ani}")
    print("目前animals串列 : ", animals)

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔', '龍']
print('型態 :', type(animals))
print('長度 :', len(animals))
print('原串列 :', animals)
print('列印全部項目')
print(animals)
print('列印前3個')
print(animals[:3])
print('列印 第1到第4個(不含)')
print(animals[1:4])
print('列印 第3個(含)以後')
print(animals[3:])
print('第1項  :', animals[1])
print('最後1項 :', animals[-1])    ##如果索引值是負的，則代表倒數第幾個。
print('第1~3項 :', animals[1:4], '\t要用[1:4]') #[n:m] 表示從n取到m-1，返回一個新的List。

print(animals[3])
print(animals[-1])
print(animals[1:4])
print(animals[3:])
print(animals[:5])
print(animals[:-2])

#測試list之最後5筆資料
print(animals[-3:])

import numpy as np
for i in range(5):
    c = np.random.choice(animals)
    print(f"本次抽中 {c}。")

llll = ['鼠', '牛', '虎', '兔', '龍']
pppp = llll[2:] #第二項(含)以後的
print(llll)
print(pppp)

print('------------------------------------------------------------')	#60個

print('字串 轉 串列')
animals = list('鼠牛虎兔龍蛇馬羊猴雞狗豬')
print('列印全部項目')
print(animals)

print('------------------------------------------------------------')	#60個

print('字串 轉 串列')

s = list('鼠牛虎兔龍蛇馬羊猴雞狗豬')
print(type(s))
print(s)
s = list("3874950382")

#print(sum(map(int, s)))    fail in kilo

"""
numbers = list()

for c in s:
    numbers.append(int(c))
#print(sum(numbers))    fail in kilo
"""

print('------------------------------------------------------------')	#60個

print('串列 使用')
animals = ['鼠', '牛', '虎', '兔', '龍']
print(type(animals))

print('列印全部項目')
print(animals)

print('列印排序後的結果')
animal_sorted = sorted(animals)
print(animal_sorted)

print('------------------------------------------------------------')	#60個

print('串列 操作')
animals = [('mouse', '鼠', 3),
      ('ox', '牛', 48),
      ('tiger', '虎', 33),
      ('rabbit', '兔', 8),
      ('dragon', '龍', 38),
      ('snake', '蛇', 16),
      ('horse', '馬', 36),
      ('goat', '羊', 29),
      ('monkey', '猴', 22),
      ('chicken', '雞', 6),
      ('dog', '狗', 12),
      ('pig', '豬', 42)
      ]
print(type(animals))
print(animals)

print('------------------------------------------------------------')	#60個

print('串列')
animals = [['鼠', 3], ['牛', 48], ['虎', 33]]
print(type(animals))
print(animals)

animals.sort(key = lambda x:x[1])
print(animals)

print('-------------')
print('串列')
animals = [['鼠', 3], ['牛', 48], ['虎', 33]]
print(type(animals))
print(animals)

animals1 = sorted(animals, key = lambda x:x[1])
print(type(animals1))
print(animals1)

print('-------------')
print('字典')
animals = {'鼠' : 3, '牛' : 48, '虎' : 33}
print(type(animals))
print(animals)

animals2 = sorted(animals.items(), key = lambda x:x[0])  # 依照key排序
print("依照名稱排序")
print(animals2)

animals3 = sorted(animals.items(), key = lambda x:x[1])  # 依照value排序
print("依照體重排序")
print(animals3)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('二維 串列')

animal_list = list()
#         id_num, name, weight
animal_list.append((1, '鼠', 3)) #裡面用()包起來的, 是一個tuple
animal_list.append((2, '牛', 48))
animal_list.append((3, '虎', 33))
animal_list.append((4, '兔', 8))
animal_list.append((5, '龍', 38))
print(animal_list)

animal1 =[5, '龍', 38]    #一維 串列
animal2 =[1, '鼠', 3]
animal3 =[4, '兔', 8]
animal4 =[2, '牛', 48]
animal5 =[3, '虎', 33]

#用5個一維 串列 組成一個2維 串列
animal_list = list()
animal_list = [animal1, animal2, animal3, animal4, animal5]
print(animal_list)

print('二維 串列 排序 依第0項排序')
animal_list.sort(key = lambda e: (e[0]))
print(animal_list)

print('二維 串列 排序 依第1項排序')
animal_list.sort(key = lambda e: (e[1]))
print(animal_list)

print('二維 串列 排序 依第2項排序, 並反相')
print(sorted(animal_list, key = lambda t: (t[2]), reverse = True))

print('三維 串列')
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

print('印出三維 串列')
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

person_data.reverse()   # 顛倒排序串列
print(type(person_data))
print(person_data)

print(len(person_data))

print('提取 前n筆資料, 組成一個二維 串列')
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


#取第一欄出來 成一個 串列 ??


print('串列 之使用')


print('------------------------------------------------------------')	#60個

data = list()
for page in range(1, 6):
    pdate = 'aaaa'
    title = 'bbbb'
    link = 'cccc'
    data.append((pdate, link, title))
print(type(data))
print(data)

print('------------------------------------------------------------')	#60個


contents = list()

for page in range(1, 6):
    content = dict()
    content['link'] = 'aaaaa'
    content['content'] = 'bbbbb'
    content['date'] = 'ccccc'
    content['title'] = 'ddddd'
    contents.append(content)
    
print(contents)

print('------------------------------------------------------------')	#60個




# 一個 串列 裡面每個元件都是 dictionary

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

"""
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
"""


print('------------------------------------------------------------')	#60個


print('串列 llll SP------------------------------------------------------------')	#60個



print('元組 tttt ST------------------------------------------------------------')	#60個



print('元組')
animals = ('鼠', '牛', '虎', '兔', '龍')
print(type(animals))
print(len(animals))
print(animals)

#animals[1] = '豬'  XXXX

print(animals[1])
print(animals[1:3])

print(animals.count('虎'))
print(animals.index('虎'))




#tuple 範例

print('------------------------------------------------------------')	#60個
animal = ('鼠', '牛', '虎', '兔', '龍')    # 定義元組元素是字串
print(animal[1:3])
print(animal[:2])
print(animal[1:])
print(animal[-2:])
print(animal[0:5:2])
      
print('------------------------------------------------------------')	#60個

animal = ('鼠', '牛', '虎', '兔', '龍')    # 定義元組元素是字串
print("animal元組長度是 %d " % len(animal))
for i in range(len(animal)):
    print(animal[i])    # 列印元組animal[i]

print('------------------------------------------------------------')	#60個

animal = ('鼠', '牛', '虎', '兔', '龍')    # 定義元組元素是字串
print("原始animal元組元素")
for animal_name in animal:
    print(animal_name)

print('------------------------------------------------------------')	#60個

tuple_animal = ('鼠', '牛', '虎', '兔', '龍')    # 定義元組元素是字串
list_animal = list(tuple_animal)              # 將元組改為串列
list_animal.append('蛇')          # 增加元素
print("列印元組", tuple_animal)
print("列印串列", list_animal)

print('------------------------------------------------------------')	#60個

animal = ('鼠', '牛', '虎', '兔', '龍')    # 定義元組元素是字串

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

print('建立一個 元組')
animal_tuple1 = ('鼠', '牛', '虎', '兔', '龍')
print(animal_tuple1)

print('建立一個 串列')
animal_list = [11, 22, 33, 44, 55, 66, 77, 88]

print('串列 轉 元組')
animal_tuple2 = tuple(animal_list)
print(animal_tuple2)

print("length is", len(animal_tuple2)) # Use function len
print("max is", max(animal_tuple2)) # Use max
print("min is", min(animal_tuple2)) # Use min
#print("sum is", sum(animal_tuple2)) # Use sum fail in kilo

print("The first element is", animal_tuple2[0]) # Use indexer

animal_tuple3 = animal_tuple1 + animal_tuple2 # Combine 2 tuples
print(animal_tuple3)

animal_tuple3 = 2 * animal_tuple1 # Multiple a tuple
print(animal_tuple3)

print(animal_tuple2[2 : 4]) # Slicing operator
print(animal_tuple1[-1])

print(55 in animal_tuple2) # in operator

for v in animal_tuple1:
    print(v, end = " ")
print()

print('元組 轉 串列')
animal_list = list(animal_tuple2)
animal_list.sort()
animal_tuple4 = tuple(animal_list)
animal_tuple5 = tuple(animal_list)
print(animal_tuple4)
print(animal_tuple4 == animal_tuple5) # Compare two tuples 

print('元組 tttt SP------------------------------------------------------------')	#60個

print('各種容器轉換 比較 ST------------------------------------------------------------')	#60個

animals1 = ['鼠', '牛', '虎', '兔', '龍']
print('串列 轉 集合')
x = set(animals1)                # 將串列轉成集合
print('集合 轉 串列')
animals2 = list(x)               # 將集合轉成串列

print('------------------------------------------------------------')	#60個

animals1 = ['鼠', '牛', '虎', '兔', '龍']
print('串列 轉 集合')
x = set(animals1)                # 將串列轉成集合
print('串列 轉 集合')
animals2 = list(x)               # 將集合轉成串列

print("原先串列資料animals1 = ", animals1)
print("新的串列資料animals2 = ", animals2)


print('------------------------------------------------------------')	#60個

list_animal = ['鼠', '牛', '虎', '兔', '龍']      # 定義串列元素是字串
print('串列 轉 元組')
tuple_animal = tuple(list_animal)            # 將串列改為元組
print("列印串列", list_animal)
print("列印元組", tuple_animal)

#tuple禁止使用append
#tuple_animal.append('elephant')         # 增加元素 --- 錯誤錯誤

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



print('------------------------------------------------------------')	#60個

print('將英文字串的每一個字母(含空白標點)拆成每個字一個集合, 大小寫不同')

animals_set = set('Mouse Ox Tiger Rabbit')
print(type(animals_set))
print(animals_set)

text = 'United States'
alphabetCount = {alphabet:text.count(alphabet) for alphabet in text}
print(alphabetCount)

text = 'United States'
alphabetCount = {alphabet:text.count(alphabet) for alphabet in set(text)}
print(alphabetCount)

print('------------------------------------------------------------')	#60個

print('集合 的方法 1')
fruits = set("orange")
print(type(fruits))
print("字元a是屬於fruits集合?", 'a' in fruits)
print("字元d是屬於fruits集合?", 'd' in fruits)

print('集合 的方法 2')
cars = {"Nissan", "Toyota", "Ford"}
print(type(cars))

boolean = "Ford" in cars
print("Ford in cars", boolean)
boolean = "Audi" in cars
print("Audi in cars", boolean)

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

print('字典範例 _size_factors')
_size_factors = {
    "kb": 1000, "mb": 1000 * 1000, "gb": 1000 * 1000 * 1000,
    "kib": 1024, "mib": 1024 * 1024, "gib": 1024 * 1024 * 1024,
}

print(type(_size_factors))

for aaa in _size_factors:
    print(aaa, _size_factors[aaa])


print('------------------------------------------------------------')	#60個

print('字典範例 _deprecations')
_deprecations = {
    "JPEGBaseline": "JPEGBaseline8Bit",
    "JPEGExtended": "JPEGExtended12Bit",
    "JPEGLossless": "JPEGLosslessSV1",
    "JPEGLSLossy": "JPEGLSNearLossless",
    "JPEG2000MultiComponentLossless": "JPEG2000MCLossless",
    "JPEG2000MultiComponent": "JPEG2000MC",
}

print(type(_deprecations))

for name in _deprecations:
    print(name)

print('------------------------------------------------------------')	#60個

import os, string

print('字典範例 encoding')
codecs = {
    'cn': ('gb2312', 'gbk', 'gb18030', 'hz'),
    'tw': ('big5', 'cp950'),
    'hk': ('big5hkscs',),
    'jp': ('cp932', 'shift_jis', 'euc_jp', 'euc_jisx0213', 'shift_jisx0213',
           'euc_jis_2004', 'shift_jis_2004'),
    'kr': ('cp949', 'euc_kr', 'johab'),
    'iso2022': ('iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2',
                'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
                'iso2022_kr'),
}

print(type(codecs))
print(codecs)

for loc, encodings in codecs.items():
    for enc in encodings:
        print(enc)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



"""

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

#list排序

import SelectionSort 

lst = [3, 4, 1, 2, 0]
SelectionSort.selectionSort(lst)

添加資料(append)
插入資料(insert)

合併資料(extend)
使用 extend() 將兩個List合併在一起，就像字串的Concatenation。
"""

print('------------------------------------------------------------')	#60個


#設定一個二維串列
money = [[41.36, 28.96, 3.77, 8.45],
[29.08, 3.58, 6.81, 0.77],
[15.68, 12.76, 3.79, 3.29],
[15.61, 10.93, 3.28, 2.95],
[11.27, 8.89, 10.22, 1.00],
[23.20, 2.26, 4.22, 0.58],
[11.28, 9.14, 6.50, 2.88],
[13.96, 9.18, 2.93, 2.84],
[14.44, 6.94, 4.70, 2.24],
[26.93, 0.63, 0.28, 0.47],
[9.05, 10.95, 1.93, 2.74],
[9.71, 7.47, 4.13, 1.90],
[9.00, 6.18, 7.20, 0.71],
[8.92, 8.03, 3.60, 2.15],
[15.00, 4.89, 0.24, 1.69],
[9.01, 8.49, 2.53, 1.77],
[7.02, 9.09, 0.98, 3.96],
[9.43, 0.40, 0.41, 10.57],
[12.78, 3.75, 3.54, 0.55]]
print(type(money))

print('------------------------------------------------------------')	#60個

print('List的用法')
list1 = []
list1.append(123)
list1.append(456)
list1.append(234)
list1.append(321)
list1.append(101)
#list1.pop()
"""
print('共輸入 %d 個數' % len(list1))
print('最大：%d' % max(list1))
print('最小：%d' % min(list1))
print('總和：%d' % sum(list1))
print('由大到小排序為：{}'.format(sorted(list1, reverse = True)))
"""

print('------------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎', '兔']
print(type(animals))
print(animals)
for animal in animals:
    print('找到動物 ' + animal)

print('------------------------------------------------------------')	#60個

#set   集合 ssss 大括號 {} 無順序 不可重複 set元素具有唯一性

animals = { '鼠', '牛', '虎'}
print(type(animals))
print(animals)
# 增加一般元素
animals.add('兔')
print('animals集合內容 ', animals)
# 增加已有元素並觀察執行結果
animals.add('牛')
print('animals集合內容 ', animals)

print(type(animals))

print('------------------------------------------------------------')	#60個

print('數字集合')
A = {n for n in range(1,20,2)}
print(type(A))
print(A)

print('------------------------------------------------------------')	#60個





print('---- zip() --------------------------------------------------------')	#60個

animals = ['鼠', '牛', '虎']   #list
weights = [3, 48, 33]   #list
#把兩個[串列] zip 起來
zipData = zip(animals, weights)                 # 執行zip
print('zipData資料類型', type(zipData))     # 列印zip資料類型
animal_list = list(zipData)                      # 將zip資料轉成串列
print('animal_list 資料類型', type(animal_list))      # 列印animal_list資料類型
print(animal_list)                               # 列印串列

print('animal_list[0] 資料類型', type(animal_list[0]))      # 列印animal_list資料類型
print('animal_list[1] 資料類型', type(animal_list[1]))      # 列印animal_list資料類型
print('animal_list[2] 資料類型', type(animal_list[2]))      # 列印animal_list資料類型

for name, weight in animal_list:
    print('{} 的體重是 {}'.format(name, weight))


print('------------------------------------------------------------')	#60個

b = list('子丑寅卯辰巳午未申酉戌亥')    #list
c = list('鼠牛虎兔龍蛇馬羊猴雞狗豬')    #list

#把兩個[串列] zip 起來
zipData = zip(b, c)                 # 執行zip

print(zipData)
for item in zipData:
    print(item)

print([item for item in zip(b, c)])

print('------------------------------------------------------------')	#60個

a = list('甲乙丙丁戊己庚辛壬癸'*6)
b = list('子丑寅卯辰巳午未申酉戌亥'*5)
years = list(zip(a, b))
print(type(years))
print(len(years))
print(years)

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


print('---- map --------------------------------------------------------')	#60個


print('map 的用法')
def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
print(type(alist))
print(type(choices))

for choice in choices:
    print(choice)

print('------------------------------------------------------------')	#60個
   


