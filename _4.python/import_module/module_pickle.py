import pickle

print('使用 pickle 模組 寫讀二進位檔案')

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
