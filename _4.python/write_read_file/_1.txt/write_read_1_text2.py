#各種檔案寫讀範例 txt 2

print('------------------------------------------------------------')	#60個

filename = 'data/pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("------------------------------------------------------------")  # 60個

filename = 'data/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))

print("------------------------------------------------------------")  # 60個

filename = 'data/pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

'''    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
'''
print("------------------------------------------------------------")  # 60個

with open("data/phrase.txt","r") as file1:
    txt = file1.readlines()#一次讀取所有行
    for line in txt: #以for廻圈讀取
        print(line, end = '')

print("------------------------------------------------------------")  # 60個

file1=open("data/phrase.txt","r")
text=file1.read(1) #以read()方法讀取檔案
print(text)
text=file1.read(3) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
file1.close()

print('------------------------------------------------------------')	#60個


with open("data/phrase.txt",'r') as file1:
    for line in file1:
        print(line,end='')

print('------------------------------------------------------------')	#60個

file1=open("data/phrase.txt ","r")
line= file1.readline()
while line != '':
    print(line,end='')
    line= file1.readline()
file1.close()

print('------------------------------------------------------------')	#60個


file1=open("data/phrase.txt","r")
text=file1.read() #以read()方法讀取檔案
print(text,end='')
file1.close()


print('------------------------------------------------------------')	#60個




obj='''五福臨門
十全十美
'''
#建立新檔
fn = open('tmp_phrase2.txt', 'w')   
fn.write(obj)#將字串寫入檔案   
fn.close()#關閉檔案



file1=open("tmp_phrase2.txt",'r')
for line in file1:
    print(line,end='')
file1.close()


import os.path #匯入os.path
import sys #匯入sys

if os.path.isfile('tmp_phrase_new.txt'): #如果檔案存在則取消複製
    print('此檔案已存在,不要複製')
    sys.exit()
else:
    file1=open('tmp_phrase2.txt','r')#讀取模式
    file2=open('tmp_phrase_new.txt','w')#寫入模式
    text=file1.read() #以逐字元的方式讀取檔案
    text=file2.write(text) #寫入檔案
    print('檔案複製成功')
    file1.close() 
    file2.close() 




print('------------------------------------------------------------')	#60個


print('編碼錯誤')
obj=open('data/test_encode.txt','r', encoding='cp950')  #開啟檔案
for line in obj:
	print(line)
obj.close()

print('編碼正確')

obj=open('data/test_encode.txt','r', encoding='UTF-8')  #開啟檔案
for line in obj:
	print(line)
obj.close()




print('------------------------------------------------------------')	#60個


str1 = "黃河遠上白雲間\n"
str2 = "一片孤城萬仞山\n"
str3 = "羌笛何須怨楊柳\n"
str4 = "春風不度玉門關"
strs = [str1, str2, str3, str4]

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950.txt'
print("用cp950編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='cp950') as fObj:
    fObj.write(str1)
    fObj.write(str2)
    fObj.write(str3)
    fObj.write(str4)

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp936.txt'
print("用cp936編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='cp936') as fObj:
    fObj.writelines(strs)

print("------------------------------------------------------------")  # 60個

filename = 'poem.utf-8.txt'
print("用utf-8編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='utf-8') as fObj:
    fObj.writelines(strs)

print("------------------------------------------------------------")  # 60個

poem_text = "黃河遠上白雲間一片孤城萬仞山羌笛何須怨楊柳春風不度玉門關"

filename = 'poem.cp950b.txt'
print("用cp950編碼 分段寫檔, 檔名 :", filename)
size = len(poem_text)
offset = 0
chunk = 5                         # 每次寫入的單位
with open(filename, 'w', encoding='cp950') as fObj:
    while True:
        if offset > size:
            break
        print(fObj.write(poem_text[offset:offset+chunk]))
        offset += chunk

print("------------------------------------------------------------")  # 60個

print('用read()一次讀完全檔')
filename = 'poem.cp950.txt'
fObj = open(filename, 'r', encoding='cp950')    
data = fObj.read()      # 讀取檔案到變數data
fObj.close()            # 關閉檔案物件
print(data)             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

print('一次讀一行')
filename = 'poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:    
    for line in fObj:       # 相當於逐列讀取
        print(line)         # 輸出line

print("------------------------------------------------------------")  # 60個

print('一次讀一行 加 rstrip()')
filename = 'poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:    
    for line in fObj:           # 相當於逐列讀取
        print(line.rstrip())    # 輸出line

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950.txt'
with open(filename, 'r', encoding='cp950') as fObj:
    print("用readline()讀一行")
    str1 = fObj.readline()
    print(str1)

    print("用readline()讀一行")
    str2 = fObj.readline()
    print(str2)

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950.txt'

print('用readlines()一次讀完全檔 至一個 list')

with open(filename, 'r', encoding='cp950') as fObj:    
    text_list = fObj.readlines()

#print(text_list)
for line in text_list:
    print(line)

print("------------------------------------------------------------")  # 60個

filename = 'poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:
    print(f"目前指針位置 {fObj.tell()}")    
    str1 = fObj.read(7)
    print(f"讀出資料 : {str1}, 目前指針位置 {fObj.tell()}")
    str2 = fObj.read(7)
    print(f"讀出資料 : {str2}, 目前指針位置 {fObj.tell()}")
    str3 = fObj.read(7)
    print(f"讀出資料 : {str3}, 目前指針位置 {fObj.tell()}")  

print("------------------------------------------------------------")  # 60個

filename = 'poem.utf-8.txt'
chunk = 3
msg = ''
with open(filename, 'r', encoding='utf-8') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個




