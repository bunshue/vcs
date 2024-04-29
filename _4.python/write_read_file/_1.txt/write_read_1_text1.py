"""
各種檔案寫讀範例 txt 1


先寫後讀 寫新檔 讀舊檔

"""

import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

filename_rw1 = 'tmp_write_read_text01.txt'

print("將字串寫入檔案 : " + filename_rw1)
f = open(filename_rw1, 'w')
f.write('ABCDE')
f.write('FGHIJ')
f.write('KLMNO')
f.write('PQRST')
f.close()

""" 改用 with as 
with open(filename_rw1, 'w') as f:
    f.write('XXXXX')
"""

print("附加檔案 : " + filename_rw1)
f = open(filename_rw1, 'a') 
f.write('UVWXYZ')
f.close()

print("------------------------------------------------------------")  # 60個

print("附加模式寫檔案")
filename_w = 'tmp_write_read_text05.txt'
f = open(filename_w, "a")
data = "123456789\n"
f.write(data)
f.close()

print("------------------------------------------------------------")  # 60個

print("寫入檔案範例")
filename_w = 'tmp_write_read_text06.txt'

#寫資料到檔案中
f = open(filename_w, "w")

#寫資料
num = f.write("黃河遠上白雲間\n一片孤城萬仞山\n羌笛何須怨楊柳\n春風不度玉門關\n")
print("總共寫了 ", num, " 拜")

#關閉文件
f.close()

print("讀取一檔並將資料寫到另檔的範例")

#python讀和寫文件

filename_r = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'
filename_w = 'tmp_write_read_text07.txt'

with open(filename_r, 'rt', encoding = 'utf8') as f:
    data = f.read()
    
print("data :\n", data)

f.close()

with open(filename_w, 'wt') as f:
    f.write(data)
    
f.close()

print('------------------------------------------------------------')	#60個

"""
模式有
r - 讀取(檔案需存在)
w - 新建檔案寫入(檔案可不存在，若存在則清空)
a - 資料附加到舊檔案後面(游標指在EOF)
"""
filename = 'tmp_write_read_text13.txt'
f = open(filename, 'a', encoding = 'UTF-8')   # 也可使用指定路徑等方式，如： C:\A.txt
f.write('黃河遠上白雲間\n')
f.write('一片孤城萬仞山\n')
f.write('羌笛何須怨楊柳\n')
f.write('春風不度玉門關\n')
f.close()

filename = 'tmp_write_read_text13.txt'
with open(filename, "w") as f:
    f.write("This Text is going to out file\nLook at it and see!")

print("------------------------------------------------------------")  # 60個

filename_rw3 = 'tmp_write_read_text03.bin'

print("建立一個檔案 binary, 檔名 : " + filename_rw3)

content="""黃河遠上白雲間
一片孤城萬仞山
羌笛何須怨楊柳
春風不度玉門關
"""
content=content.encode("utf-8") #轉成 bytes
with open(filename_rw3,'wb') as f:
    f.write(content)

print("------------------------------------------------------------")  # 60個

filename1 = 'tmp_write_read_text04.txt'

print("建立一個檔案")

content="""黃河遠上白雲間
一片孤城萬仞山
羌笛何須怨楊柳
春風不度玉門關
"""

f = open(filename1,'w')
f.write(content)
f.close()

filename_rw2 = 'tmp_write_read_text08.txt'

content="""黃河遠上白雲間
一片孤城萬仞山
羌笛何須怨楊柳
春風不度玉門關
"""

f=open(filename_rw2, 'w')
f.write(content)
f.close()


content="""黃河遠上白雲間
一片孤城萬仞山
羌笛何須怨楊柳
春風不度玉門關
"""

f=open(filename_rw2, 'w',encoding='UTF-8')
f.write(content)
f.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 : " + filename_rw1)
f = open(filename_rw1, 'r')
read_data = f.read()
f.close()
print('檔案內容: ', read_data)

print("------------------------------------------------------------")  # 60個

print("讀取檔案 : " + filename_rw1)
f = open(filename_rw1, 'r+')
read_data = f.read()
print('檔案內容: ', read_data)

print("------------------------------------------------------------")  # 60個

print("測試fseek")

f=open(filename_rw1,'rb')
print("目前文件索引位置：",f.tell()) #0
f.seek(6) #移到索引第 6 (第7個字元)位置
string1=f.read(7) #讀取 7 個字元
print(string1)  # b'Python\n'
print("目前文件索引位置：",f.tell()) #13

f.seek(0) #回文件最前端
print("目前文件索引位置：",f.tell()) #0
string2=f.read(5) #讀取 5 個字元
print(string2)  # b'Hello'

f.seek(-8,2) #移至最尾端，向前取 8 個字元
string3=f.read()
print(string3)  # b'Welcome\n'

f.close()

print("------------------------------------------------------------")  # 60個

print("測試fseek ftell")
print("開啟檔案 : " + filename_rw1)
f = open(filename_rw1, "r+")
string = f.read(10);
print("read 10 string is : ", string)

print("讀取檔案 : " + filename_rw1)
position = f.tell();
print("目前檔案位置 : ", position)

print("將檔案位置調到 20")
f.seek(20)

string = f.read(10);
print("讀取10拜 : ", string)

