import sys
import pickle

print("使用 pickle 模組 寫讀二進位檔案")

print("------------------------------------------------------------")  # 60個

filename = "tmp_pickle1.dat"

print("寫入二進位檔案 :", filename)
f = open(filename, "wb")
pickle.dump(2023, f)  # 整數
pickle.dump("中秋節", f)  # 字串
pickle.dump(123.456, f)  # 浮點數
pickle.dump([1, 2, 3, 4], f)  # 串列
f.close()

filename = "tmp_pickle1.dat"

print("讀取二進位檔案 :", filename)
f = open(filename, "rb")
a = pickle.load(f)
print(type(a))
print(a)
b = pickle.load(f)
print(type(b))
print(b)
c = pickle.load(f)
print(type(c))
print(c)
d = pickle.load(f)
print(type(d))
print(d)
f.close()

print("------------------------------------------------------------")  # 60個

print("用pickle來存取一個字典檔案, 讀寫接用 wb/rb binary")

animal = {
    "mouse": "老鼠",
    "panda": "貓熊",
    "penguin": "企鵝",
    "lion": "獅子",
}

filename = "tmp_pickle2.dat"
f = open(filename, "wb")

pickle.dump(animal, f)

f.close()

filename = "tmp_pickle2.dat"
f = open(filename, "rb")

pickledict = pickle.load(f)
f.close()
print(pickledict)

print("------------------------------------------------------------")  # 60個

print("將資料寫入pickle檔案")
a = 12
b = 34
c = 56

filename = "tmp_pickle3.dat"

file = open(filename, "wb")
pickle.dump(a, file)
pickle.dump(b, file)
pickle.dump(c, file)
file.close()

print("從pickle檔案讀出資料")

filename = "tmp_pickle3.dat"

file = open(filename, "rb")
a = pickle.load(file)
b = pickle.load(file)
c = pickle.load(file)
file.close()

print("a =", a)
print("b =", b)
print("c =", c)

print("------------------------------------------------------------")  # 60個

game_info = {
    "position_X": "100",
    "position_Y": "200",
    "money": 300,
    "pocket": ["黃金", "鑰匙", "小刀"],
}

filename = "tmp_pickle4.pickle"
filename_obj = open(filename, "wb")  # 二進位開啟
pickle.dump(game_info, filename_obj)
filename_obj.close()

print("------------------------------------------------------------")  # 60個
# 3030

filename = "tmp_pickle4.pickle"
filename_obj = open(filename, "rb")  # 二進位開啟
game_info = pickle.load(filename_obj)
filename_obj.close()
print(game_info)

print("------------------------------------------------------------")  # 60個

filename = "tmp_pickle5.dat"
f = open(filename, "wb")
print("寫入整數: 11")
pickle.dump(11, f)
print("寫入字串: '陳會安'")
pickle.dump("陳會安", f)
print("寫入串列: [1, 2, 3, 4]")
pickle.dump([1, 2, 3, 4], f)
f.close()

filename = "tmp_pickle5.dat"

f = open(filename, "rb")
i = pickle.load(f)
print("讀取整數 = ", str(i))
str1 = pickle.load(f)
print("讀取姓名 = ", str1)
list1 = pickle.load(f)
print("讀取串列 = ", str(list1))
f.close()

print("------------------------------------------------------------")  # 60個

data = {
    "name": "Joe Chen",
    "age": 22,
    "score": 95,
}

filename = "tmp_pickle6.dat"
with open(filename, "wb") as f:
    pickle.dump(data, f)

filename = "tmp_pickle6.dat"
with open(filename, "rb") as f:
    new_data = pickle.load(f)

print(new_data)

print("------------------------------------------------------------")  # 60個

print("寫入資料給pickle")

filename = "tmp_pickle7.dat"
f = open(filename, "wb")

for _ in range(10):
    pickle.dump(_, f)
    # print(_)
for _ in range(10):
    pickle.dump(_, f)
    # print(_)

f.close()

print("從pickle讀取資料")
filename = "tmp_pickle7.dat"
f = open(filename, "rb")

end_of_file = False
while not end_of_file:
    try:
        print(pickle.load(f), end=" ")
    except EOFError:
        end_of_file = True

f.close()

print("------------------------------------------------------------")  # 60個

a_dict = {"da": 111, 2: [23, 1, 4], "23": {1: 2, "d": "sad"}}

# pickle a variable to a file
filename = "tmp_pickle8.dat"
file = open(filename, "wb")
pickle.dump(a_dict, file)
file.close()

# reload a file to a variable
filename = "tmp_pickle8.dat"
with open(filename, "rb") as file:
    a_dict1 = pickle.load(file)

print(a_dict1)

print("------------------------------------------------------------")  # 60個

import os

print("製作 pickle 檔案")

print("看似只能一次寫入 不能附加 所以要用二維陣列 一次寫入")

filename = "tmp_pickle9.dat"
f = open(filename, "wb")

addressList = [
    [5, "aaa", "bbb", "ccc", "ddd"],
    [15, "aaa", "bbb", "ccc", "ddd"],
    [25, "aaa", "bbb", "ccc", "ddd"],
]

pickle.dump(addressList, f)

f.close()


print("讀取 pickle 檔案")

addressList = []

if not os.path.isfile(filename):
    addressList = []
else:
    print("使用 pickle 讀取檔案")
    try:
        f = open(filename, "rb")
        addressList = pickle.load(f)
        print(type(addressList))
        print(len(addressList))
    except EOFError:
        addressList = []

    f.close()
    print(addressList)

print("------------------------------------------------------------")  # 60個

data1 = {"a": [1, 2.0, 4 + 6j], "b": ("string1", "Unicode string"), "c": None}
output = open("tmp2.pkl", "wb")
pickle.dump(data1, output)
output.close()

pkl_file = open("tmp2.pkl", "rb")
data2 = pickle.load(pkl_file)
print(data2)
pkl_file.close()

print("------------------------------------------------------------")  # 60個
""" NG
file_obj = open("recordmat.dat", "wb")
pickle.dump(recordmat[0], file_obj)
file_obj.close()

read_obj = open("recordmat.dat", "rb")
readmat = pickle.load(read_obj)
print(shape(readmat))
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
