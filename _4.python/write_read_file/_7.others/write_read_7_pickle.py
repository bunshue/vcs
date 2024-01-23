import pickle

print('使用 pickle 模組 寫讀二進位檔案')

print('------------------------------------------------------------')	#60個
'''
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

'''

'''
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
'''


print('------------------------------------------------------------')	#60個

import pickle

print('使用 pickle 模組 寫讀二進位檔案')



import pickle
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


print('------------------------------------------------------------')	#60個

import pickle

fn = "data/data19.dat"
fn_obj = open(fn, 'rb')         # 二進位開啟
game_info = pickle.load(fn_obj)
fn_obj.close()
print(game_info)

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個