print("將檔案位置調到檔頭")
f.seek(0)
string = f.read(10);
print("讀取10拜 : ", string)
f.close()


filename_rw3 = 'tmp_write_read_text03.bin'

print("讀取一個檔案 binary, 檔名 : " + filename_rw3)
with open(filename_rw3,'rb') as f:
    content=f.read().decode("utf-8") 
    print(content) 

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)
f=open(filename1,'rt')
for line in f:
    print(line,end="")
f.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)
with open(filename1,'r') as f:
    for line in f:
        print(line,end="")
f.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)
with open(filename1,'r') as f:
    string1=f.read(5)
    print(string1)  # Hello
f.close()

print("------------------------------------------------------------")  # 60個

filename2 = 'C:/_git/vcs/_1.data/______test_files1/file2.txt'

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as f:
    print(f.readline())  # 123中文字\n
    print(f.readline(3)) # abc

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)    
with open(filename1, 'r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as f:
    doc=f.readlines() 
    print(doc)      

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename2)    
with open(filename2, 'r', encoding = 'UTF-8') as f:
    string1=f.read(5)
    print(string1)  # 123中

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8-sig') as f:
    string1=f.read(5)
    print(string1)  # 123中文

print("------------------------------------------------------------")  # 60個

print("使用cp950編碼 讀取檔案")
filename_utf8 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/fileUTF8.txt'
f=open(filename_utf8, 'r', encoding = 'cp950')
for line in f:
    print(line, end = "")
f.close()

print("------------------------------------------------------------")  # 60個

#david: 其實也不怎麼對, 後面才對

print('111111111111111111')
f=open(filename_utf8, 'r',encoding ='UTF-8-sig')
print(f.readline())  # 123中文字\n
print(f.readline(3)) # abc
f.close()

print('------------------------------------------------------------')	#60個

#各種檔案寫讀範例

filename = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'

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

filename = "C:/_git/vcs/_4.python/_data/王之渙_涼州詞.big5.txt"

f = open(filename, "r")
while True:
    print('讀一行')
    line = f.readline()
    if len(line) == 0:  #Zero length indicates EOF
        break
    print(line.strip())

f.close()



print("一次讀一行")
filename = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'
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
#f = open(filename, "r+")
f = open(filename, 'r+', encoding = 'utf8')

string = f.read(10);  #讀10拜
print("Read String is : ", string)
# Close opend file
f.close()

#f = open(filename, 'r')
f = open(filename, 'r+', encoding = 'utf8')

string = f.read()
f.close()

print(string)

#print(string.decode('utf-8')) # 這是什麼？
#print(string.decode('utf-8').encode('utf-8')) # 這是什麼？


#從檔案把資料讀出來，一次讀完
#打開一個文件
#f = open(filename, "r")
f = open(filename, 'r', encoding = 'utf8')

#一次讀完資料
string = f.read()
print(string)

#關閉文件
f.close()

print('------------------------------------------------------------')	#60個

#從檔案把資料讀出來，一次讀一行
#打開一個文件
#f = open(filename, "r")
f = open(filename, 'r', encoding = 'utf8')

#一次讀一行
string = f.readline()
print(string)

#一次讀一行
string = f.readline()
print(string)

#一次讀一行
string = f.readline()
print(string)

#關閉文件
f.close()


#從檔案把資料讀出來，一次讀所有行
#打開一個文件
#f = open(filename, "r")
f = open(filename, 'r', encoding = 'utf8')

#一次讀所有行
string = f.readlines()
print(string)

#關閉文件
f.close()

print('------------------------------------------------------------')	#60個


def disp_area():
    i = 0
    for a in climate_data:
        print("{:>2}:{:<6}\t".format(i,a[0]), end="")
        i += 1
        if not (i % 5): print()
    print()

def disp_temp(data):
    print("顯示區域:", data[0])
    print("---------------------")
    for i in range(1,13):
        print("{:>2}月均溫:{:>.1f}度".format(i, float(data[i])))
    print("本地區年均溫為{}度".format(data[13]))
    print("---------------------")


filename = 'C:/_git/vcs/_1.data/______test_files1/data_climate.txt'

with open(filename, 'r', encoding='utf-8') as fp:
    raw_data = fp.readlines()
climate_data=[]
for item in raw_data:
    climate_data.append(item.rstrip('\n').split('\t'))

disp_area()
disp_temp(climate_data[4])

print('------------------------------------------------------------')	#60個

print('各種讀取檔案的方法')

filename = 'C:/_git/vcs/_1.data/______test_files1/Presidents.txt'

# Open file for input
infile = open(filename, "r")
print("(1) Using read(): ")
print(infile.read())
infile.close() # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(2) Using read(number): ")
s1 = infile.read(4)
print(s1)
s2 = infile.read(10)
print(repr(s2))
infile.close() # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(3) Using readline(): ")
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()
print(repr(line1))
print(repr(line2))
print(repr(line3))
print(repr(line4))
infile.close() # Close the input file

# Open file for input
infile = open(filename, "r")
print("\n(4) Using readlines(): ")
print(infile.readlines())
infile.close() # Close the input file

print('------------------------------------------------------------')	#60個

print('指定編碼讀取檔案')

stopWord_filename = 'C:/_git/vcs/_1.data/______test_files1/_jieba/stopWord_test.txt'  #設定自訂詞庫

