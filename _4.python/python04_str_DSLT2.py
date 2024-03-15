import sys

"""
各種python專用的語法 字典 串列 元組 集合


"""

print('------------------------------------------------------------')	#60個


animals = '鼠牛虎兔龍蛇馬羊猴雞狗豬'

for animal in animals:
    print(animal)



print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個


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



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


