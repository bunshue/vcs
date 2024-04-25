import sys

"""
各種python專用的語法 字典 串列 元組 集合


"""

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

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
print("Stephen Curry是 %s 的球員" % players["Stephen Curry"])
print("Kevin Durant是 %s 的球員" % players["Kevin Durant"])
print("Paul Gasol是 %s 的球員" % players["Paul Gasol"])

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
for name, team in players.items():
    print("\n姓名: ", name)
    print("隊名: ", team)

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
for name in players.keys():
    print("姓名: ", name)

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
for name in players:
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
for name in sorted(players.keys()):
    print(name)
    print("Hi! %s 我喜歡看你在 %s 的表現" % (name, players[name]))

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
for team in players.values():
    print(team)

print("------------------------------------------------------------")  # 60個

players = {
    "Stephen Curry": "Golden State Warriors",
    "Kevin Durant": "Golden State Warriors",
    "Lebron James": "Cleveland Cavaliers",
    "James Harden": "Houston Rockets",
    "Paul Gasol": "San Antonio Spurs",
}
for team in set(players.values()):
    print(team)

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
