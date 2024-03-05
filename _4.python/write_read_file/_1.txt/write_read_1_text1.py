#各種檔案寫讀範例 txt 1

import sys

print('------------------------------------------------------------')	#60個

filename_rw1 = 'tmp_ABC.txt'

print("將字串寫入檔案 : " + filename_rw1)
fo = open(filename_rw1, 'w')
fo.write('ABCDE')
fo.write('FGHIJ')
fo.write('KLMNO')
fo.write('PQRST')
fo.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 : " + filename_rw1)
fo = open(filename_rw1, 'r')
read_data = fo.read()
fo.close()
print('檔案內容: ', read_data)

print("------------------------------------------------------------")  # 60個

print("附加檔案 : " + filename_rw1)
fo = open(filename_rw1, 'a') 
fo.write('UVWXYZ')
fo.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 : " + filename_rw1)
fo = open(filename_rw1, 'r+')
read_data = fo.read()
print('檔案內容: ', read_data)

'''
with open(filename_rw1, 'w') as fo:
	fo.write('using with!')
'''

print("------------------------------------------------------------")  # 60個

print("測試fseek")

fo=open(filename_rw1,'rb')
print("目前文件索引位置：",fo.tell()) #0
fo.seek(6) #移到索引第 6 (第7個字元)位置
str1=fo.read(7) #讀取 7 個字元
print(str1)  # b'Python\n'
print("目前文件索引位置：",fo.tell()) #13

fo.seek(0) #回文件最前端
print("目前文件索引位置：",fo.tell()) #0
str2=fo.read(5) #讀取 5 個字元
print(str2)  # b'Hello'

fo.seek(-8,2) #移至最尾端，向前取 8 個字元
str3=fo.read()
print(str3)  # b'Welcome\n'

fo.close()

print("------------------------------------------------------------")  # 60個

filename_rw2 = 'tmp_text2.txt'

print("寫入檔案 : " + filename_rw2)
fo = open(filename_rw2, "w")
fo.write("abcdefghijklmnopqrstuvwxyz");
fo.close()

print("------------------------------------------------------------")  # 60個

print("開啟檔案 : " + filename_rw2)
fo = open(filename_rw2, "r+")
str = fo.read(10);
print("read 10 string is : ", str)

print("讀取檔案 : " + filename_rw2)
position = fo.tell();
print("目前檔案位置 : ", position)

print("將檔案位置調到 20")
fo.seek(20)

str = fo.read(10);
print("讀取10拜 : ", str)

print("將檔案位置調到檔頭")
fo.seek(0)
str = fo.read(10);
print("讀取10拜 : ", str)
fo.close()

filename_rw3 = 'tmp_file.bin'

print("建立一個檔案 binary, 檔名 : " + filename_rw3)
content='''Hello Python
中文字測試
Welcome
'''

content=content.encode("utf-8") #轉成 bytes
with open(filename_rw3,'wb') as fo:
    fo.write(content)

print("讀取一個檔案 binary, 檔名 : " + filename_rw3)
with open(filename_rw3,'rb') as fo:
    content=fo.read().decode("utf-8") 
    print(content) 

print("------------------------------------------------------------")  # 60個

filename1 = 'C:/_git/vcs/_1.data/______test_files2/file1.txt'

print("建立一個檔案")

content='''Hello Python
中文字測試
Welcome
'''

fo = open(filename1,'w')
fo.write(content)
fo.close()


print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)
fo=open(filename1,'rt')
for line in fo:
    print(line,end="")
fo.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)
with open(filename1,'r') as fo:
    for line in fo:
        print(line,end="")
fo.close()

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)
with open(filename1,'r') as fo:
    str1=fo.read(5)
    print(str1)  # Hello
fo.close()

print("------------------------------------------------------------")  # 60個

filename2 = 'C:/_git/vcs/_1.data/______test_files1/file2.txt'

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as fo:
    print(fo.readline())  # 123中文字\n
    print(fo.readline(3)) # abc

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename1)    
with open(filename1, 'r') as fo:
    content=fo.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as fo:
    doc=fo.readlines() 
    print(doc)      

print("------------------------------------------------------------")  # 60個

print("讀取檔案 " + filename2)    
with open(filename2, 'r', encoding = 'UTF-8') as fo:
    str1=fo.read(5)
    print(str1)  # 123中

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8-sig') as fo:
    doc=fo.readlines() 
    print(doc)      

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8-sig') as fo:
    str1=fo.read(5)
    print(str1)  # 123中文

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

