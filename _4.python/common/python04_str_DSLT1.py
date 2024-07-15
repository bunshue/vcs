import sys


"""
各種python專用的語法 字典 串列 元組 集合 DSLT

字 dict  字典 dddd 大括號 {} 無順序 不可重複 = 集合 + list  d = {"key :value", "key :value", ...}
集 set   集合 ssss 大括號 {} 無順序 不可重複 set元素具有唯一性
串 lsit  串列 llll 中括號 [] 有順序 允許重複 list中的data type不用一致
元 tuple 元組 tttt 小括號 () 有順序 允許重複 不可變清單	常數list

Collections總整理
Collections(容器)
Python提供四種Collections，分別是Dictionary、Set、List、Tuple，
每個Collection都有各自的特色和使用時機，下面這些不用背起來，經常使用自然就會習慣了。

    字典(Dict)：無序且未索引的容器，沒有重複的成員，資料格式為key: value。
    集合(Set)：無序且未索引的容器，沒有重複的成員。
    列表(List)：有序且可更改的容器，允許重複的成員。
    組合(Tuple)：有序且不可更改的容器，允許重複的成員。

Dictionary(字典)
Dictionary是無序、沒有索引值且沒有重複的成員的容器，Pair的語法是key: value，一個key對應一個value，key不一定要是字串，但必須是唯一的。

"""

print("建立空容器")

print("建立一個空字典")
animals = dict()
animals = {}

print("建立一個空集合")
animals = set()
animals = set()

print("建立一個空串列")
animals = []

print("建立一個空元組")

print("字典 dddd ST------------------------------------------------------------")  # 60個

print("建立空字典")
animal = {}
print("空字典", animal)

print("建立字典")

animal = {
    "mouse": "鼠",
    "ox": "牛",
    "tiger": "虎",
    "rabbit": "兔",
}

print("增加字典內容")  # 只要給新的key就會產生新的資料。
animal["dragon"] = "龍"
animal["snake"] = "蛇"
animal["horse"] = "馬"
animal["goat"] = "羊"

print("刪除字典內容")
del animal["snake"]

# 移除dictionary
# 使用pop(key)移除該key值的資料。
# animal.pop('snake')

# 語法是dict[key]，利用key來存取數量。dict[key] = value就可以改變數量。
print(animal["dragon"])

print("測試字典的各種方法")

# 完整的動物字典
animals = {
    "mouse": "鼠",
    "ox": "牛",
    "tiger": "虎",
    "rabbit": "兔",
    "dragon": "龍",
    "snake": "蛇",
    "horse": "馬",
    "goat": "羊",
    "monkey": "猴",
    "chicken": "雞",
    "dog": "狗",
    "pig": "豬",
}


print("直接打印字典內容")
print(animals)
print("資料長度 :", len(animals), "筆")
print("字典裡內容一一列出")
for ani in animals:
    print(ani + ": " + animals[ani])

ename = "chicken"
cname = animals.get(ename)
if cname == None:
    print("沒有 " + ename + " 動物")
else:
    print("找到動物" + ename + ", 中文為 :" + animals[ename])

""" get 測試
animals = {"鼠": 3, "牛": 48}
ret_value1 = animals.get("牛")
print("Value = ", ret_value1)
ret_value2 = animals.get("虎")
print("Value = ", ret_value2)
ret_value3 = animals.get("虎", 10)
print("Value = ", ret_value3)
print("animals字典 :")
print(animals)
"""

print("------------------------------------------------------------")  # 60個

# 取得所有資料
# 使用keys()取得所有key值，回傳是所有key的List。
print("取得 keys")
cc = animals.keys()
print(cc)
print("資料長度 :", len(cc), "筆")
for ename in animals.keys():
    print(f"{ename},{animals[ename]}")

# 取得所有數值
# 使用values()取得所有value值，回傳是所有value的List。
print("取得 values")
cc = animals.values()
print(cc)
print("資料長度 :", len(cc), "筆")
for ani in animals.values():
    print(ani)

print("keys() values() 使用範例")
listkey = list(animals.keys())
listvalue = list(animals.values())

for i in range(len(listkey)):
    print("英文 : %s, 中文 : %s" % (listkey[i], listvalue[i]))

# 取得所有資料
# 使用item()取得所有資料組，回傳是由(key, value)所組成的List。
print("取得 items")
cc = animals.items()
print(cc)
print("資料長度 :", len(cc), "筆")
for ename, cname in animals.items():
    print("{:15s}{:15s}".format(ename, cname))
    # print("英文 : %s, 中文 : %s" % (ename, cname))


print("排序")
print(sorted(animals))

print("排序再顯示")
for ename in sorted(animals.keys()):
    print(f"{ename},{animals[ename]}")

print("排序 反相 再顯示")
for ename in sorted(animals.keys(), reverse=True):
    print(f"{ename},{animals[ename]}")


animal_name = "dragon"
if animal_name in animals:
    print("有此動物 :", animal_name, "=>", animals[animal_name])
else:
    print("查無此動物 :", animal_name)

animal_name = "dinosour"
if animal_name in animals:
    print("有此動物 :", animal_name, "=>", animals[animal_name])
else:
    print("查無此動物 :", animal_name)

print("目前字典元素數量     = ", len(animals))

animals.clear()

print("目前字典內容:", animals)
print("目前字典元素數量     = ", len(animals))

print("------------------------------------------------------------")  # 60個

print("建立內含{字典}的{字典}")
animals = {
    "鼠": {"特性1": "生性樂觀", "特性2": "適應力強", "特性3": "坐言起行"},
    "牛": {"特性1": "思想細密", "特性2": "目標清晰", "特性3": "老實可靠", "特性4": "活潑機智", "特性5": "永不言倦"},
}

print(type(animals))
print(animals)

# 列印字典元素個數
print("animals字典元素個數   :", len(animals))
print("animals['鼠']元素個數 :", len(animals["鼠"]))
print("animals['牛']元素個數 :", len(animals["牛"]))

print("------------------------------------------------------------")  # 60個

print("字典的用法")

# 完整的動物字典
animals = {
    "mouse": "鼠",
    "ox": "牛",
    "tiger": "虎",
    "rabbit": "兔",
    "dragon": "龍",
    "snake": "蛇",
    "horse": "馬",
    "goat": "羊",
    "monkey": "猴",
    "chicken": "雞",
    "dog": "狗",
    "pig": "豬",
}

print("刪除某一項 snake")
animals.pop("snake")
print(animals)

print("------------------------------------------------------------")  # 60個

print("建立內含{集合}的{字典}")

print("字典範例")

animals = {
    "鼠": {"生性樂觀", "適應力強", "坐言起行"},
    "牛": {"思想細密", "目標清晰", "老實可靠", "活潑機智", "永不言倦"},
    "虎": {"胸懷大志", "生性獨立", "著重行動", "挑戰自己"},
    "兔": {"性情溫馴", "挑戰自己", "坐言起行", "頭腦清晰"},
    "龍": {"積極進取", "胸懷大志", "行動敏捷", "性情溫馴"},
    "蛇": {"才智非凡", "永不言倦", "情感豐富"},
    "馬": {"活潑機智", "積極進取", "目標清晰", "積極進取"},
    "羊": {"心思慎密", "溫柔體貼", "永不言倦", "有第六感", "挑戰自己"},
    "猴": {"有幽默感", "頭腦清晰", "思考周詳", "行動敏捷", "生性獨立"},
    "雞": {"思想細密", "頭腦靈活", "胸懷大志", "永不言倦", "有第六感", "性情溫馴", "適應力強"},
    "狗": {"坐言起行", "直覺敏銳", "生性樂觀", "尊師重道", "直覺敏銳", ""},
    "豬": {"活潑機智", "生性獨立", "適應力強", "性情溫馴"},
}

# print(type(animals))
# print(animals)
# print(type(animals['牛']))
# print(animals['牛'])

print("含有 適應力強 的動物 :")
for name, character in animals.items():
    if "適應力強" in character:
        print(name)

print("含有 適應力強 但是不含 生性樂觀 的動物 : ")
for name, character in animals.items():
    if "適應力強" in character and not ("生性樂觀" in character):
        print(name)

print("------------------------------------------------------------")  # 60個

print("建立內含{字典}的{字典}")
animals = {
    "鼠": {"cname": "鼠", "ename": "mouse", "weight": "3"},
    "牛": {"cname": "牛", "ename": "ox", "weight": "48"},
}

# 列印內含字典的字典
for animal, animal_info in animals.items():
    print("名稱 = ", animal)  # 列印鍵(key)
    cname = animal_info["cname"]
    ename = animal_info["ename"]
    print("中文名 :", cname)
    print("英文名 :", ename)
    print("體重       = {animal_info['weight']}")  # 列印值(value)

# 列印字典元素個數
print(f"animals字典元素個數       {len(animals)}")
print(f"animals['鼠']元素個數 {len(animals['鼠'])}")
print(f"animals['牛']元素個數  {len(animals['牛'])}")

print("------------------------------------------------------------")  # 60個

print("建立內含[串列]的{字典}")

animals = {
    "鼠": ["生性樂觀", "適應力強", "坐言起行"],
    "牛": ["思想細密", "目標清晰", "老實可靠", "活潑機智", "永不言倦"],
    "虎": ["胸懷大志", "生性獨立", "著重行動", "挑戰自己"],
}

print(type(animals))
print(animals)

# 列印key名字 + 字串'喜歡的運動'
for name, character in animals.items():
    print("動物 %s 的特性是 : " % name)
    # 列印value,這是串列
    for ch in character:
        print("   ", ch)

print("------------------------------------------------------------")  # 60個

print("建立內含{元組}的{字典}")

animals = {
    "鼠": ("mouse", 3),
    "牛": ("ox", 48),
    "虎": ("tiger", 33),
    "兔": ("rabbit", 8),
    "龍": ("dragon", 38),
    "蛇": ("snake", 16),
    "馬": ("horse", 31),
    "羊": ("goat", 29),
    "猴": ("monkey", 22),
    "雞": ("chicken", 6),
    "狗": ("dog", 12),
    "豬": ("pig", 42),
}

