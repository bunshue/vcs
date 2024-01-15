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





print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('測試完成')

    