#各種檔案寫讀範例 txt 2

print("附加模式寫檔案")
filename_w = 'C:/_git/vcs/_1.data/______test_files2/TestFileW1.txt'
fo = open(filename_w, "a")
data = "123456789\n"
fo.write(data)
fo.close()

print("------------------------------------------------------------")  # 60個

print("寫入檔案範例")
filename_w = 'C:/_git/vcs/_1.data/______test_files2/TestFileW2.txt'

#寫資料到檔案中
#打開一個文件
fo = open(filename_w, "w")

#寫資料
num = fo.write("python讀和寫文件python讀和寫文件\npython讀和寫文件python讀和寫文件\n")

print("總共寫了 ", num, " 拜")

#關閉文件
fo.close()

print("讀取一檔並將資料寫到另檔的範例")

#python讀和寫文件

filename_r = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'
filename_w = 'C:/_git/vcs/_1.data/______test_files2/poetry_another.txt'

with open(filename_r, 'rt', encoding = 'utf8') as fo:
    data = fo.read()
    
print("data :\n", data)

fo.close()

with open(filename_w, 'wt') as fo:
    fo.write(data)
    
fo.close()

print('------------------------------------------------------------')	#60個

#各種檔案寫讀範例

filename = 'C:/_git/vcs/_1.data/______test_files1/poetry.txt'

print("讀取檔案 : "+filename)

fo = open(filename, 'r', encoding = 'utf8')
#fo = open(filename, 'r', encoding = 'UTF-8')

print("檔名: ", fo.name)
for line in fo.readlines():
    #line = line.strip
    print(line)
fo.close


print("一次讀完一檔")
#fo = open(filename, 'r')
fo = open(filename, 'r', encoding = 'utf8')
line = fo.readlines()
print(line),
fo.close()

print("一次讀一行")
#fo = open(filename, 'r')
fo = open(filename, 'r', encoding = 'utf8')
i = 0
while True:
    line = fo.readline()
    if len(line) == 0:  #Zero length indicates EOF
        break;
    i = i + 1
    #print(str(i), line),    # Notice comma to avoid automatic newline added by Python
    print(line),
fo.close()

print("一次讀一行")
#fo = open(filename, 'r')
fo = open(filename, 'r', encoding = 'utf8')
for line in fo: print(line) #通過迭代器訪問
fo.close()

print("讀前10拜")
#fo = open(filename, "r+")
fo = open(filename, 'r+', encoding = 'utf8')

str = fo.read(10);  #讀10拜
print("Read String is : ", str)
# Close opend file
fo.close()

#fo = open(filename, 'r')
fo = open(filename, 'r+', encoding = 'utf8')

b_str = fo.read()
fo.close()

print(b_str)

#print(b_str.decode('utf-8')) # 這是什麼？
#print(b_str.decode('utf-8').encode('utf-8')) # 這是什麼？


#從檔案把資料讀出來，一次讀完
#打開一個文件
#fo = open(filename, "r")
fo = open(filename, 'r', encoding = 'utf8')

#一次讀完資料
str = fo.read()
print(str)

#關閉文件
fo.close()

print('------------------------------------------------------------')	#60個

#從檔案把資料讀出來，一次讀一行
#打開一個文件
#fo = open(filename, "r")
fo = open(filename, 'r', encoding = 'utf8')

#一次讀一行
str = fo.readline()
print(str)

#一次讀一行
str = fo.readline()
print(str)

#一次讀一行
str = fo.readline()
print(str)

#關閉文件
fo.close()


#從檔案把資料讀出來，一次讀所有行
#打開一個文件
#fo = open(filename, "r")
fo = open(filename, 'r', encoding = 'utf8')

#一次讀所有行
str = fo.readlines()
print(str)