animals["象"] = ("elephant", 100)

print(type(animals["象"]))
print(animals["象"])

print(type(animals))
print(animals)
print(animals["龍"])

print("預設排序")
for key in animals:
    print("{}:{}".format(key, animals[key]))

print("依英文名稱排序")
ani = sorted(animals.items(), key=lambda item: item[1][0])
print("中文名稱", "        英文名稱 ", " 體重")
for i in range(len(ani)):
    print(f"{ani[i][0]:8s}{ani[i][1][0]:10s}{ani[i][1][1]:8d}")

print("依體重排序")
ani = sorted(animals.items(), key=lambda item: item[1][1])
print("中文名稱", "        英文名稱 ", " 體重")
for i in range(len(ani)):
    print(f"{ani[i][0]:8s}{ani[i][1][0]:10s}{ani[i][1][1]:8d}")

print("------------------------------------------------------------")  # 60個

# key在字典內
animals = {"鼠": 3, "牛": 48}
ret_value = animals.setdefault("牛")
print("Value = ", ret_value)
print("animals字典", animals)
ret_value = animals.setdefault("牛", 100)
print("Value = ", ret_value)
print("animals字典 :")
print(animals)

print("------------------------------------------------------------")  # 60個

animal_mouse = {"name": "mouse"}
print("原先字典內容", animal_mouse)

# 'cname'鍵不存在
# cname = animal_mouse.setdefault('cname')    #未填入值
cname = animal_mouse.setdefault("cname", "鼠")  # 有填入值
print("增加cname鍵 ", animal_mouse)
print("cname = ", cname)

# 'weight'鍵不存在
weight = animal_mouse.setdefault("weight", 3)
print("增加weight鍵 ", animal_mouse)
print("weight = ", weight)

print("------------------------------------------------------------")  # 60個

song = """Are you sleeping, are you sleeping, Brother John, Brother John?
Morning bells are ringing, morning bells are ringing.
Ding ding dong, Ding ding dong."""
mydict = {}  # 空字典未來儲存單字計數結果
print("原始歌曲")
print(song)

# 以下是將歌曲大寫字母全部改成小寫
songLower = song.lower()  # 歌曲改為小寫
print("小寫歌曲")
print(songLower)

# 將歌曲的標點符號用空字元取代
for ch in songLower:
    if ch in ".,?":
        songLower = songLower.replace(ch, "")
print("不再有標點符號的歌曲")
print(songLower)

# 將歌曲字串轉成串列
songList = songLower.split()
print("以下是歌曲串列")
print(songList)  # 列印歌曲串列

# 將歌曲串列處理成字典
for wd in songList:
    if wd in mydict:  # 檢查此字是否已在字典內
        mydict[wd] += 1  # 累計出現次數
    else:
        mydict[wd] = 1  # 第一次出現的字建立此鍵與值

print("以下是最後執行結果")
print(mydict)  # 列印字典

print("------------------------------------------------------------")  # 60個

cname = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
ename = [
    "mouse",
    "ox",
    "tiger",
    "rabbit",
    "dragon",
    "snake",
    "horse",
    "goat",
    "monkey",
    "chicken",
    "dog",
    "pig",
]

print("將兩個串列編在一起組成字典")
name_dict = dict(zip(cname, ename))  # 建立字典

print("列印編碼字典\n", name_dict)  # 列印字典

msgTest = "鼠牛虎兔龍蛇馬羊猴雞狗豬"

cipher = []  # 串列
for i in msgTest:  # 執行每個字元加密
    v = name_dict[i]  # 加密
    cipher.append(v)  # 加密結果
ciphertext = "".join(cipher)  # 將串列轉成字串

print("原始字串 :", msgTest)
print("編碼字串 :", ciphertext)

print("------------------------------------------------------------")  # 60個

print("找字典內的value")

animal_dict = {
    "鼠": ("mouse", 3),
    "牛": ("ox", 48),
    "虎": ("tiger", 33),
    "兔": ("rabbit", 8),
    "龍": ("dragon", 38),
    "蛇": ("snake", 16),
    "馬": ("horse", 31),
    "羊": ("goat", 29),
    "猴": ("monkey", 22),
    "雞": ("chicken", 6),
    "狗": ("dog", 12),
    "豬": ("pig", 42),
}

print(type(animal_dict))

print("字串轉串列")
animal_string = "鼠牛虎兔龍蛇馬羊猴雞狗豬"
animal_list = list(animal_string)

print(type(animal_list))

print("從字典的key找到value")
for animal in animal_list:
    print("key = ", animal)
    print("value = ", animal_dict[animal])

print("------------------------------------------------------------")  # 60個

animals = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38}
animals = {"鼠": 3, "牛": 48, "虎": 33}
animals["兔"] = 8
animals["龍"] = 38
animals_item = animals.items()
for name, weight in animals_item:
    print("%s 的體重為 %d" % (name, weight))

animals = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38}
animals = {"鼠": 3, "牛": 48, "虎": 33}
animals["兔"] = 8
animals["龍"] = 38
animals_key = list(animals.keys())
animals_value = list(animals.values())
for i in range(len(animals_key)):
    print("%s 的體重為 %d" % (animals_key[i], animals_value[i]))

print("------------------------------------------------------------")  # 60個

print("dict使用範例")

class_101 = dict()  # 記錄學生座號及姓名
chi_score = dict()  # 記錄國文成績
eng_score = dict()  # 記錄英文成績
mat_score = dict()  # 記錄數學成績

subjects = ["國文", "英文", "數學"]  # 串列
scores = [chi_score, eng_score, mat_score]  # 3個字典組成的串列

class_101[1] = "牛"
class_101[2] = "虎"
class_101[4] = "龍"
class_101[8] = "猴"
print("現有動物 :", class_101)

print("國文成績")
subject_no = 0
scores[subject_no][1] = 80
scores[subject_no][2] = 85
scores[subject_no][4] = 78
scores[subject_no][8] = 88

print("顯示國文成績")
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print("英文成績")
subject_no = 1
scores[subject_no][1] = 84
scores[subject_no][2] = 79
scores[subject_no][4] = 92
scores[subject_no][8] = 82

print("顯示英文成績")
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print("數學成績")
subject_no = 2
scores[subject_no][1] = 85
scores[subject_no][2] = 91
scores[subject_no][4] = 84
scores[subject_no][8] = 77

print("顯示數學成績")
for no, name in class_101.items():
    print("{},{}的{}成績:".format(no, name, subjects[subject_no]), scores[subject_no][no])

print("顯示總成績")
for no in class_101.keys():
    print("{:<5}:".format(class_101[no]), end="")
    sum = 0
    for subject_no in range(0, 3):
        sum = sum + scores[subject_no][no]
        print("{}:{:>3} ".format(subjects[subject_no], scores[subject_no][no]), end="")
    print("總分:{:>3}, 平均:{:.2f}".format(sum, float(sum) / len(scores)))

print("------------------------------------------------------------")  # 60個

print("字典的用法")

animals = {
    "鼠": "mouse",
    "牛": "ox",
    "虎": "tiger",
}

print(type(animals))
print(animals)

for cname, ename in animals.items():
    name = "%s %s" % (cname, ename)
    print(name)

print("------------------------------------------------------------")  # 60個

print("字典的用法 _size_factors")
_size_factors = {
    "kb": 1000,
    "mb": 1000 * 1000,
    "gb": 1000 * 1000 * 1000,
    "kib": 1024,
    "mib": 1024 * 1024,
    "gib": 1024 * 1024 * 1024,
}

print(type(_size_factors))

for aaa in _size_factors:
    print(aaa, _size_factors[aaa])

print("------------------------------------------------------------")  # 60個

print("字典的用法 encoding")
print("字典裡面的values是tuple")
codecs = {
    "cn": ("gb2312", "gbk", "gb18030", "hz"),
    "tw": ("big5", "cp950"),
    "hk": ("big5hkscs"),
    "jp": ("cp932", "shift_jis", "euc_jp"),
    "kr": ("cp949", "euc_kr", "johab"),
}

print(type(codecs))
print(codecs)

print(type(codecs["kr"]))
print(codecs["kr"])

for loc, encodings in codecs.items():
    print()
    for enc in encodings:
        print(enc)

print("------------------------------------------------------------")  # 60個

print("字典的排序, 使用lambda")

animals = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38}
print(type(animals))
print(animals.items())
print(animals)

animals2 = sorted(animals.items(), key=lambda x: x[0])  # 依照key排序
print("依照名稱排序")
print(animals2)

animals3a = sorted(animals.items(), key=lambda x: x[1])  # 依照value排序
print("依照體重排序")
print(animals3a)

animals3b = sorted(animals.items(), key=lambda x: x[1], reverse=True)
print("依照體重排序")
print(animals3b)

print("字典的排序, 使用sort")
print(sorted(animals.items()))

for key, item in sorted(animals.items()):
    print(key, item)

print("------------------------------------------------------------")  # 60個

print("字典之合併: 使用 update")

animals = {"鼠": 3, "牛": 48, "虎": 33, "兔": 8, "龍": 38}
animal = {"name": "mouse", "class": "A", "weight": 3}

animal_new_data = {"name": "鼠", "weight": 5, "sports": "soccer"}

animal.update(animal_new_data)

print(animal)

print("------------------------------------------------------------")  # 60個

print("字典之合併: 使用 聯集算符")

animal = {"name": "mouse", "class": "A", "weight": 3}

animal_new_data = {"name": "鼠", "weight": 5, "sports": "soccer"}
""" fail in kilo
new_setting = animal | animal_new_data

print(new_setting)

animal |= animal_new_data

print(animal)
"""
print("------------------------------------------------------------")  # 60個

print("字典之合併: 使用 多重解包")

animal = {"name": "mouse", "class": "A", "weight": 3}

