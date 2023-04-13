#各種檔案寫讀範例 txt 1

filename_rw1 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/sample1.txt'

print("將字串寫入檔案 : " + filename_rw1)
fo = open(filename_rw1, 'w')
fo.write('ABCDE')
fo.write('FGHIJ')
fo.write('KLMNO')
fo.write('PQRST')
fo.close()

print("讀取檔案 : " + filename_rw1)
fo = open(filename_rw1, 'r')
read_data = fo.read()
fo.close()
print('檔案內容: ', read_data)

print("附加檔案 : " + filename_rw1)
fo = open(filename_rw1, 'a') 
fo.write('UVWXYZ')
fo.close()

print("讀取檔案 : " + filename_rw1)
fo = open(filename_rw1, 'r+')
read_data = fo.read()
print('檔案內容: ', read_data)

'''
with open(filename_rw1, 'w') as fo:
	fo.write('using with!')
'''

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

filename_rw2 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/sample2.txt'

print("寫入檔案 : " + filename_rw2)
fo = open(filename_rw2, "w")
fo.write("abcdefghijklmnopqrstuvwxyz");
fo.close()

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

filename_rw3 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/file.bin'

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

filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/file1.txt'

print("建立一個檔案")

content='''Hello Python
中文字測試
Welcome
'''

fo = open(filename1,'w')
fo.write(content)
fo.close()


print("讀取檔案 " + filename1)
fo=open(filename1,'rt')
for line in fo:
    print(line,end="")
fo.close()

print("讀取檔案 " + filename1)
with open(filename1,'r') as fo:
    for line in fo:
        print(line,end="")
fo.close()

print("讀取檔案 " + filename1)
with open(filename1,'r') as fo:
    str1=fo.read(5)
    print(str1)  # Hello
fo.close()

filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/data/file2.txt'

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as fo:
    print(fo.readline())  # 123中文字\n
    print(fo.readline(3)) # abc

print("讀取檔案 " + filename1)    
with open(filename1, 'r') as fo:
    content=fo.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  

print("讀取檔案 " + filename2)
with open(filename2, 'r', encoding = 'UTF-8') as fo:
    doc=fo.readlines() 
    print(doc)      

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

print("使用cp950編碼 讀取檔案")
filename_utf8 = 'C:/_git/vcs/_4.cmpp/_python_test/data/fileUTF8.txt'
fo=open(filename_utf8, 'r', encoding = 'cp950')
for line in fo:
    print(line, end = "")
fo.close()




#各種檔案寫讀範例 txt 2

print("附加模式寫檔案")
filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/TestFileW1.txt'
fo = open(filename_w, "a")
data = "123456789\n"
fo.write(data)
fo.close()

print("寫入檔案範例")
filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/TestFileW2.txt'

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

filename_r = 'C:/_git/vcs/_4.cmpp/_python_test/data/poetry.txt'
filename_w = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/poetry_another.txt'

with open(filename_r, 'rt', encoding = 'utf8') as fo:
    data = fo.read()
    
print("data :\n", data)

fo.close()

with open(filename_w, 'wt') as fo:
    fo.write(data)
    
fo.close()


#各種檔案寫讀範例

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/poetry.txt'

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


filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/data_climate.txt'

with open(filename, 'r', encoding='utf-8') as fp:
    raw_data = fp.readlines()
climate_data=[]
for item in raw_data:
    climate_data.append(item.rstrip('\n').split('\t'))

disp_area()
disp_temp(climate_data[4])


print('各種讀取檔案的方法')

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/Presidents.txt'

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


print('指定編碼讀取檔案')
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/stopWord_test.txt'
with open(filename, 'r', encoding='utf-8-sig') as f:  #設定停用詞
    stops = f.read().split('\n')   

print(stops)



print('測試完成')

    