#關閉文件
fo.close()

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
filename = 'C:/_git/vcs/_1.data/______test_files1/stopWord_test.txt'
with open(filename, 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   

print(stops)


print('------------------------------------------------------------')	#60個

temperatures = []
with open('data/temperature.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))

print('取得溫度資料 :\n', temperatures)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

filename_rw2 = 'C:/_git/vcs/_1.data/______test_files2/sample5.txt'

content='''Hello Python
中文字測試
Welcome
'''

f=open(filename_rw2, 'w')
f.write(content)
f.close()


content='''Hello Python
中文字測試
Welcome
'''

f=open(filename_rw2, 'w',encoding='UTF-8')
f.write(content)
f.close()



f=open(filename_rw2, 'r',encoding='UTF-8')
for line in f:
    print(line,end="")
f.close()

with open(filename_rw2, 'r',encoding='UTF-8') as f:
    for line in f:
        print(line,end="")


with open(filename_rw2, 'r',encoding='UTF-8') as f:
    str1=f.read(5)
    print(str1)  # Hello


with open(filename_rw2, 'r',encoding='UTF-8') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)



with open(filename_rw2, 'r',encoding ='UTF-8') as f:
    content=f.readlines() 
    print(content)      
    
f=open(filename_rw2, 'r',encoding ='UTF-8')
str1=f.read(5)
print(str1)  # 123中
f.close()


with open(filename_rw2, 'r',encoding ='UTF-8-sig') as f:
    content=f.readlines() 
    print(content)      
    
f=open(filename_rw2, 'r',encoding ='UTF-8-sig')
str1=f.read(5)
print(str1)  # 123中文
f.close()


f=open(filename_rw2, 'r',encoding ='UTF-8-sig')
print(f.readline())  # 123中文字\n
print(f.readline(3)) # abc
f.close()
'''
f=open(filename_rw2, 'r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()
'''

filename_rw3 = 'C:/_git/vcs/_1.data/______test_files2/Presidents.txt'

# Open file for output
outfile = open(filename_rw3, "w")

# Write data to the file
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama")

outfile.close() # Close the output file


filename_rw4 = 'C:/_git/vcs/_1.data/______test_files2/Info.txt'
# Open file for appending data
outfile = open(filename_rw4, "a")
outfile.write("\nPython is interpreted\n")
outfile.close() # Close the input file



import random

filename = 'C:/_git/vcs/_1.data/______test_files2/numbers.txt'

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
filename = 'C:/_git/vcs/_1.data/______test_files2/demo_en222.txt'

file = open(filename, "a")

file.write("Take me home, country road\n")

file.close()




print('測試完成')

    




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\write_read_file\_1.txt\write_read_1_text3.py

from random import randint

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
        random_line = (randint(0, len(line)-1))
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

#檔案 : C:\_git\vcs\_4.python\write_read_file\_1.txt\write_read_1_text4.py

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW\_txt/python_password2.txt'

import ast

data = dict()
with open(filename,'r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   data = ast.literal_eval(filedata)
print(type(data),data)


print('------------------------------------------------------------')	#60個






import os
import sys

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


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\write_read_file\_1.txt\write_read_1_text5.py

filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file1.txt'


f = open(filename1, 'r')
for line in f:
    print(line,end="")
f.close()


with open(filename1, 'r') as f:
    for line in f:
        print(line,end="")


f=open(filename1, 'r')
str1=f.read(5)
print(str1)  # Hello
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
str1=f.read(5)
print(str1)  # 123中
f.close()


with open(filename2, 'r',encoding ='UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open(filename2, 'r',encoding ='UTF-8-sig')
str1=f.read(5)
print(str1)  # 123中文
f.close()







        

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\write_read_file\_1.txt\write_read_1_text6.py

'''
模式有

r - 讀取(檔案需存在)

w - 新建檔案寫入(檔案可不存在，若存在則清空)

a - 資料附加到舊檔案後面(游標指在EOF)
'''

filename = 'C:/_git/vcs/_1.data/______test_files2/test_write1.txt'

f = open(filename, 'a', encoding = 'UTF-8')   # 也可使用指定路徑等方式，如： C:\A.txt
f.write('你好1\n')
f.write('你好2\n')
f.write('你好3\n')
f.close()

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


filename = 'C:/_git/vcs/_1.data/______test_files2/test_write2.txt'
# write to test_write.txt
# Write a file
with open(filename, "w") as out_file:
    out_file.write("This Text is going to out file\nLook at it and see!")



filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file4.txt'
text = open(filename).read().strip()
print(text)

print('----------------------------------------------------')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file3.txt'

text = open(filename).read().strip()
print(text)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\write_read_file\_1.txt\write_read_1_text7_dict.py

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


filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_password2222.txt'

print('將字典寫為檔案')
with open(filename2, 'w', encoding = 'UTF-8-sig') as f:
    f.write(str(data))
print("{}已被儲存完畢".format(name)) 
 
print("程式執行完畢！")

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個