animal_new_data = {"name": "鼠", "weight": 5, "sports": "soccer"}

new_setting = {**animal, **animal_new_data}

print(new_setting)

print("------------------------------------------------------------")  # 60個

print("字典之合併: 使用 dict() 與 **")

animal = {"name": "mouse", "class": "A", "weight": 3}

animal_new_data = {"name": "鼠", "weight": 5, "sports": "soccer"}

new_setting = dict(animal, **animal_new_data)

print(new_setting)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("字典 dddd SP------------------------------------------------------------")  # 60個


print("串列 llll ST------------------------------------------------------------")  # 60個

print("一維 串列")

print("建立串列")

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

print("原串列 :", animals)
print("串列 增加項目")
animals.append("蛇")
animals.append("蛇")
animals.append("蛇")
new_animals = ["馬", "羊"]  # 串列
animals = animals + new_animals
print("新串列 :", animals)
print("改變第1項的值")
animals[1] = "豬"
print(animals)

print("在第1項的位置安插一個項目")
print("原串列 :", animals)
animals.insert(1, "猴")
print("新串列 :", animals)

print("牛 是否在 串列 裏?", "牛" in animals)
print("豬 是否在 串列 裏?", "豬" in animals)

print("一維 串列")
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列

print("一一取出 串列 內的值")
for ani in animals:
    print(ani)

print("直接印出 串列")
print(animals)

print("顛倒排序串列")
animals.reverse()  # 顛倒排序串列
print(animals)

# 建立一個長度N的布林陣列 都放著 False
N = 10
animal_list = N * [False]
print(animal_list)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print("目前animals串列 :", animals)
animals.append("蛇")
print("目前animals串列 :", animals)
animals.insert(3, "馬")
print("目前animals串列 :", animals)
animals.remove("虎")
print("目前animals串列 :", animals)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print("目前animals串列 :", animals)

for ani in animals[:]:
    animals.remove(ani)
    print(f"刪除 {ani}")
    print("目前animals串列 :", animals)

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print("型態 :", type(animals))
print("長度 :", len(animals))
print("原串列 :", animals)
print("列印全部項目")
print(animals)
print("列印前3個")
print(animals[:3])
print("列印 第1到第4個(不含)")
print(animals[1:4])
print("列印 第3個(含)以後")
print(animals[3:])
print("第1項  :", animals[1])
print("最後1項 :", animals[-1])  ##如果索引值是負的，則代表倒數第幾個。
print("第1~3項 :", animals[1:4], "\t要用[1:4]")  # [n:m] 表示從n取到m-1，返回一個新的List。

print(animals[3])
print(animals[-1])
print(animals[1:4])
print(animals[3:])
print(animals[:5])
print(animals[:-2])

# 測試list之最後5筆資料
print(animals[-3:])

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print(animals)

animals_partial = animals[2:]  # 第二項(含)以後的
print(animals_partial)

# count() 計算次數
print("虎 出現的次數 :")
print(animals.count("虎"))

# index() 搜尋
print("虎 出現的索引位置 :")
print(animals.index("虎"))

#print("象 出現的索引位置 :") # 出現錯誤
#print(animals.index("象"))

sys.exit()

print("------------------------------------------------------------")  # 60個

print("字串 轉 串列")
animal_list = list("鼠牛虎兔龍蛇馬羊猴雞狗豬")
print(type(animal_list))
print(animal_list)

print("字串 轉 串列")
s = list("0912345678")

numbers = list()

for c in s:
    numbers.append(int(c))

print(type(numbers))
print(numbers)

print("------------------------------------------------------------")  # 60個

print("串列 使用")
animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print(type(animals))

print("列印全部項目")
print(animals)

print("列印排序後的結果")
animal_sorted = sorted(animals)
print(animal_sorted)

print("------------------------------------------------------------")  # 60個

print("串列 操作, 建立內含元組的串列")
animals = [
    ("mouse", "鼠", 3),
    ("ox", "牛", 48),
    ("tiger", "虎", 33),
    ("rabbit", "兔", 8),
    ("dragon", "龍", 38),
    ("snake", "蛇", 16),
    ("horse", "馬", 31),
    ("goat", "羊", 29),
    ("monkey", "猴", 22),
    ("chicken", "雞", 6),
    ("dog", "狗", 12),
    ("pig", "豬", 42),
]
print(type(animals))
print(animals)

print("------------------------------------------------------------")  # 60個

print("串列 操作, 建立內含串列的串列")
animals = [["鼠", 3], ["牛", 48], ["虎", 33]]
print(type(animals))
print(animals)

animals.sort(key=lambda x: x[1])
print(animals)

print("-------------")
print("串列 操作, 建立內含串列的串列")
animals = [["鼠", 3], ["牛", 48], ["虎", 33]]
print(type(animals))
print(animals)

animals1 = sorted(animals, key=lambda x: x[1])
print(type(animals1))
print(animals1)

print("------------------------------------------------------------")  # 60個

print("依英文名字數長短排序")


def compare_num_of_chars(string1):
    return len(string1)


animals = [
    "mouse",
    "ox",
    "tiger",
    "rabbit",
    "dragon",
    "snake",
    "horse",
    "goat",
    "monkey",
    "chicken",
    "dog",
    "pig",
]
animals.sort(key=compare_num_of_chars)
print(animals)

print("------------------------------------------------------------")  # 60個

print("二維 串列")

animal_list = list()
#         id_num, name, weight
animal_list.append((1, "鼠", 3))  # 裡面用()包起來的, 是一個tuple
animal_list.append((2, "牛", 48))
animal_list.append((3, "虎", 33))
animal_list.append((4, "兔", 8))
animal_list.append((5, "龍", 38))
print(animal_list)

animal1 = [5, "龍", 38]  # 一維 串列
animal2 = [1, "鼠", 3]
animal3 = [4, "兔", 8]
animal4 = [2, "牛", 48]
animal5 = [3, "虎", 33]

# 用5個一維 串列 組成一個2維 串列
animal_list = list()
animal_list = [animal1, animal2, animal3, animal4, animal5]
print(animal_list)

print("二維 串列 排序 依第0項排序")
animal_list.sort(key=lambda e: (e[0]))
print(animal_list)

print("二維 串列 排序 依第1項排序")
animal_list.sort(key=lambda e: (e[1]))
print(animal_list)

print("二維 串列 排序 依第2項排序, 並反相")
print(sorted(animal_list, key=lambda t: (t[2]), reverse=True))

print("三維 串列")
dates = [
    [[1, 3, 5, 7], [9, 11, 13, 15], [17, 19, 21, 23], [25, 27, 29, 31]],
    [[2, 3, 6, 7], [10, 11, 14, 15], [18, 19, 22, 23], [26, 27, 30, 31]],
    [[4, 5, 6, 7], [12, 13, 14, 15], [20, 21, 22, 23], [28, 29, 30, 31]],
    [[8, 9, 10, 11], [12, 13, 14, 15], [24, 25, 26, 27], [28, 29, 30, 31]],
    [[16, 17, 18, 19], [20, 21, 22, 23], [24, 25, 26, 27], [28, 29, 30, 31]],
]

print(type(dates))
print(len(dates))
print("直接印出 此 三維 串列")
print(dates)

print("用迴圈印出 此 三維 串列")
for i in range(5):
    for j in range(4):
        for k in range(4):
            print(format(dates[i][j][k], "4d"), end=" ")
        print()

print("------------------------------------------------------------")  # 60個

print("二維 串列, 裡面都是list")

animal_list = [
    [1, "鼠", "mouse", 3],
    [2, "牛", "ox", 48],
    [3, "虎", "tiger", 33],
    [4, "兔", "rabbit", 8],
    [5, "龍", "dragon", 38],
    [6, "蛇", "snake", 16],
    [7, "馬", "horse", 31],
    [8, "羊", "goat", 29],
    [9, "猴", "monkey", 22],
    [10, "雞", "chicken", 6],
    [11, "狗", "dog", 12],
    [12, "豬", "pig", 42],
]

print("二維 串列, 裡面都是tuple")

animal_list = [
    (1, "鼠", "mouse", 3),
    (2, "牛", "ox", 48),
    (3, "虎", "tiger", 33),
    (4, "兔", "rabbit", 8),
    (5, "龍", "dragon", 38),
    (6, "蛇", "snake", 16),
    (7, "馬", "horse", 31),
    (8, "羊", "goat", 29),
    (9, "猴", "monkey", 22),
    (10, "雞", "chicken", 7),
    (11, "狗", "dog", 12),
    (12, "豬", "pig", 42),
]

print("串列反相排列")
animal_list.reverse()  # 顛倒排序串列
print(type(animal_list))
print(animal_list)
print(len(animal_list))

print("提取 前n筆資料, 組成一個二維 串列")
print(type(animal_list[:5]))
print(animal_list[:5])
print("提取 第n筆資料, tuple")
print(type(animal_list[5]))
print(animal_list[5])

print("提取 從a開始到b, 間隔c")
a = 0
b = 5
c = 2
print(type(animal_list[a:b:c]))  # 串列
print(animal_list[a:b:c])

# 取第一欄出來 成一個 串列 ??

print("------------------------------------------------------------")  # 60個

print("串列, 建立內含元組的串列")

animals = list()
for i in range(1, 6):
    name = "鼠"
    ename = "mouse"
    weight = 3 + i
    tt = (name, ename, weight)  # 組合成一個元組
    animals.append(tt)

print(type(animals))
print(animals)

print("------------------------------------------------------------")  # 60個

print("串列, 建立內含字典的串列")

animals = list()
for i in range(1, 6):
    dd = dict()
    dd["name"] = "鼠"
    dd["ename"] = "mouse"
    dd["weight"] = 3 + i
    animals.append(dd)

print(type(animals))
print(animals)

print("------------------------------------------------------------")  # 60個

# 一個 串列 裡面每個元件都是 dictionary

