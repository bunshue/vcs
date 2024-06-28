import sys
import pickle

print('使用 pickle 模組 寫讀二進位檔案')
'''
print('------------------------------------------------------------')	#60個

filename = 'pickle.dat'
print('寫入二進位檔案 :', filename)
fp = open(filename, "wb")
pickle.dump(2023, fp)           #整數
pickle.dump('中秋節', fp)       #字串
pickle.dump(123.456, fp)        #浮點數
pickle.dump([1, 2, 3, 4], fp)   #串列
fp.close()

print('讀取二進位檔案 :', filename)
fp = open(filename, "rb")
a = pickle.load(fp)
print(type(a))
print(a)
b = pickle.load(fp)
print(type(b))
print(b)
c = pickle.load(fp)
print(type(c))
print(c)
d = pickle.load(fp)
print(type(d))
print(d)
fp.close()

print('------------------------------------------------------------')	#60個

print('用pickle來存取一個字典檔案, 讀寫接用 wb/rb binary')

animal = {
    'mouse':'老鼠',
    'panda':'貓熊',
    'penguin':'企鵝',
    'lion':'獅子',
}

f = open("animal.pickle", 'wb')

pickle.dump(animal, f)

f.close()

f = open("animal.pickle", 'rb')

pickledict = pickle.load(f)
f.close()
print(pickledict)

print('------------------------------------------------------------')	#60個

print('將資料寫入pickle檔案')
a = 12
b = 34
c = 56
file = open("state", 'wb')
pickle.dump(a, file)
pickle.dump(b, file)
pickle.dump(c, file)
file.close()

print('------------------------------------------------------------')	#60個

print('從pickle檔案讀出資料')
file = open("state", 'rb')
a = pickle.load(file)
b = pickle.load(file)
c = pickle.load(file)
file.close()

print('a =', a)
print('b =', b)
print('c =', c)

print('------------------------------------------------------------')	#60個

game_info = {
    "position_X":"100",
    "position_Y":"200",
    "money":300,
    "pocket":["黃金", "鑰匙", "小刀"]
}

fn = "tmp_pickle.dat"
fn_obj = open(fn, 'wb')         # 二進位開啟
pickle.dump(game_info, fn_obj)
fn_obj.close()

print('------------------------------------------------------------')	#60個

fn = "data/data19.dat"
fn_obj = open(fn, 'rb')         # 二進位開啟
game_info = pickle.load(fn_obj)
fn_obj.close()
print(game_info)

print("------------------------------------------------------------")  # 60個

fp = open("note.dat", "wb")
print("寫入整數: 11")
pickle.dump(11, fp)
print("寫入字串: '陳會安'")
pickle.dump("陳會安", fp)
print("寫入串列: [1, 2, 3, 4]")
pickle.dump([1, 2, 3, 4], fp)
fp.close()    

print("------------------------------------------------------------")  # 60個

fp = open("note.dat", "rb")
i = pickle.load(fp)
print("讀取整數 = ", str(i))
str1 = pickle.load(fp)
print("讀取姓名 = ", str1)
list1 = pickle.load(fp)
print("讀取串列 = ", str(list1))
fp.close()    

print("------------------------------------------------------------")  # 60個

data = {
    "name": "Joe Chen",
    "age": 22,
    "score": 95,
}
with open("dic.dat", "wb") as f:
    pickle.dump(data, f)
with open("dic.dat", "rb") as f:
    new_data = pickle.load(f)
print(new_data)    

print('------------------------------------------------------------')	#60個
'''
print("寫入資料給pickle")
outfile = open("tmp_pickle_file.dat", "wb")

for _ in range(10):
    pickle.dump(_, outfile)
    #print(_)
for _ in range(10):
    pickle.dump(_, outfile)
    #print(_)

outfile.close() # Close the output file

print("從pickle讀取資料")
infile = open("tmp_pickle_file.dat", "rb")
    
end_of_file = False
while not end_of_file:
    try:
        print(pickle.load(infile), end = " ")
    except EOFError:
        end_of_file = True

infile.close() # Close the input file

print("\nOK")
    
print('------------------------------------------------------------')	#60個

a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}

# pickle a variable to a file
file = open('tmp_pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()

# reload a file to a variable
with open('tmp_pickle_example.pickle', 'rb') as file:
    a_dict1 =pickle.load(file)

print(a_dict1)

print('------------------------------------------------------------')	#60個

import os

print('製作 pickle 檔案')

print('看似只能一次寫入 不能附加 所以要用二維陣列 一次寫入')

filename = "tmp_pickle.dat"
outfile = open(filename, "wb")

addressList = [[5, "aaa", "bbb", "ccc", "ddd"], [15, "aaa", "bbb", "ccc", "ddd"], [25, "aaa", "bbb", "ccc", "ddd"]]

pickle.dump(addressList, outfile)

outfile.close()


print('讀取 pickle 檔案')

addressList = []

if not os.path.isfile(filename):
    addressList = []
else:
    print("使用 pickle 讀取檔案")
    try:
        infile = open(filename, "rb")
        addressList = pickle.load(infile)
        print(type(addressList))
        print(len(addressList))
    except EOFError:
        addressList = []

    infile.close()
    print(addressList)





print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



