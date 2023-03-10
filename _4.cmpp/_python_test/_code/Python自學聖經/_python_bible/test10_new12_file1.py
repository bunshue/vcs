# Python 新進測試 12

print("cp -r data/oswalk ___tmpdata/oswalk222")
import shutil
#shutil.copytree("data\oswalk", "___tmpdata\oswalk222" )  # 目錄複製

filename_rw = '__temp\file.bin'

print("建立一個檔案 binary")
content='''Hello Python
中文字測試
Welcome
'''

content=content.encode("utf-8") #轉成 bytes
with open(filename_rw,'wb') as f:
    f.write(content)


print("讀取一個檔案 binary")
with open(filename_rw,'rb') as f:
    content=f.read().decode("utf-8") 
    print(content) 


filename1 = '__temp\file1.txt'
filename2 = '__temp\file2.txt'

print("建立一個檔案")

content='''Hello Python
中文字測試
Welcome
'''

f=open(filename1,'w')
f.write(content)
f.close()


print("讀取檔案 " + filename1)
f=open(filename1,'rt')
for line in f:
    print(line,end="")
f.close()


print("讀取檔案 " + filename1)
with open(filename1,'r') as f:
    for line in f:
        print(line,end="")

print("讀取檔案 " + filename1)
with open(filename1,'r') as f:
    str1=f.read(5)
    print(str1)  # Hello
    
print("讀取檔案 " + filename2)
with open(filename2,'r',encoding ='UTF-8') as f:
    print(f.readline())  # 123中文字\n
    print(f.readline(3)) # abc

print("讀取檔案 " + filename1)    
with open(filename1,'r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  

print("讀取檔案 " + filename2)
with open(filename2,'r',encoding ='UTF-8') as f:
    doc=f.readlines() 
    print(doc)      

print("讀取檔案 " + filename2)    
with open(filename2,'r',encoding ='UTF-8') as f:
    str1=f.read(5)
    print(str1)  # 123中

print("讀取檔案 " + filename2)
with open(filename2,'r',encoding ='UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      

print("讀取檔案 " + filename2)
with open(filename2,'r',encoding ='UTF-8-sig') as f:
    str1=f.read(5)
    print(str1)  # 123中文


print("測試fseek")
# filename_rw 內容
'''Hello Python
中文字測試
Welcome
'''

f=open(filename_rw,'rb')
print("目前文件索引位置：",f.tell()) #0
f.seek(6) #移到索引第 6 (第7個字元)位置
str1=f.read(7) #讀取 7 個字元
print(str1)  # b'Python\n'
print("目前文件索引位置：",f.tell()) #13

f.seek(0) #回文件最前端
print("目前文件索引位置：",f.tell()) #0
str2=f.read(5) #讀取 5 個字元
print(str2)  # b'Hello'

f.seek(-8,2) #移至最尾端，向前取 8 個字元
str3=f.read()
print(str3)  # b'Welcome\n'

f.close()


print("使用cp950編碼 讀取檔案")
f=open('data\fileUTF8.txt','r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()



    