price_data = [
    {"name": "112/03/13", "data": [{"name": "98 無鉛汽油", "y": 32.7, "GroupID": 7}]},
    {"name": "112/03/20", "data": [{"name": "98 無鉛汽油", "y": 32.4, "GroupID": 6}]},
    {"name": "112/03/27", "data": [{"name": "98 無鉛汽油", "y": 31.9, "GroupID": 5}]},
    {"name": "112/04/03", "data": [{"name": "98 無鉛汽油", "y": 32.4, "GroupID": 4}]},
    {"name": "112/04/10", "data": [{"name": "98 無鉛汽油", "y": 33.0, "GroupID": 3}]},
    {"name": "112/04/17", "data": [{"name": "98 無鉛汽油", "y": 33.3, "GroupID": 2}]},
    {"name": "112/04/24", "data": [{"name": "98 無鉛汽油", "y": 33.1, "GroupID": 1}]},
    {"name": "112/03/13", "data": [{"name": "95 無鉛汽油", "y": 30.7, "GroupID": 7}]},
    {"name": "112/03/20", "data": [{"name": "95 無鉛汽油", "y": 30.4, "GroupID": 6}]},
    {"name": "112/03/27", "data": [{"name": "95 無鉛汽油", "y": 29.9, "GroupID": 5}]},
]

print("資料型態 :\t", type(price_data))
print("資料長度 :\t", len(price_data))
print("資料內容")
for info in price_data:
    print(type(info))
    print(info)
    print("日期:", info["name"])
    # print(info['data'])
    for infos in info["data"]:
        print(type(infos))
        print(infos)
        print("油品:", infos["name"])
        print("價格:", infos["y"])

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


print("------------------------------------------------------------")  # 60個


print("串列 llll SP------------------------------------------------------------")  # 60個


print("元組 tttt ST------------------------------------------------------------")  # 60個

print("元組")
animals = ("鼠", "牛", "虎", "兔", "龍")
print(type(animals))
print(len(animals))
print(animals)

# animals[1] = '豬'  XXXX

print("第1號動物 :")
print(animals[1])
print("第1~3號動物 :")
print(animals[1:3])

print("虎 出現的次數 :")
print(animals.count("虎"))
print("虎 出現的索引位置 :")
print(animals.index("虎"))

print("------------------------------------------------------------")  # 60個

animal = ("鼠", "牛", "虎", "兔", "龍")  # 定義元組元素是字串
print(animal[1:3])
print(animal[:2])
print(animal[1:])
print(animal[-2:])
print(animal[0:5:2])

print("------------------------------------------------------------")  # 60個

animal = ("鼠", "牛", "虎", "兔", "龍")  # 定義元組元素是字串
print("animal元組長度是 %d " % len(animal))
for i in range(len(animal)):
    print(animal[i])  # 列印元組animal[i]

print("------------------------------------------------------------")  # 60個

animal = ("鼠", "牛", "虎", "兔", "龍")  # 定義元組元素是字串
print("原始animal元組元素")
for animal_name in animal:
    print(animal_name)

print("------------------------------------------------------------")  # 60個

animal_tuple = ("鼠", "牛", "虎", "兔", "龍")  # 定義元組元素是字串
animal_list = list(animal_tuple)  # 將元組改為串列
animal_list.append("蛇")  # 增加元素
print("列印元組", animal_tuple)
print("列印串列", animal_list)

print("------------------------------------------------------------")  # 60個

animal = ("鼠", "牛", "虎", "兔", "龍")  # 定義元組元素是字串

print("animal最大值是", max(animal))
print("animal最小值是", min(animal))

print("------------------------------------------------------------")  # 60個

print("建立一個 元組")
animal_tuple1 = ("鼠", "牛", "虎", "兔", "龍")
print(animal_tuple1)

print("建立一個 串列")
animal_list = [11, 22, 33, 44, 55, 66, 77, 88]

print("串列 轉 元組")
animal_tuple2 = tuple(animal_list)
print(animal_tuple2)

print("length is", len(animal_tuple2))  # Use function len
print("max is", max(animal_tuple2))  # Use max
print("min is", min(animal_tuple2))  # Use min
# print("sum is", sum(animal_tuple2)) # Use sum fail in kilo

print("The first element is", animal_tuple2[0])  # Use indexer

animal_tuple3 = animal_tuple1 + animal_tuple2  # Combine 2 tuples
print(animal_tuple3)

animal_tuple3 = 2 * animal_tuple1  # Multiple a tuple
print(animal_tuple3)

print(animal_tuple2[2:4])  # Slicing operator
print(animal_tuple1[-1])

print(55 in animal_tuple2)  # in operator

for v in animal_tuple1:
    print(v, end=" ")
print()

print("元組 轉 串列")
animal_list = list(animal_tuple2)
animal_list.sort()
animal_tuple4 = tuple(animal_list)
animal_tuple5 = tuple(animal_list)
print(animal_tuple4)
print(animal_tuple4 == animal_tuple5)  # Compare two tuples

print("元組 tttt SP------------------------------------------------------------")  # 60個


print("集合 ssss ST------------------------------------------------------------")  # 60個

print("集合的運算")

# 大動物 : [牛虎龍馬豬][羊猴][象] 8
# 小動物 : [鼠兔蛇雞狗][羊猴][龜] 8

print("建立集合")
big_animal = set()  # 宣告集合
big_animal = {"牛", "虎", "龍", "馬", "豬", "羊", "猴", "象"}

small_animal = set()  # 宣告集合
small_animal = set(["鼠", "兔", "蛇", "雞", "狗", "羊", "猴", "龜"])  # 由串列轉集合

print("大動物 :", big_animal)
print("小動物 :", small_animal)


print("交集 Set Intersection :")
animal = big_animal & small_animal
print(animal)
animal = big_animal.intersection(small_animal)
print(animal)

print("聯集 Set Union :")
animal = big_animal | small_animal
print(animal)
animal = big_animal.union(small_animal)
print(animal)

print("差集 Set Difference(大-小) :")
animal = big_animal - small_animal
print(animal)
animal = big_animal.difference(small_animal)
print(animal)

print("差集 Set Difference(小-大) :")
animal = small_animal - big_animal
print(animal)
animal = small_animal.difference(big_animal)
print(animal)

print("對稱差集 Set Symmetric Difference :")
animal = big_animal ^ small_animal
print(animal)
animal = big_animal.symmetric_difference(small_animal)
print(animal)

print("------------------------------------------------------------")  # 60個

# 大動物 : [牛虎龍馬豬][羊猴][象] 8
# 小動物 : [鼠兔蛇雞狗][羊猴][龜] 8

print("建立集合")
big_animal = set()  # 宣告集合
big_animal = {"牛", "虎", "龍", "馬", "馬", "馬"}

small_animal = set()  # 宣告集合
small_animal = set(["鼠", "兔", "蛇", "雞", "雞", "雞"])  # 由串列轉集合

print("大動物 :", big_animal)
print("小動物 :", small_animal)

print("在集合中新增元素")
big_animal.add("豬")
big_animal.add("羊")
big_animal.add("猴")
big_animal.add("象")

new_small_animals = {"狗", "羊", "猴", "龜"}
small_animal.update(new_small_animals)

print("大動物 :", big_animal)
print("小動物 :", small_animal)

print("在集合中刪除元素")
big_animal.discard("象")
small_animal.remove("龜")

print("大動物 :", big_animal)
print("小動物 :", small_animal)

print("比較兩集合是否相等")
print(big_animal == small_animal)

print("集合的成員運算子")
print("龍 是否在集合1之中?", "龍" in big_animal)
print("龍 是否在集合2之中?", "龍" in small_animal)

print("length is", len(big_animal))  # Use function len
print("max is", max(big_animal))  # Use max
print("min is", min(big_animal))  # Use min
# print("sum is", sum(big_animal)) # Use sum

print("在集合中刪除全部元素")
big_animal.clear()
small_animal.clear()

print("大動物 :", big_animal)
print("小動物 :", small_animal)

print("------------------------------------------------------------")  # 60個

print("字典子集")

animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
    "蛇": 16,
    "馬": 31,
    "羊": 29,
    "猴": 22,
    "雞": 6,
    "狗": 12,
    "豬": 42,
}

animals1 = {key: value for key, value in animals.items() if value > 30}
print("大於30公斤的動物 :", animals1)

protected_names = {"虎", "龍", "馬", "猴"}
animals2 = {key: value for key, value in animals.items() if key in protected_names}
print("保育類動物動物 :", animals2)

print("------------------------------------------------------------")  # 60個

animal_list = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print("原 串列")
print(animal_list)

print("串列 轉 集合")
animal_set = set(animal_list)
print(animal_set)

print("集合長度 :", len(animal_set))
print("最大 :", max(animal_set))
print("最小 :", min(animal_set))

print("集合 轉 串列")
animal_list = list(animal_set)
print(animal_list)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
# 將intersection( )應用在A集合
AB = A.intersection(B)  # A和B的交集
print("A和B的交集是 ", AB)
# 將intersection( )應用在B集合
BA = B.intersection(A)  # B和A的交集
print("B和A的交集是 ", BA)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
# 將union( )應用在A集合
AorB = A.union(B)  # A和B的聯集
print("A和B的聯集是 ", AorB)
# 將union( )應用在B集合
BorA = B.union(A)  # B和A的聯集
print("B和A的聯集是 ", BorA)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
# 將difference( )應用在A集合
A_B = A.difference(B)  # A-B的差集
print("A-B的差集是 ", A_B)
# 將difference( )應用在B集合
B_A = B.difference(A)  # B-A的差集
print("B-A的差集是 ", B_A)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
# 將symmetric_difference( )應用在A集合
A_sydi_B = A.symmetric_difference(B)  # A和B的對稱差集
print("A和B的對稱差集是 ", A_sydi_B)
# 將symmetric_difference( )應用在B集合
B_sydi_A = B.symmetric_difference(A)  # B和A的對稱差集
print("B和A的對稱差集是 ", B_sydi_A)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
C = {1, 2, 3, 4, 5}  # 定義集合C
# 列出A與B集合是否相等
print("A與B集合相等", A == B)
# 列出A與C集合是否相等
print("A與C集合相等", A == C)