with open(stopWord_filename, 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   

print(stops)

print('------------------------------------------------------------')	#60個

temperatures = []
with open('data/temperature.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print('取得溫度資料 :\n', temperatures)

print('------------------------------------------------------------')	#60個



filename_rw2 = 'tmp_write_read_text08.txt'


f=open(filename_rw2, 'r',encoding='UTF-8')
for line in f:
    print(line,end="")
f.close()

with open(filename_rw2, 'r',encoding='UTF-8') as f:
    for line in f:
        print(line,end="")


with open(filename_rw2, 'r',encoding='UTF-8') as f:
    string1=f.read(5)
    print(string1)  # Hello


with open(filename_rw2, 'r',encoding='UTF-8') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)



with open(filename_rw2, 'r',encoding ='UTF-8') as f:
    content=f.readlines() 
    print(content)      
    
f=open(filename_rw2, 'r',encoding ='UTF-8')
string1=f.read(5)
print(string1)  # 123中
f.close()


with open(filename_rw2, 'r',encoding ='UTF-8-sig') as f:
    content=f.readlines() 
    print(content)      
    
f=open(filename_rw2, 'r',encoding ='UTF-8-sig')
string1=f.read(5)
print(string1)  # 123中文
f.close()


f=open(filename_rw2, 'r',encoding ='UTF-8-sig')
print(f.readline())  # 123中文字\n
print(f.readline(3)) # abc
f.close()
"""
f=open(filename_rw2, 'r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()
"""

filename_rw3 = 'tmp_write_read_text09.txt'

# Open file for output
outfile = open(filename_rw3, "w")

# Write data to the file
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama")

outfile.close() # Close the output file


filename_rw4 = 'tmp_write_read_text10.txt'
# Open file for appending data
outfile = open(filename_rw4, "a")
outfile.write("\nPython is interpreted\n")
outfile.close() # Close the input file

print('------------------------------------------------------------')	#60個

""" fail
filename = 'tmp_write_read_text11.txt'

# Open file for writing data
outfile = open(filename, "w")
for i in range(10):
    outfile.write(str(random.randint(0, 9)) + " ")
outfile.close() # Close the file

# Open file for reading data
infile = open(filename, "r")
s = infile.read()
numbers = [eval(x) for x in s.split()]
for number in numbers:
    print(number, end = " ")
infile.close() # Close the file
"""

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/Presidents.txt'

fp = open(filename, "r")
zops = fp.readlines()
fp.close()

i=1
print("檔案內容")
for zen in zops:
    print("第 {} 行 : {}".format(i, zen), end="")
    i += 1

print()



print('讀出檔案 1 英文')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_en.txt'
file = open(filename, "r")

content = file.read()
print(content)

file.close()

print('讀出檔案 2 中文')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_ch.txt'
file = open(filename, "r", encoding="utf-8")

content = file.read()
print(content)

file.close()

print('讀出檔案 3')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_en.txt'
file = open(filename, "r")

lines = file.readlines()
print(lines)

file.close()

print('讀出檔案 4')
filename = 'C:/_git/vcs/_1.data/______test_files1/demo_en.txt'
with open(filename, "r") as file:
    content = file.read()
    print(content)


print('寫入檔案')
filename = 'tmp_write_read_text12.txt'

file = open(filename, "a")

file.write("Take me home, country road\n")

file.close()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/quotes.txt'
#filename = 'C:/_git/vcs/_1.data/______test_files1/poetry2.txt'

def get_random_quote():
    start_line  = None
    end_line    = None

    # Open the quote file
    with open(filename) as file:
        line = file.readlines()
        print('total lines = ', str(len(line)))

    # Let's begin with some random line number
    # When '%%' is found, save the line number and break the loop
    for i in range(len(line)-1):
        random_line = (random.randint(0, len(line)-1))
        print(random_line)
        if "%%" in line[random_line]:
            start_line = random_line
            print('break at start', start_line)
            break

    # Find the closest next '%%' line number
    for i in range(start_line+1, len(line)):
        if "%%" in line[i]:
            end_line = i
            print('break at end', end_line)
            break

    # We don't need the '%%' to be printed
    start_line += 1

    # Join all the text between these two '%%'
    quote = "".join(line[start_line:end_line])

    return quote

mesg = get_random_quote()
print(mesg)
mesg = get_random_quote()
print(mesg)
mesg = get_random_quote()
print(mesg)

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW\_txt/python_password2.txt'

import ast

data = dict()
with open(filename,'r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   data = ast.literal_eval(filedata)
print(type(data),data)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = list()
for line in ksvote:
    num_ksvote.append(int(line.strip().replace(",","")))
print(num_ksvote)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = [int(line.strip().replace(",","")) for line in ksvote]
print(num_ksvote)

print('------------------------------------------------------------')	#60個

def fixtype(n):
    return int(n.strip().replace(",",""))

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(fixtype, ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/ksvote.txt'

with open(filename, "r", encoding="utf-8") as f:
    ksvote = f.readlines()
num_ksvote = map(lambda n:int(n.strip().replace(",","")), ksvote)
for vote in num_ksvote:
    print(vote)

print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file1.txt'

f = open(filename1, 'r')
for line in f:
    print(line,end="")
f.close()


with open(filename1, 'r') as f:
    for line in f:
        print(line,end="")


f=open(filename1, 'r')
string1=f.read(5)
print(string1)  # Hello
f.close()

with open(filename1, 'r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)

filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file2.txt'
with open(filename2, 'r',encoding = 'UTF-8') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open(filename2, 'r',encoding = 'UTF-8')
string1=f.read(5)
print(string1)  # 123中
f.close()


with open(filename2, 'r',encoding ='UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open(filename2, 'r',encoding ='UTF-8-sig')
string1=f.read(5)
print(string1)  # 123中文
f.close()

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text13.txt'


filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file3.txt'

f = open(filename)
print(f.readline())
print(f.readline())
#f.close()

f.seek(0)
for line in f:
    print(line.strip())
    
f.close()

with open(filename) as f:
    for line in f:
        print(line.strip())          

filename = 'tmp_write_read_text14.txt'

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file4.txt'
text = open(filename).read().strip()
print(text)

print('----------------------------------------------------')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file3.txt'

text = open(filename).read().strip()
print(text)

print("------------------------------------------------------------")  # 60個

import ast

# 讀取文字檔後轉換為 dict
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_password.txt'

data = dict()

with open(filename, 'r', encoding = 'UTF-8-sig') as f:
    filedata = f.read()
    if filedata != "":
        data = ast.literal_eval(filedata)

print(data)

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print('新增資料 2筆')
data['david'] = '12345678'
data['john'] = '88888888'

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print('檢查資料')

name = 'david'
if not name in data:
    print("{} 帳號不存在!".format(name))
else:
    print("{} 帳號存在!, 修改資料".format(name))
    data[name] = '3333'

name = 'alex'
if not name in data:
    print("{} 帳號不存在!".format(name))
else:
    print("{} 帳號存在!, 修改資料".format(name))
    data[name] = '3333'

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

print('刪除資料')
name = 'david'
del data[name]

print("帳號\t密碼")
print("================")
for key in data:
    print("{}\t{}".format(key, data[key]))

filename2 = 'tmp_write_read_text15_password.txt'

print('將字典寫為檔案')
with open(filename2, 'w', encoding = 'UTF-8-sig') as f:
    f.write(str(data))
print("{}已被儲存完畢".format(name)) 

print("程式執行完畢！")

print("------------------------------------------------------------")  # 60個

def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print("找不到 %s 檔案" % filename)
    else:
        wordList = data.split()     # 將文章轉成串列
        print("檔案 :", filename, "\n字數計算, 單字 :", len(wordList))    # 列印文章字數

filename = 'C:/_git/vcs/_4.python/_data/song1.txt'
wordsNum(filename)

print("------------------------------------------------------------")  # 60個

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

"""    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
"""

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

obj="""五福臨門
十全十美
"""
#建立新檔
filename1 = 'tmp_write_read_text16a.txt'
filename2 = 'tmp_write_read_text16b.txt'

f = open(filename1, 'w')   
f.write(obj)#將字串寫入檔案   
f.close()#關閉檔案

file1=open(filename1,'r')
for line in file1:
    print(line,end='')
file1.close()

""" skip
import os.path

if os.path.isfile('tmp_phrase_new.txt'): #如果檔案存在則取消複製
    print('此檔案已存在,不要複製')
    sys.exit()
else:
    file1=open(filename1,'r')#讀取模式
    file2=open(filename2,'w')#寫入模式
    text=file1.read() #以逐字元的方式讀取檔案
    text=file2.write(text) #寫入檔案
    print('檔案複製成功')
    file1.close() 
    file2.close() 
"""

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

string1 = "黃河遠上白雲間\n"
string2 = "一片孤城萬仞山\n"
string3 = "羌笛何須怨楊柳\n"
string4 = "春風不度玉門關"
strings = [string1, string2, string3, string4]

filename = 'tmp_write_read_text17_poem.cp950.txt'
print("用cp950編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='cp950') as fObj:
    fObj.write(string1)
    fObj.write(string2)
    fObj.write(string3)
    fObj.write(string4)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text17_poem.cp936.txt'
print("用cp936編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='cp936') as fObj:
    fObj.writelines(strings)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text17_poem.utf-8.txt'
print("用utf-8編碼寫一檔, 檔名 :", filename)
with open(filename, 'w', encoding='utf-8') as fObj:
    fObj.writelines(strings)

print("------------------------------------------------------------")  # 60個

poem_text = "黃河遠上白雲間一片孤城萬仞山羌笛何須怨楊柳春風不度玉門關"

filename = 'tmp_write_read_text17_poem.cp950b.txt'
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
filename = 'tmp_write_read_text17_poem.cp950.txt'
fObj = open(filename, 'r', encoding='cp950')    
data = fObj.read()      # 讀取檔案到變數data
fObj.close()            # 關閉檔案物件
print(data)             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

print('一次讀一行')
filename = 'tmp_write_read_text17_poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:    
    for line in fObj:       # 相當於逐列讀取
        print(line)         # 輸出line

print("------------------------------------------------------------")  # 60個

print('一次讀一行 加 rstrip()')
filename = 'tmp_write_read_text17_poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:    
    for line in fObj:           # 相當於逐列讀取
        print(line.rstrip())    # 輸出line

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text17_poem.cp950.txt'
with open(filename, 'r', encoding='cp950') as fObj:
    print("用readline()讀一行")
    string1 = fObj.readline()
    print(string1)

    print("用readline()讀一行")
    string2 = fObj.readline()
    print(string2)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text17_poem.cp950.txt'

print('用readlines()一次讀完全檔 至一個 list')

with open(filename, 'r', encoding='cp950') as fObj:    
    text_list = fObj.readlines()

#print(text_list)
for line in text_list:
    print(line)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text17_poem.cp950b.txt'
with open(filename, 'r', encoding='cp950') as fObj:
    print(f"目前指針位置 {fObj.tell()}")    
    string1 = fObj.read(7)
    print(f"讀出資料 : {string1}, 目前指針位置 {fObj.tell()}")
    string2 = fObj.read(7)
    print(f"讀出資料 : {string2}, 目前指針位置 {fObj.tell()}")
    string3 = fObj.read(7)
    print(f"讀出資料 : {string3}, 目前指針位置 {fObj.tell()}")  

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text17_poem.utf-8.txt'
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






"""
#readlines()可以依照行讀取整個檔案，回傳是一個List，每一個element就是一行字。

file = open("demo_en.txt", "r")

lines = file.readlines()
print(lines)

file.close()
"""

print('------------------------------------------------------------')	#60個

"""
print('一種寫入檔案的方法')
filename = 'tmp_write_read_text18.txt'

fp = open(filename,'w')
print('[OPTIONS]', file=fp)
print('Auto Index=Yes', file=fp)
print('Binary TOC=No', file=fp)
print('Binary Index=Yes', file=fp)
print('Compatibility=1.1', file=fp)
print('Error log file=ErrorLog.log', file=fp)
print('Display compile progress=Yes', file=fp)
print('Full-text search=Yes', file=fp)
print('Default window=main', file=fp)
print('', file=fp)  #寫一個空白列
print('[WINDOWS]', file=fp)
print('main=,"' + '","'
+ '","","",,,,,0x23520,222,0x1046,[10,10,780,560],'
'0xB0000,,,,,,0', file=fp)
print('', file=fp)
print('[FILES]', file=fp)
print('', file=fp)
fp.close()
"""


"""
print('11')
filename = 'engnews.txt'
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline())#讀一行

print('22')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    data = f.read() #讀全部成一行串列

print(repr(data))
print(data)
print(data.split())
data = data.split()
for d in data:
    d.strip()
print(data)

print('33')
filename = 'engnews.txt'    
with open(filename, "r", encoding="utf-8") as f:
    print(f.readlines())#讀全部成多行串列
"""

print("------------------------------------------------------------")  # 60個


"""
file_Obj =  open(filename, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(filename, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
file_Obj =  open(filename, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
with open(filename, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行
with open(filename, encoding='utf-8-sig') as file_Obj:  # 開啟utf-8檔案
    obj_list = file_Obj.readlines()               # 每次讀一行
"""



file = open("tmp_text_file.txt", "w+")

file.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

file.flush()

print("寫入之後的游標位置：", file.tell())

print('往後跳16拜')
file.seek(16, 0)

print('擷取至位置26')
file.truncate(26)

print('讀出來')
print(file.read())

file1=open("tmp_text_file.txt","r")
text=file1.read(1) #以read()方法讀取檔案
print(text)
text=file1.read(3) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
file1.close()


print("------------------------------------------------------------")  # 60個

""" no file
print("讀出檔案最後一行字")

def read_final_line(filename):
    f = open(filename, 'r')
    for line in f:
        pass
    f.close()
    return line

print(read_final_line("../datalogin.log"))
"""
print("------------------------------------------------------------")  # 60個

#統計檔案的字元數、字數與行數

def wordcount(filename):
    result = {
        'Characters': 0,
        'Words': 0,
        'Unique words': 0,
        'Lines': 0,
        }
    unique_words = set()
 
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            result['Lines'] += 1
            result['Characters'] += len(line)
            result['Words'] += len(words)
            unique_words.update(words)
 
        result['Unique words'] = len(unique_words)
 
    for key, value in result.items():
        print(f'{key}: {value}')

wordcount("../data/text.txt")

print('------------------------------------------------------------')	#60個

#找出檔案內的最長單字

def find_longest_word(filename):
    longest = ''
    with open(filename, 'r') as f:
        for line in f:
            for word in line.replace('.', '').split():
                if len(word) > len(longest):
                    longest = word
    return longest

print(find_longest_word("../data/text2.txt"))

print('------------------------------------------------------------')	#60個

#豬拉丁文 --- 檔案翻譯機

def pl_word(word):
    if word[0] in 'aeiou':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

def pl_file(filename):
    with open(filename, 'r') as f:
        return ' '.join([pl_word(word.lower().replace('.', ''))
                         for line in f
                         for word in line.split()])

print(pl_file("../data/text2.txt"))

print('------------------------------------------------------------')	#60個

# 過濾檔案中特定條件的單字

def word_filter(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    with open(filename, 'r') as f:
        words = ([word.replace('.', '')
                  for line in f
                      for word in line.split()
                      if len(set(word) & vowels) >= 3])
    return words

print(word_filter("../data/text2.txt"))

print('------------------------------------------------------------')	#60個

#希伯來數字密碼（Part I + Part II）

import string

def gematria_dict():
    return {char: index
            for index, char
            in enumerate(string.ascii_lowercase, 1)}

GEMATRIA = gematria_dict()

def gematria_value(word):
    return sum(GEMATRIA[char]
               for char in word.lower()
               if char in GEMATRIA)

def gematria_equal_words(my_word, filename):
    my_value = gematria_value(my_word)
    with open(filename, 'r', encoding='utf-8') as f:
        return [word
                for line in f
                for word in line.lower().split()
                if my_value == gematria_value(word)]

print(gematria_equal_words('programming', "../data/book.txt"))

print('------------------------------------------------------------')	#60個

# 檔案單字產生器

def word_generator(filename, max_words):
    index = 0
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if index >= max_words:
                    return
                yield word.replace('.', '')
                index += 1

ten_words = word_generator("../data/text2.txt", 10)

for word in ten_words:
    print(word)

print('------------------------------------------------------------')	#60個

print('直接 print 到檔案')

filename = 'tmp_write_read_text19.txt'

with open(filename, 'wt') as f:
    print('Hello World!', file = f)

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/Romeo&Juliet.txt'

infile = open(filename, 'r')

count = 0
for line in infile:
    string1 = line.strip()
    if len(string1)>0:
        count += 1

print('total', count, 'lines')
infile.close()

print("------------------------------------------------------------")  # 60個

def distinctNN(n):
    set1 = set()
    for i in range(2, n+1):
        for j in range(1, n+1):
            set1.add(i*j)
    return set1

def doOutput(filename, outlist):
    outfile = open(filename, 'w')
    
    count = 0
    for num in outlist:
        outfile.write(str(num)+' ')
        count += 1
        if count%5==0:
            outfile.write('\n')
            
    outfile.close()
    print(filename+' created')

setNN = distinctNN(19)
list1 = sorted(list(setNN))
#print(list1)

filename = 'tmp_write_read_text20.txt'

doOutput(filename, list1)

print("------------------------------------------------------------")  # 60個

"""
filename = 'tmp_write_read_text21.txt'
filename = 'myfile.txt'
inf = open(filename, 'r')
outfilename = filename[:-4]+'2.txt'
outf = open(outfilename, 'w')

for line in inf:           # 讀進來的line字串是有包含檔案內的換行字元哦！
    string1 = line.strip()    # 移除line的多餘空白
    if len(string1)>0:        # 如果移除完還有內容，寫進輸出檔
        outf.write(string1+'\n')
inf.close()
outf.close()
"""

print("------------------------------------------------------------")  # 60個

filename = '../data/en-us2.log'
infile = open(filename, 'r')

# 前50行
count = 0
for line in infile:
    if count>=50:
        break
    print((count+1), line, end='')
    count += 1
    
infile.close()

print("------------------------------------------------------------")  # 60個

""" many

filename = 'C:/_git/vcs/_4.python/_data/Romeo&Juliet.txt'
infile = open(filename, 'r')

count = 0
string1 = infile.readline()
len1 = len(string1)
while len1>0:
    count += 1
    print(count, string1.strip())
    string1 = infile.readline()
    len1 = len(string1)
    

print('total', count, 'lines')
infile.close()
"""

"""
with open("myfile.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
        
# 不用關檔了！！
"""
print("------------------------------------------------------------")  # 60個



"""
从文本文件中读取数据

"""

""" fail

def main():
    # 一次性读取整个文件内容
    with open('data/致橡树.txt', 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open('data/致橡树.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()

    # 读取文件按行读取到列表中
    with open('data/致橡树.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()
"""

print("------------------------------------------------------------")  # 60個

print('读取圆周率文件判断其中是否包含自己的生日')

birth = "0311"
with open('data/pi_million_digits.txt') as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')

sys.exit()

print("------------------------------------------------------------")  # 60個


# 處理劇本中的單一句子，去除標點並切割
def processString(str1):
    tup1 = (',', '.', ';', '?', '!', "'", '-', ':')
    strK = str1
    #Why, such is love's transgression. 要轉換成：
    #Why  such is love s transgression 然後用空白切割
    for tok in tup1:
        strK = strK.replace(tok, ' ')
    strK = strK.lower()
    slist = strK.split()
    # 串列生成，將兩個字母以上的文字以及a和i留下
    slist2 = [s for s in slist if len(s)>1 or s=='a' or s=='i']
    return slist2

filename = 'C:/_git/vcs/_4.python/_data/Romeo&Juliet.txt'

infile = open(filename, 'rt', encoding='utf-8')

freq = {}
for line in infile:
    string1 = line.strip()
    # 處理劇本中的單一句子，去除標點並切割
    slist = processString(string1)
    # 將切好的詞彙紀錄頻率
    for tok in slist:
        freq[tok] = freq.get(tok, 0)+1
infile.close()

# 開始找尋最長以及最常的詞彙
longest = ''    # 最長
maxoccur = ''    # 最常
maxv = 0
for k, v in freq.items():
    # 比出目前最長
    if len(k)>len(longest):
        longest = k
    # 比出目前最常
    if v>maxv:
        maxoccur = k
        maxv = v
        
print('最長用詞:', longest, ', 長度', len(longest))
print('最頻繁用詞:', maxoccur, ', 次數', maxv)

print('------------------------------------------------------------')	#60個

filename = '../data/DatingTestSet.txt'
stat = {}
tags = ['largeDoses', 'smallDoses', 'didntLike']
with open(filename, 'rt', encoding='utf-8') as inf:
    for line in inf:
        slist = line.strip().split('\t')
        try:
            idx = tags.index(slist[-1])
            key = tags[idx]
            stat[key] = stat.get(key, 0)+1
        except:
            # 沒出現過的tag使用index()方法
            # 會產生ValueError例外，跳過
            pass

# 使用串列生成加上sum()來找出總數
sum1 = sum([v for v in stat.values()])
for k, v in stat.items():
    # 計算百分比並完成輸出
    stat[k] = 100.0*v/sum1
    print(k+':', str(stat[k])+'%')
    
print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'
#filename = 'C:/_git/vcs/_1.data/______test_files1/quotes.txt'

fp = open(filename, 'r', encoding = 'UTF-8')
try:
    while 1:
        line = fp.readline()
        if not line:
            break
        print(line, end = '')
finally:
    fp.close()

print('------------------------------------------------------------')	#60個
with open(filename, 'r', encoding = 'UTF-8') as file:
    line = file.readlines()
#print(line)
    
for l in line:
    #print(l, end ="")
    print(l[:3])    #每行的前三字
    print(l[3:])    #每行的第三字開始到最後
    
print('------------------------------------------------------------')	#60個

"""
fp = open(filename, 'r', encoding = 'UTF-8')
line = fp.readlines()
fp.close()

print(line)
"""

print('------------------------------------------------------------')	#60個


def wordsNum(filename):
    """適用英文文件, 輸入文章的檔案名稱,可以計算此文章的字數"""
    try:
        with open(filename) as file_Obj:  # 用預設mode=r開啟檔案
            data = file_Obj.read()  # 讀取檔案到變數data
    except FileNotFoundError:
        print(f"找不到 {filename} 檔案")
    else:
        wordList = data.split()     # 將文章轉成串列
        print(f"{filename} 文章的字數是 {len(wordList)}")   # 文章字數

file = 'data15_5.txt'               # 設定欲開啟的檔案
wordsNum(file)

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

# 新進


filename = 'data2/ch14_20.txt'              # 設定欲開啟的檔案
with open(filename) as file_Obj:      # 傳回檔案物件file_Obj
    data = file_Obj.read()      # 讀取檔案到變數data
    new_data = data.replace('工專', '科大') # 新變數儲存
    print(new_data.rstrip())    # 輸出檔案

print("------------------------------------------------------------")  # 60個

filename = 'data2/sse.txt'              # 設定欲開啟的檔案
with open(filename) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入
    str_Obj += line.rstrip()

print("欲搜尋字串")
findstr = "aaaa"
if findstr in str_Obj:      # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, filename))
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, filename))

print("------------------------------------------------------------")  # 60個

filename = 'data2/sse.txt'              # 設定欲開啟的檔案

with open(filename) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
    obj_list = file_Obj.readlines()  # 每次讀一行

str_Obj = ''                # 先設為空字串
for line in obj_list:       # 將各行字串存入
    str_Obj += line.rstrip()

print("欲搜尋字串")
findstr = "aaaa"
index = str_Obj.find(findstr)     # 搜尋findstr字串是否存在
if  index >= 0:             # 搜尋檔案是否有欲尋找字串
    print("搜尋 %s 字串存在 %s 檔案中" % (findstr, filename))
    print("在索引 %s 位置出現" % index)
else:
    print("搜尋 %s 字串不存在 %s 檔案中" % (findstr, filename))

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text22.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(filename, 'w') as file_Obj:
    file_Obj.write(str1)
    file_Obj.write(str2)

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text23.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(filename, 'w') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')

print("------------------------------------------------------------")  # 60個

filename = 'tmp_write_read_text24.txt'
str1 = 'I love Python.'
str2 = 'Learn Python from the best book.'

with open(filename, 'a') as file_Obj:
    file_Obj.write(str1 + '\n')
    file_Obj.write(str2 + '\n')

print("------------------------------------------------------------")  # 60個

""" no file
filename = 'data2/ansi14_44.txt'                    # 設定欲開啟的檔案
file_Obj =  open(filename, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案
"""

print("------------------------------------------------------------")  # 60個

"""
filename = 'data2/utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(filename, encoding='cp950')  # 用預設encoding='cp950'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案
"""
print("------------------------------------------------------------")  # 60個

filename = 'data2/utf14_45.txt'                     # 設定欲開啟的檔案
file_Obj =  open(filename, encoding='utf-8')  # 用encoding='utf-8'開啟檔案
data = file_Obj.read()                  # 讀取檔案到變數data
file_Obj.close()                        # 關閉檔案物件
print(data)                             # 輸出變數data相當於輸出檔案

print("------------------------------------------------------------")  # 60個

filename = 'data2/utf14_45.txt'                             # 設定欲開啟的檔案
with open(filename, encoding='utf-8') as file_Obj:    # 開啟utf-8檔案
    obj_list = file_Obj.readlines()             # 每次讀一行

print(obj_list)                                 # 列印串列

print("------------------------------------------------------------")  # 60個

filename = 'data2/data14_8.txt'         # 設定欲開啟的檔案

with open(filename, 'r', encoding='cp950') as fObj:
    print(f"指針位置 {fObj.tell()}")    
    txt1 = fObj.read(3)
    print(f"{txt1}, 指針位置 {fObj.tell()}")
    txt2 = fObj.read(3)
    print(f"{txt2}, 指針位置 {fObj.tell()}")
    txt3 = fObj.read(3)
    print(f"{txt3}, 指針位置 {fObj.tell()}")     

print('------------------------------------------------------------')	#60個

filename = 'data2/data14_9.txt'             # 設定欲開啟的檔案

chunk = 100
msg = ''
with open(filename, 'r', encoding='cp950') as fObj: 
    while True:
        txt = fObj.read(chunk)  # 一次讀取chunk數量
        if not txt:
            break
        msg += txt
print(msg)

print('------------------------------------------------------------')	#60個

print('寫入檔案')
fp = open("tmp_write_read_text25.txt", "w") 
print("用print的方法寫入檔案", file=fp)
fp.close( )

print('------------------------------------------------------------')	#60個

print('寫入檔案')
filename = 'tmp_write_read_text26.txt'
str1 = '寫入檔案字串1'
str2 = '寫入檔案字串2'

#with open(filename, 'w') as fp:    #覆寫模式
with open(filename, 'a') as fp:     #附加模式
    fp.write(str1 + '\n')
    fp.write(str2 + '\n')

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一檔')
filename = 'data2/data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    data = fp.read()  # 讀取檔案到變數data
    print(data)             # 輸出變數data相當於輸出檔案

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一行')
filename = 'data2/data14_2.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    for line in fp:   # 逐行讀取檔案到變數line
        print(line)         # 輸出變數line相當於輸出一行

print('------------------------------------------------------------')	#60個

print('讀取檔案, 一次讀一檔, 讀成串列')
filename = 'data2/data14_7.txt'         # 設定欲開啟的檔案
with open(filename) as fp:  # 用預設mode=r開啟檔案,傳回檔案物件fp
    obj_list = fp.readlines()  # 每次讀一行

print(len(obj_list))
print(obj_list)             # 列印串列

for line in obj_list:
    print(line.rstrip())    # 列印串列



print("------------------------------------------------------------")  # 60個




def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    for wd in songList:
        if wd in dict:
            dict[wd] += 1
        else:
            dict[wd] = 1

filename = "data2/ch14_51.txt"
with open(filename) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案
    print("以下是所讀取的歌曲")
    print(data)                     # 列印歌曲檔案

dict = {}                           # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(dict)                         # 列印字典

print("------------------------------------------------------------")  # 60個

def passWord(pwd):
    #檢查密碼長度必須是5到8個字元
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception('密碼長度不足')
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception('密碼長度太長')
    print('密碼長度正確')

for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        print("密碼長度檢查異常發生: ", str(err))

print("------------------------------------------------------------")  # 60個

#filename = 'C:/_git/vcs/_1.data/______test_files1/poetrya.txt'

def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    for wd in songList:
        if wd in mydict:
            mydict[wd] += 1
        else:
            mydict[wd] = 1

filename = "data2/data14_17.txt"
with open(filename) as fp:          # 開啟歌曲檔案
    data = fp.read()          # 讀取歌曲檔案
    print("以下是所讀取的歌曲")
    print(data)                     # 列印歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典

print('------------------------------------------------------------')	#60個

def modifySong(songStr):            # 將歌曲的標點符號用空字元取代       
    for ch in songStr:
        if ch in ".,?":
            songStr = songStr.replace(ch,'')
    return songStr                  # 傳回取代結果

def wordCount(songCount):
    global mydict
    songList = songCount.split()    # 將歌曲字串轉成串列
    print("以下是歌曲串列")
    print(songList)
    mydict = {wd:songList.count(wd) for wd in set(songList)}

filename = "data2/AreYouSleeping.txt"
with open(filename) as file_Obj:          # 開啟歌曲檔案
    data = file_Obj.read()          # 讀取歌曲檔案
    print("以下是所讀取的歌曲")
    print(data)                     # 列印歌曲檔案

mydict = {}                         # 空字典未來儲存單字計數結果
print("以下是將歌曲大寫字母全部改成小寫同時將標點符號用空字元取代")
song = modifySong(data.lower())
print(song)

wordCount(song)                     # 執行歌曲單字計數
print("以下是最後執行結果")
print(mydict)                       # 列印字典


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



filename = "C:/_git/vcs/_4.python/_data/王之渙_涼州詞.big5.txt"

f = open(filename, "r")
all_lines = f.readlines()
print(all_lines)

print("------------------------------------------------------------")  # 60個

"""
製作 log 檔
每執行一次, 存一筆資料在log檔

"""

print("------------------------------------------------------------")  # 60個

with open('tmp_my_logfile1.log', 'a') as log_file:
    log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - 寫了一筆工作紀錄\n')

print("------------------------------------------------------------")  # 60個

#製作log檔的範例
print('存檔紀念')

fp = open('tmp_my_logfile2.txt', 'w')
fp.write("# BUILD INFO\n")
fp.write("# Date: %s\n" % time.ctime())
fp.close()

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




