#各種讀取檔案範例

filename = "data\poetry.txt"
print("讀取檔案 : "+filename)

f = open(filename, 'r', encoding = 'utf8')
#f = open(filename, 'r', encoding = 'UTF-8')

print("檔名: ", f.name)
for line in f.readlines():
    #line = line.strip
    print(line)
f.close


print("一次讀完一檔")
#f = open(filename, 'r')
f = open(filename, 'r', encoding = 'utf8')
line = f.readlines()
print(line),
f.close()

print("一次讀一行")
#f = open(filename, 'r')
f = open(filename, 'r', encoding = 'utf8')
i = 0
while True:
    line = f.readline()
    if len(line) == 0:  #Zero length indicates EOF
        break;
    i = i + 1
    #print(str(i), line),    # Notice comma to avoid automatic newline added by Python
    print(line),
f.close()

print("一次讀一行")
#f = open(filename, 'r')
f = open(filename, 'r', encoding = 'utf8')
for line in f: print(line) #通過迭代器訪問
f.close()


print("讀前10拜")
#fo = open(filename, "r+")
fo = open(filename, 'r+', encoding = 'utf8')

str = fo.read(10);  #讀10拜
print("Read String is : ", str)
# Close opend file
fo.close()

#!/usr/bin/python
# -*- coding: UTF-8 -*-    #告訴Python直譯器檔案編碼為UTF-8

#f = open(filename, 'r')
f = open(filename, 'r+', encoding = 'utf8')

b_str = f.read()
f.close()

print(b_str)

#print(b_str.decode('utf-8')) # 這是什麼？
#print(b_str.decode('utf-8').encode('utf-8')) # 這是什麼？



#從檔案把資料讀出來，一次讀完
#打開一個文件
#f = open(filename, "r")
f = open(filename, 'r', encoding = 'utf8')

#一次讀完資料
str = f.read()
print(str)

#關閉文件
f.close()


#從檔案把資料讀出來，一次讀一行
#打開一個文件
#f = open(filename, "r")
f = open(filename, 'r', encoding = 'utf8')

#一次讀一行
str = f.readline()
print(str)

#一次讀一行
str = f.readline()
print(str)

#一次讀一行
str = f.readline()
print(str)

#關閉文件
f.close()


#從檔案把資料讀出來，一次讀所有行
#打開一個文件
#f = open(filename, "r")
f = open(filename, 'r', encoding = 'utf8')

#一次讀所有行
str = f.readlines()
print(str)

#關閉文件
f.close()