print("------------------------------------------------------------")  # 60個

A = {1, 2, 3, 4, 5}  # 定義集合A
B = {3, 4, 5, 6, 7}  # 定義集合B
C = {1, 2, 3, 4, 5}  # 定義集合C
# 列出A與B集合是否相等
print("A與B集合不相等", A != B)
# 列出A與C集合是否不相等
print("A與C集合不相等", A != C)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("集合 ssss SP------------------------------------------------------------")  # 60個


print("各種容器轉換 比較 ST------------------------------------------------------------")  # 60個

animals1 = ["鼠", "牛", "虎", "兔", "龍"]
print("串列 轉 集合")
x = set(animals1)  # 將串列轉成集合
print("集合 轉 串列")
animals2 = list(x)  # 將集合轉成串列

print("------------------------------------------------------------")  # 60個

animals1 = ["鼠", "牛", "虎", "兔", "龍"]
print("串列 轉 集合")
x = set(animals1)  # 將串列轉成集合
print("串列 轉 集合")
animals2 = list(x)  # 將集合轉成串列

print("原先串列資料animals1 = ", animals1)
print("新的串列資料animals2 = ", animals2)

print("------------------------------------------------------------")  # 60個

animal_list = ["鼠", "牛", "虎", "兔", "龍"]  # 定義串列元素是字串
print("串列 轉 元組")
animal_tuple = tuple(animal_list)  # 將串列改為元組
print("列印串列 :", animal_list)
print("列印元組 :", animal_tuple)

# tuple禁止使用append
# animal_tuple.append('elephant')         # 增加元素 --- 錯誤錯誤

print("------------------------------------------------------------")  # 60個

import random
import time

print("set 和 list 速度比較")
NUMBER_OF_ELEMENTS = 15000

# Create a list
lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

# Create a set from the list
s = set(lst)

# Test if an element is in the set
startTime = time.time()  # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in s
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "To test if",
    NUMBER_OF_ELEMENTS,
    "elements are in the set\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

# Test if an element is in the list
startTime = time.time()  # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "\nTo test if",
    NUMBER_OF_ELEMENTS,
    "elements are in the list\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

# Remove elements from a set one at a time
startTime = time.time()  # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    s.remove(i)
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "\nTo remove",
    NUMBER_OF_ELEMENTS,
    "elements from the set\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

# Remove elements from a list one at a time
startTime = time.time()  # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    lst.remove(i)
endTime = time.time()  # Get end time
runTime = int((endTime - startTime) * 1000)  # Get test time
print(
    "\nTo remove",
    NUMBER_OF_ELEMENTS,
    "elements from the list\n",
    "The runtime is",
    runTime,
    "milliseconds",
)

print("各種容器轉換 比較 SP------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("將英文字串的每一個字母(含空白標點)拆成每個字一個集合, 大小寫不同")

print("字串 轉 集合")

animal_string = "Mouse Ox Tiger Rabbit"
animal_set = set(animal_string)
print(type(animal_set))
print(animal_set)

text = "United States"
alphabetCount = {alphabet: text.count(alphabet) for alphabet in text}
print(alphabetCount)

text = "United States"
alphabetCount = {alphabet: text.count(alphabet) for alphabet in set(text)}
print(alphabetCount)

print("------------------------------------------------------------")  # 60個

print("集合 的方法 1")
animals = set("鼠牛虎兔龍")
print(type(animals))
print("虎 是屬於animals集合?", "a" in animals)
print("羊 是屬於animals集合?", "d" in animals)

print("集合 的方法 2")
animals = {"鼠", "牛", "虎"}
print(type(animals))

boolean = "虎" in animals
print("虎 in animals ?", boolean)
boolean = "羊" in animals
print("羊 in animals ?", boolean)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


def draw_bar(n):
    return "*" * n


s = [2, 5, 4, 7, 5, 4]
for bar in map(draw_bar, s):
    print(bar)

print("------------------------------------------------------------")  # 60個

s = [2, 5, 4, 7, 5, 4]
for bar in map(lambda n: "*" * n, s):
    print(bar)

print("------------------------------------------------------------")  # 60個

"""
a = list("甲乙丙丁戊己庚辛壬癸")
b = list("子丑寅卯辰巳午未申酉戌亥")
for i in a:
    for j in b:
        print((i, j))

print("------------------------------------------------------------")  # 60個

a = list("甲乙丙丁戊己庚辛壬癸")
b = list("子丑寅卯辰巳午未申酉戌亥")
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

"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

print("List的用法")
list1 = []
list1.append(333)
list1.append(777)
list1.append(222)
list1.append(111)
list1.append(555)
list1.append(666)
list1.append(444)
list1.append(888)
list1.append(999)
list1.pop()
# 原本加入9個 取出最後一個 所以剩8個
print("串列內共有 %d 個數" % len(list1))
print("最大：%d" % max(list1))
print("最小：%d" % min(list1))
# print('總和：%d' % sum(list1))
print("由小到大排序為：{}".format(sorted(list1)))
print("由大到小排序為：{}".format(sorted(list1, reverse=True)))

print("------------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎", "兔", "龍"]  # 串列
print(type(animals))
print(animals)
for animal in animals:
    print("找到動物 " + animal)

print("------------------------------------------------------------")  # 60個

# set   集合 ssss 大括號 {} 無順序 不可重複 set元素具有唯一性

animal_set = {"鼠", "牛", "虎"}
print(type(animal_set))
print(animal_set)

# 增加一般元素
animal_set.add("兔")
print("animal_set 集合內容 ", animal_set)

# 增加已有元素並觀察執行結果
animal_set.add("牛")
print("animal_set 集合內容 ", animal_set)

print("------------------------------------------------------------")  # 60個

print("數字集合")
numbers_set = {n for n in range(1, 20, 2)}
print(type(numbers_set))
print(numbers_set)

print("------------------------------------------------------------")  # 60個


print("---- zip() --------------------------------------------------------")  # 60個

animals = ["鼠", "牛", "虎"]  # list
weights = [3, 48, 33]  # list
# 把兩個[串列] zip 起來
zipData = zip(animals, weights)  # 執行zip
print("zipData資料類型", type(zipData))  # 列印zip資料類型
animal_list = list(zipData)  # 將zip資料轉成串列
print("animal_list 資料類型", type(animal_list))  # 列印animal_list資料類型
print(animal_list)  # 列印串列

print("animal_list[0] 資料類型", type(animal_list[0]))  # 列印animal_list資料類型
print("animal_list[1] 資料類型", type(animal_list[1]))  # 列印animal_list資料類型
print("animal_list[2] 資料類型", type(animal_list[2]))  # 列印animal_list資料類型

for name, weight in animal_list:
    print("{} 的體重是 {}".format(name, weight))

print("------------------------------------------------------------")  # 60個

print("字串轉串列")
b = list("子丑寅卯辰巳午未申酉戌亥")  # list
c = list("鼠牛虎兔龍蛇馬羊猴雞狗豬")  # list

# 把兩個[串列] zip 起來
zipData = zip(b, c)  # 執行zip

print(zipData)
for item in zipData:
    print(item)

print([item for item in zip(b, c)])

print("------------------------------------------------------------")  # 60個

print("(字串*6)轉串列")
a = list("甲乙丙丁戊己庚辛壬癸" * 6)
print("(字串*5)轉串列")
b = list("子丑寅卯辰巳午未申酉戌亥" * 5)
years = list(zip(a, b))
print(type(years))
print(len(years))
print(years)

print("------------------------------------------------------------")  # 60個

fields = ["name", "weight", "cname"]
info = ["mouse", "3", "鼠"]

zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型

animal = list(zipData)  # 將zip資料轉成串列
print(animal)

print("------------------------------------------------------------")  # 60個

# 資料有欠缺之zip
fields = ["name", "weight", "cname"]
info = ["mouse", "3"]

zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型

animal = list(zipData)  # 將zip資料轉成串列
print(animal)  # 列印串列

print("------------------------------------------------------------")  # 60個

fields = ["name", "weight", "cname"]
info = ["mouse", "3", "鼠"]

zipData = zip(fields, info)  # 執行zip
print(type(zipData))  # 列印zip資料類型

animal = list(zipData)  # 將zip資料轉成串列
print(animal)  # 列印串列

f, i = zip(*animal)  # 執行unzip
print("fields = ", f)
print("info   = ", i)

print("---- map --------------------------------------------------------")  # 60個

print("map 的用法")


def pick(x):
    animals = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
    return animals[x]


# 第n個
select_number = [1, 4, 2, 5, 0, 3, 4, 4, 2]
select_list = map(pick, select_number)

print(type(select_number))
print(type(select_list))

for select in select_list:
    print(select)

print("------------------------------------------------------------")  # 60個

x = [1, 2, 3, 4, 5]
print(type(x))
print(x)

# repr()把整個list原封不動(包含中括號)當成字串搬進來
cc = repr(x)
print(type(cc))
print(cc)

print("------------------------------------------------------------")  # 60個

# 用壽司算符給 list 切片

numbers = [0, 1, 2, 3, 4]

print(numbers[1:3:1])
print(numbers[1:4])
print(numbers[::2])
print(numbers[::-1])
print(list(reversed(numbers)))

string = "Welcome to the United States"
print(string)
print(string[15:28])
print(string[::-1])

print("------------------------------------------------------------")  # 60個

# 串列 生成式
squares = [x**2 for x in range(10)]
print(type(squares))
print(squares)

squares = [x**2 for x in range(10) if x % 2 == 0]
print(type(squares))
print(squares)

matrix = [[x * y for x in range(3)] for y in range(4)]
print(type(matrix))
print(matrix)

print("------------------------------------------------------------")  # 60個

# 走訪 dict 鍵與值

emails = {
    "Bob": "bob@office.com",
    "Alice": "aloce@office.com",
}

for name, email in emails.items():
    print(f"{name} -> {email}")

print("------------------------------------------------------------")  # 60個


# 用 zip() 同時走訪多個容器/旋轉二維陣列

my_numbers = [1, 2, 3, 4]
my_items = ["a", "b", "c"]

for num, item in zip(my_numbers, my_items):
    print(f"{num} -> {item}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(zip(*matrix)))
print(list(zip(*reversed(matrix))))

print("------------------------------------------------------------")  # 60個

# 用 enumerate() 列舉元素
my_items = ["a", "b", "c"]

for i, item in enumerate(my_items):
    print(f"{i}: {item}")

print("------------------------------------------------------------")  # 60個

print("建立tuple資料 動物體重")
weight_tuple = (3, 48, 33, 8, 38, 16, 31, 29, 22, 6, 12, 42)
print("原有資料：")
print(type(weight_tuple))
print(weight_tuple)

# 由小而大
print("體重由小而大排序：", sorted(weight_tuple))

# 遞減排序
print("體重由大而小排序：", sorted(weight_tuple, reverse=True))

print("資料經排序後仍保留原資料位置：")
print(weight_tuple)

print("------------------------------------------------------------")  # 60個

tup = (3, 48, 33, 8, 38, 16, 31, 29, 22, 6, 12, 42)
print("目前元組內的所有元素：")
for item in range(len(tup)):
    print("tup[%2d] %3d" % (item, tup[item]))

print("------------------------------------------------------------")  # 60個

# 完整動物 容器

print("建立字典")
animals = {
    "順序": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "中文名": ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"],
    "英文名": [
        "mouse",
        "ox",
        "tiger",
        "rabbit",
        "dragon",
        "snake",
        "horse",
        "goat",
        "monkey",
        "chicken",
        "dog",
        "pig",
    ],
    "體重": [3, 48, 33, 8, 38, 16, 31, 29, 22, 6, 12, 42],
    "代表": [
        "米老鼠",
        "班尼牛",
        "跳跳虎",
        "彼得兔",
        "逗逗龍",
        "貪吃蛇",
        "草泥馬",
        "喜羊羊",
        "山道猴",
        "肯德雞",
        "貴賓狗",
        "佩佩豬",
    ],
}
print(animals)
print(animals["順序"])
print(animals["中文名"])
print(animals["英文名"])
print(animals["體重"])
print(animals["代表"])

print("建立二維串列")
animals = [
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
    ["龍", "dragon", 38, "逗逗龍"],
    ["蛇", "snake", 16, "貪吃蛇"],
    ["馬", "horse", 31, "草泥馬"],
    ["羊", "goat", 29, "喜羊羊"],
    ["猴", "monkey", 22, "山道猴"],
    ["雞", "chicken", 6, "肯德雞"],
    ["狗", "dog", 12, "貴賓狗"],
    ["豬", "pig", 42, "佩佩豬"],
]

print("串列 操作, 建立內含元組的串列")
animals = [
    ("mouse", "鼠", 3),
    ("ox", "牛", 48),
    ("tiger", "虎", 33),
    ("rabbit", "兔", 8),
    ("dragon", "龍", 38),
    ("snake", "蛇", 16),
    ("horse", "馬", 31),
    ("goat", "羊", 29),
    ("monkey", "猴", 22),
    ("chicken", "雞", 6),
    ("dog", "狗", 12),
    ("pig", "豬", 42),
]
print(type(animals))
print(animals)

# 讀寫檔案大集合

print("將 字典 寫入檔案")
filename = "C:/_git/vcs/_1.data/______test_files2/dict.txt"

with open(filename, "w") as fp:
    # 將字典轉成字串寫入檔案
    fp.write(str(animals))

print("寫入檔案 : " + filename)


"""

#標準版DSLT大集合

#D
字典內是LIST

#S
#L
一維LIST
二維LIST
#T

"""

# range轉list
list1 = range(1, 10)
print(list(list1))

list2 = range(2, 11, 2)
print(list(list2))

list3 = range(1, 10, 2)
print(list(list3))


# 讀取串列資料
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(list1)):
    for j in range(len(list1[i])):
        print(("%4d") % list1[i][j], end=" ")
    print()


list1 = []
sum = 0

score = 85
list1.append(score)
sum += score

score = 72
list1.append(score)
sum += score

score = 91
list1.append(score)
sum += score

score = 88
list1.append(score)
sum += score

score = 86
list1.append(score)
sum += score

score = 79
list1.append(score)
sum += score

score = 93
list1.append(score)
sum += score

print("分數總分為:", sum)
print(list1)


print("------------------------------------------------------------")  # 60個

list1 = [50, 40, 20, 40, 20, 60, 20, 80, 90]
print("原始串列:", list1)
list1.sort()
list1.reverse()
print("由大到小:", list1)

print("------------------------------------------------------------")  # 60個

list1 = []

list1.append(85)
list1.append(72)
list1.append(91)
list1.append(88)
list1.append(86)
list1.append(79)
list1.append(93)

list2 = sorted(list1)
list3 = sorted(list1, reverse=True)
print("原始成績:", list1)
print("由小到大:", list2)
print("由大到小:", list3)

print("------------------------------------------------------------")  # 60個

# list.sort()做遞增、遞減排序
name = ["mouse", "ox", "tiger", "rabbit"]

# 省略參數，依字母做遞增
name.sort()
print(f"英文名依字母遞增排序：\n{name}")

number = [3, 48, 33, 8]
number.sort(reverse=True)  # 遞減排序
print("體重遞減排序：", number)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

animals = "鼠牛虎兔龍蛇馬羊猴雞狗豬"

for animal in animals:
    print(animal)


print("------------------------------------------------------------")  # 60個

print("串列 裡面都是字典")
animal0 = {
    "cname": "鼠",
    "ename": "mouse",
    "weight": 3,
}

animal1 = {
    "cname": "牛",
    "ename": "ox",
    "weight": 48,
}
animal2 = {
    "cname": "虎",
    "ename": "tiger",
    "weight": 33,
}

animal = [animal0, animal1, animal2]
print(type(animal0))
print(type(animal1))
print(type(animal2))
print(type(animal))

for ani in animal:
    for key, value in ani.items():
        print(f"Key: {key}", end="\t")
        print(f"Value: {value}")

print("------------------------------------------------------------")  # 60個


print("字典 裡面都是字典")

animal = {
    "mouse": {
        "cname": "鼠",
        "ename": "mouse",
        "weight": 3,
    },
    "ox": {
        "cname": "牛",
        "ename": "ox",
        "weight": 48,
    },
}

print(animal)
print(type(animal))

for animal_name, animal_info in animal.items():
    print(f"\nAnimalName: {animal_name}")
    name = f"{animal_info['cname']} {animal_info['ename']}"
    weight = animal_info["weight"]
    print(f"\tName: {name}")
    print(f"\tweight: {weight}")

print("------------------------------------------------------------")  # 60個

# 建立空白串列
animals = []

# 建立30隻動物
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    animals.append(new_alien)

# 顯示前5隻動物
for alien in animals[:5]:
    print(alien)
print("...")

# 前3隻改資料
for alien in animals[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

# 顯示前5隻動物
for alien in animals[:5]:
    print(alien)
print("...")

print("------------------------------------------------------------")  # 60個

# 使用 json.dumps() 美觀列印 dict

import json

animals = {
    "鼠": 3,
    "牛": 48,
    "虎": 33,
    "兔": 8,
    "龍": 38,
    "蛇": 16,
}

print(type(animals))

print(json.dumps(animals, indent=4, sort_keys=True))

print("------------------------------------------------------------")  # 60個


# 比較兩個 dict 的差異


def dict_diff(first, second):
    output = {}
    all_keys = sorted(first.keys() | second.keys())

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output


d1 = {"a": 1, "b": 2, "c": 3, "d": 5}
d2 = {"a": 1, "b": 2, "d": 4, "e": 6}
print(dict_diff(d1, d2))

print("------------------------------------------------------------")  # 60個

animals = ["mouse", "ox", "tiger", "rabbit"]

print("反轉前內容：", animals)
animals.reverse()
print("反轉後內容：", animals)
score = [65, 76, 54, 32, 18]
print("反轉前內容：", score)
score.reverse()
print("反轉後內容：", score)

print("------------------------------------------------------------")  # 60個

score = [98, 46, 37, 66, 69]
print("排序前順序：", score)
score.sort()  # 省略reverse參數, 遞增排序
print("遞增排序：", score)
letter = ["one", "time", "happy", "child"]
print("排序前順序：")
print(letter)
letter.sort(reverse=True)  # 依字母做遞減排序
print("遞減排序：")
print(letter)

print("------------------------------------------------------------")  # 60個

animals = ["mouse", "ox", "tiger", "rabbit"]
animal = "tiger"
print("刪除前的animals", animals)
while animal in animals:  # 只要串列內有 tiger 迴圈就繼續
    animals.remove(animal)
print("刪除後的animals", animals)

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)  # 定義元組元素是整數
animals = ("mouse", "ox", "tiger", "rabbit")  # 定義元組元素是字串
mixed = ("James", 50)  # 定義元組元素是不同型態資料
val_tuple = (10,)  # 只有一個元素的元祖
print(numbers1)
print(animals)
print(mixed)
print(val_tuple)
# 列出元組資料型態
print("元組mixed資料型態是: ", type(mixed))

print("------------------------------------------------------------")  # 60個

numbers1 = (1, 2, 3, 4, 5)  # 定義元組元素是整數
animals = ("mouse", "ox", "tiger", "rabbit")  # 定義元組元素是字串
val_tuple = (10,)  # 只有一個元素的元祖
print(numbers1[0])  # 以中括號索引值讀取元素內容
print(numbers1[4])
print(animals[0], animals[1])
print(val_tuple[0])
x, y = ("ox", "tiger")  # 有趣的應用也可以用x,y=animals
print(x, y)

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
for key in keys:
    print(key)

print("------------------------------------------------------------")  # 60個

animals = ("mouse", "ox", "tiger", "rabbit")  # 定義元組元素是水果
print("原始animals元組元素")
for animal in animals:
    print(animal)

animals = ("mouse", "ox", "tiger", "rabbit")  # 定義新的元組元素
print("\n新的animals元組元素")
for animal in animals:
    print(animal)

print("------------------------------------------------------------")  # 60個

animals = ("mouse", "ox", "tiger", "rabbit")
print(animals[1:3])
print(animals[:2])
print(animals[1:])
print(animals[-2:])
print(animals[0:5:2])

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
print("keys元組長度是 %d " % len(keys))

print("------------------------------------------------------------")  # 60個

keys = ("magic", "xaab", 9099)  # 定義元組元素是字串與數字
list_keys = list(keys)  # 將元組改為串列
list_keys.append("secret")  # 增加元素
print("列印元組", keys)
print("列印串列", list_keys)

print("------------------------------------------------------------")  # 60個

keys = ["magic", "xaab", 9099]  # 定義串列元素是字串與數字
tuple_keys = tuple(keys)  # 將串列改為元組
print("列印串列", keys)
print("列印元組", tuple_keys)

print("------------------------------------------------------------")  # 60個

tup = (1, 3, 5, 7, 9)
print("tup最大值是", max(tup))
print("tup最小值是", min(tup))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
enumerate_drinks = enumerate(drinks)  # 數值初始是0
print("轉成元組輸出, 初始值是 0 = ", tuple(enumerate_drinks))

enumerate_drinks = enumerate(drinks, start=10)  # 數值初始是10
print("轉成元組輸出, 初始值是10 = ", tuple(enumerate_drinks))

print("------------------------------------------------------------")  # 60個

drinks = ("coffee", "tea", "wine")
# 解析enumerate物件
for drink in enumerate(drinks):  # 數值初始是0
    print(drink)
for count, drink in enumerate(drinks):
    print(count, drink)
print("****************")
# 解析enumerate物件
for drink in enumerate(drinks, 10):  # 數值初始是10
    print(drink)
for count, drink in enumerate(drinks, 10):
    print(count, drink)

print("------------------------------------------------------------")  # 60個

soldier0 = {}  # 建立空字典
print("空小兵字典", soldier0)
soldier0["tag"] = "red"
soldier0["score"] = 3
print("新小兵字典", soldier0)

print("------------------------------------------------------------")  # 60個

animals = {"mouse": 3, "ox": 48, "tiger": 33, "rabbit": 8}

canimals = animals.copy()
print("位址 = ", id(animals), "  animals元素 = ", animals)
print("位址 = ", id(canimals), "  animals元素 = ", canimals)

print("------------------------------------------------------------")  # 60個

animals = {"mouse": 3, "ox": 48, "tiger": 33, "rabbit": 8}

noodles = {"牛肉麵": 100, "肉絲麵": 80, "陽春麵": 60}
empty_dict = {}
print("animals字典元素數量     = ", len(animals))
print("noodles字典元素數量    = ", len(noodles))
print("empty_dict字典元素數量 = ", len(empty_dict))

print("------------------------------------------------------------")  # 60個

soldier0 = {"tag": "red", "score": 3, "speed": "slow"}  # 建立小兵
soldier1 = {"tag": "blue", "score": 5, "speed": "medium"}
soldier2 = {"tag": "green", "score": 10, "speed": "fast"}
armys = [soldier0, soldier1, soldier2]  # 小兵組成串列
for army in armys:  # 列印小兵
    print(army)

print("------------------------------------------------------------")  # 60個

armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {"tag": "red", "score": 3, "speed": "slow"}
    armys.append(soldier)
# 列印前3個小兵
for soldier in armys[:3]:
    print(soldier)
# 列印小兵數量
print("小兵數量 = ", len(armys))

print("------------------------------------------------------------")  # 60個

armys = []  # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {"tag": "red", "score": 3, "speed": "slow"}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)
# 更改編號36到38的小兵
for soldier in armys[35:38]:
    if soldier["tag"] == "red":
        soldier["tag"] = "blue"
        soldier["score"] = 5
        soldier["speed"] = "medium"
# 列印編號35到40的小兵
print("列印編號35到40小兵資料")
for soldier in armys[34:40]:
    print(soldier)

print("------------------------------------------------------------")  # 60個

# 建立內含字串的字典
sports = {"Curry": ["籃球", "美式足球"], "Durant": ["棒球"], "James": ["美式足球", "棒球", "籃球"]}
# 列印key名字 + 字串'喜歡的運動'
for name, favorite_sport in sports.items():
    print("%s 喜歡的運動是: " % name)
    # 列印value,這是串列
    for sport in favorite_sport:
        print("   ", sport)

print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {
    "cshung": {"last_name": "洪", "first_name": "錦魁", "city": "台北"},
    "kevin": {"last_name": "鄭", "first_name": "義盟", "city": "北京"},
}
# 列印內含字典的字典
for account, account_info in wechat_account.items():
    print("使用者帳號 = ", account)  # 列印鍵(key)
    name = account_info["last_name"] + " " + account_info["first_name"]
    print("姓名       = ", name)  # 列印值(value)
    print("城市       = ", account_info["city"])  # 列印值(value)


print("------------------------------------------------------------")  # 60個

# 建立內含字典的字典
wechat_account = {
    "cshung": {"last_name": "洪", "first_name": "錦魁", "city": "台北"},
    "kevin": {"last_name": "鄭", "first_name": "義盟", "city": "北京"},
}
# 列印字典元素個數
print("wechat_account字典元素個數       ", len(wechat_account))
print("wechat_account['cshung']元素個數 ", len(wechat_account["cshung"]))
print("wechat_account['kevin']元素個數  ", len(wechat_account["kevin"]))

print("------------------------------------------------------------")  # 60個

# 將串列轉成字典
seq1 = ["name", "city"]  # 定義串列
list_dict1 = dict.fromkeys(seq1)
print("字典1 ", list_dict1)
list_dict2 = dict.fromkeys(seq1, "Chicago")
print("字典2 ", list_dict2)
# 將元組轉成字典
seq2 = ["name", "city"]  # 定義元組
tup_dict1 = dict.fromkeys(seq2)
print("字典3 ", tup_dict1)
tup_dict2 = dict.fromkeys(seq2, "New York")
print("字典4 ", tup_dict2)

print("------------------------------------------------------------")  # 60個

animals = {"mouse": 3, "ox": 48}
ret_value1 = animals.get("ox")
print("Value = ", ret_value1)
ret_value2 = animals.get("tiger")
print("Value = ", ret_value2)
ret_value3 = animals.get("tiger", 10)
print("Value = ", ret_value3)

print("------------------------------------------------------------")  # 60個

print("集合 的用法")
animals = {"mouse", "ox", "tiger", "rabbit", "dragon"}
print(type(animals))
print(animals)

print("------------------------------------------------------------")  # 60個

# 集合由整數所組成
integer_set = {1, 2, 3, 4, 5}
print(integer_set)
# 集合由不同資料型態所組成
mixed_set = {1, "Python", (2, 5, 10)}
print(mixed_set)
# 集合的元素是不可變的所以程式第6行所設定的元組元素改成
# 第10行串列的寫法將會產生錯誤
# mixed_set = { 1, 'Python', [2, 5, 10]}

print("------------------------------------------------------------")  # 60個

x = {}  # 這是建立空字典非空集合
print("列印     = ", x)
print("列印類別 = ", type(x))

print("------------------------------------------------------------")  # 60個

empty_dict = {}  # 這是建立空字典
print("列印類別 = ", type(empty_dict))
empty_set = set()  # 這是建立空集合
print("列印類別 = ", type(empty_set))

print("------------------------------------------------------------")  # 60個

print("字串轉集合")
x = set("United States of America")
print(x)
print(type(x))

print("------------------------------------------------------------")  # 60個

# 表達方式1
animals = ["mouse", "ox", "tiger", "rabbit"]
x = set(animals)
print(x)
# 表達方式2
y = set(["mouse", "ox", "tiger", "rabbit"])
print(y)

print("------------------------------------------------------------")  # 60個

animals = set(("mouse", "ox", "tiger", "rabbit", "dragon"))
print(animals)

print("------------------------------------------------------------")  # 60個

animals1 = ["mouse", "ox", "tiger", "rabbit"]
x = set(animals1)  # 將串列轉成集合
animals2 = list(x)  # 將集合轉成串列
print("原先串列資料animals1 = ", animals1)
print("新的串列資料animals2 = ", animals2)

print("------------------------------------------------------------")  # 60個

# 方法1
animals = set("elephant")
print("字元a是屬於animals集合?", "a" in animals)
print("字元d是屬於animals集合?", "d" in animals)

# 方法2
animals = {"mouse", "ox", "tiger"}
boolean = "tiger" in animals
print("tiger in animals", boolean)
boolean = "snake" in animals
print("snake in animals", boolean)

print("------------------------------------------------------------")  # 60個

# 方法1
animals = set("elephant")
print("字元a是不屬於animals集合?", "a" not in animals)
print("字元d是不屬於animals集合?", "d" not in animals)
# 方法2
animals = {"mouse", "ox", "tiger"}
boolean = "tiger" not in animals
print("tiger not in animals", boolean)
boolean = "snake" not in animals
print("snake not in animals", boolean)

print("------------------------------------------------------------")  # 60個

animals = ["ox", "mouse", "dragon"]
nums = [1, 3, 5]
animalslist = animals * 3  # 串列乘以數字
print(animalslist)
numslist = nums * 5  # 串列乘以數字
print(numslist)

print("------------------------------------------------------------")  # 60個

James = ["Lebron James", 23, 19, 22, 31, 18]  # 定義James串列
Love = ["Kevin Love", 20, 18, 30, 22, 15]  # 定義Love串列
game3 = James[4] + Love[4]
LKgame = James[0] + " 和 " + Love[0] + "第四場總得分 = "
print(LKgame, game3)

print("------------------------------------------------------------")  # 60個

warriors = ["Curry", "Durant", "Iquodala", "Bell", "Thompson"]
print("2018年初NBA勇士隊主將陣容", warriors)
del warriors[3]  # 不明原因離隊
print("2018年末NBA勇士隊主將陣容", warriors)

print("------------------------------------------------------------")  # 60個

nums1 = [1, 3, 5]
print("刪除nums1串列索引1元素前   = ", nums1)
del nums1[1]
print("刪除nums1串列索引1元素後   = ", nums1)
nums2 = [1, 2, 3, 4, 5, 6]
print("刪除nums2串列索引[0:2]前   = ", nums2)
del nums2[0:2]
print("刪除nums2串列索引[0:2]後   = ", nums2)
nums3 = [1, 2, 3, 4, 5, 6]
print("刪除nums3串列索引[0:6:2]前 = ", nums3)
del nums3[0:6:2]
print("刪除nums3串列索引[0:6:2]後 = ", nums3)

print("------------------------------------------------------------")  # 60個

animals = ["ox", "mouse", "dragon"]
print("animals串列長度是 = %d" % len(animals))
if len(animals) != 0:
    del animals[0]
    print("刪除animals串列元素成功")
    print("animals串列長度是 = %d" % len(animals))
else:
    print("animals串列內沒有元素資料")
nums = []
print("nums串列長度是 = %d" % len(nums))
if len(nums) != 0:
    del nums[0]
    print("刪除nums串列元素成功")
else:
    print("nums串列內沒有元素資料")

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "ox", "tiger"]
print("目前串列內容 = ", animals)
print("在索引1位置插入mouse")
animals.insert(1, "mouse")
print("新的串列內容 = ", animals)
print("在索引0位置插入rabbit")
animals.insert(0, "rabbit")
print("最新串列內容 = ", animals)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "ox", "tiger", "rabbit"]
print("目前串列內容 = ", animals)
print("使用pop( )刪除串列元素")
popped_animal = animals.pop()  # 刪除串列末端值
print("所刪除的串列內容是 : ", popped_animal)
print("新的串列內容 = ", animals)
print("使用pop(1)刪除串列元素")
popped_animal = animals.pop(1)  # 刪除串列索引為1的值
print("所刪除的串列內容是 : ", popped_animal)
print("新的串列內容 = ", animals)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "rabbit", "ox", "tiger", "rabbit"]
print("目前串列內容 = ", animals)
print("使用remove( )刪除串列元素")
expensive = "rabbit"
animals.remove(expensive)  # 刪除第一次出現的元素rabbit
print("所刪除的內容是: " + expensive.upper() + " 因為太貴了")
print("新的串列內容", animals)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "rabbit", "ox", "tiger", "rabbit"]
print("目前串列內容 = ", animals)
# 直接列印animals[::-1]顛倒排序,不更改串列內容
print("列印使用[::-1]顛倒排序\n", animals[::-1])
# 更改串列內容
print("使用reverse( )顛倒排序串列元素")
animals.reverse()  # 顛倒排序串列
print("新的串列內容 = ", animals)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "rabbit", "ox", "tiger"]
print("目前串列內容 = ", animals)
print("使用sort( )由小排到大")
animals.sort()
print("排序串列結果 = ", animals)
nums = [5, 3, 9, 2]
print("目前串列內容 = ", nums)
print("使用sort( )由小排到大")
nums.sort()
print("排序串列結果 = ", nums)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "rabbit", "ox", "tiger"]
print("目前串列內容 = ", animals)
print("使用sort( )由大排到小")
animals.sort(reverse=True)
print("排序串列結果 = ", animals)
nums = [5, 3, 9, 2]
print("目前串列內容 = ", nums)
print("使用sort( )由大排到小")
nums.sort(reverse=True)
print("排序串列結果 = ", nums)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "rabbit", "ox", "tiger"]
print("目前串列animal內容 = ", animals)
print("使用sorted( )由小排到大")
animals_sorted = sorted(animals)
print("排序串列結果 = ", animals_sorted)
print("原先串列animal內容 = ", animals)
nums = [5, 3, 9, 2]
print("目前串列num內容 = ", nums)
print("使用sorted( )由小排到大")
nums_sorted = sorted(nums)
print("排序串列結果 = ", nums_sorted)
print("原先串列num內容 = ", nums)

print("------------------------------------------------------------")  # 60個

animals = ["dragon", "rabbit", "ox", "tiger"]
print("目前串列animal內容 = ", animals)
print("使用sorted( )由大排到小")
animals_sorted = sorted(animals, reverse=True)
print("排序串列結果    = ", animals_sorted)
print("原先串列animal內容 = ", animals)
nums = [5, 3, 9, 2]
print("目前串列num內容 = ", nums)
print("使用sorted( )由大排到小")
nums_sorted = sorted(nums, reverse=True)
print("排序串列結果    = ", nums_sorted)
print("原先串列num內容 = ", nums)

print("------------------------------------------------------------")  # 60個

animals = ["ox", "mouse", "dragon"]
search_str = "mouse"
i = animals.index(search_str)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_str, i))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
j = nums.index(search_val)
print("所搜尋元素 %s 第一次出現位置索引是 %d" % (search_val, j))

print("------------------------------------------------------------")  # 60個

James = ["Lebron James", 23, 19, 22, 31, 18]  # 定義James串列
games = len(James)  # 求元素數量
score_Max = max(James[1:games])  # 最高得分
i = James.index(score_Max)  # 場次
print(James[0], "在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

animals = ["ox", "mouse", "dragon"]
search_str = "mouse"
num1 = animals.count(search_str)
print("所搜尋元素 %s 出現 %d 次" % (search_str, num1))
nums = [7, 12, 30, 12, 30, 9, 8]
search_val = 30
num2 = nums.count(search_val)
print("所搜尋元素 %s 出現 %d 次" % (search_val, num2))

print("------------------------------------------------------------")  # 60個

char = "-"
lst = ["Silicon", "Stone", "Education"]
print(char.join(lst))
char = "***"
lst = ["Silicon", "Stone", "Education"]
print(char.join(lst))
char = "\n"  # 換行字元
lst = ["Silicon", "Stone", "Education"]
print(char.join(lst))

print("------------------------------------------------------------")  # 60個

James = [["Lebron James", "SF", "12/30/84"], 23, 19, 22, 31, 18]  # 定義James串列
games = len(James)  # 求元素數量
score_Max = max(James[1:games])  # 最高得分
i = James.index(score_Max)  # 場次
name = James[0][0]
position = James[0][1]
born = James[0][2]
print("姓名     : ", name)
print("位置     : ", position)
print("出生日期 : ", born)
print("在第 %d 場得最高分 %d" % (i, score_Max))

print("------------------------------------------------------------")  # 60個

animals1 = ["ox", "mouse", "dragon"]
animals2 = ["tiger", "snake"]
print("原先animals1串列內容 = ", animals1)
print("原先animals2串列內容 = ", animals2)
animals1.append(animals2)
print("執行append( )後串列animals1內容 = ", animals1)
print("執行append( )後串列animals2內容 = ", animals2)

print("------------------------------------------------------------")  # 60個

animals1 = ["ox", "mouse", "dragon"]
animals2 = ["tiger", "snake"]
print("原先animals1串列內容 = ", animals1)
print("原先animals2串列內容 = ", animals2)
animals1.extend(animals2)
print("執行extend( )後串列animals1內容 = ", animals1)
print("執行extend( )後串列animals2內容 = ", animals2)

print("------------------------------------------------------------")  # 60個

mysports = ["basketball", "baseball"]
friendsports = mysports
print("我喜歡的運動     = ", mysports)
print("我朋友喜歡的運動 = ", friendsports)

mysports.append("football")
friendsports.append("soccer")
print("我喜歡的最新運動     = ", mysports)
print("我朋友喜歡的最新運動 = ", friendsports)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

animals = {
    "鼠": "mouse",
    "牛": "ox",
    "虎": "tiger",
    "兔": "rabbit",
    "龍": "dragon",
}

for cname, ename in animals.items():
    print("中文名: ", cname)
    print("英文名: ", ename)


animals = {
    "鼠": "mouse",
    "牛": "ox",
    "虎": "tiger",
    "兔": "rabbit",
    "龍": "dragon",
}

for name in animals.keys():
    print("姓名: ", name)

print("------------------------------------------------------------")  # 60個

animals = {
    "鼠": "mouse",
    "牛": "ox",
    "虎": "tiger",
    "兔": "rabbit",
    "龍": "dragon",
}
for name in animals:
    print(name)
    print("Hi! %s  %s" % (name, animals[name]))

for name in sorted(animals.keys()):
    print(name)
    print("Hi! %s  %s" % (name, animals[name]))

print("------------------------------------------------------------")  # 60個

animals = {
    "鼠": "mouse",
    "牛": "ox",
    "虎": "tiger",
    "兔": "rabbit",
    "龍": "dragon",
}

for ani in animals.values():
    print(ani)

print("------------------------------------------------------------")  # 60個

animals = {
    "鼠": "mouse",
    "牛": "ox",
    "虎": "tiger",
    "兔": "rabbit",
    "龍": "dragon",
}

for ani in set(animals.values()):
    print(ani)

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


# 標準完整的容器範例


# 完整的動物字典 DDDD
animals_dict = {
    "mouse": "鼠",
    "ox": "牛",
    "tiger": "虎",
    "rabbit": "兔",
    "dragon": "龍",
    "snake": "蛇",
    "horse": "馬",
    "goat": "羊",
    "monkey": "猴",
    "chicken": "雞",
    "dog": "狗",
    "pig": "豬",
}


# 完整的動物集合 SSSS
animals_set = set()


# 完整的動物串列(一維) LLLL
animals_list1 = []


# 完整的動物串列(二維) LLLL

animals_list2 = []

# 完整的動物元組 TTTT
animals_tuple = ()
