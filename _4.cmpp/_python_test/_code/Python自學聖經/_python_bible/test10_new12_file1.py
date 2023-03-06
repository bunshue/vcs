# Python 新進測試 12

print("cp -r oswalk oswalk222")
import shutil
#shutil.copytree("oswalk","oswalk222" )  # 目錄複製



print("建立一個檔案 binary")
content='''Hello Python
中文字測試
Welcome
'''

'''
content=content.encode("utf-8") #轉成 bytes
with open('file.bin','wb') as f:
    f.write(content)
'''


'''
print("讀取一個檔案 binary")
with open('file.bin','rb') as f:
    content=f.read().decode("utf-8") 
    print(content) 
'''

print("建立一個檔案")

content='''Hello Python
中文字測試
Welcome
'''

'''
f=open('file1.txt','w')
f.write(content)
f.close()
'''        

print("讀取檔案 file1.txt")
f=open('file1.txt','rt')
for line in f:
    print(line,end="")
f.close()


print("讀取檔案 file1.txt")
with open('file1.txt','r') as f:
    for line in f:
        print(line,end="")

print("讀取檔案 file1.txt")
with open('file1.txt','r') as f:
    str1=f.read(5)
    print(str1)  # Hello
    
print("讀取檔案 file2.txt")
with open('file2.txt','r',encoding ='UTF-8') as f:
    print(f.readline())  # 123中文字\n
    print(f.readline(3)) # abc

print("讀取檔案 file1.txt")    
with open('file1.txt','r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  

print("讀取檔案 file2.txt")
with open('file2.txt','r',encoding ='UTF-8') as f:
    doc=f.readlines() 
    print(doc)      

print("讀取檔案 file2.txt")    
with open('file2.txt','r',encoding ='UTF-8') as f:
    str1=f.read(5)
    print(str1)  # 123中

print("讀取檔案 file2.txt")
with open('file2.txt','r',encoding ='UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      

print("讀取檔案 file2.txt")
with open('file2.txt','r',encoding ='UTF-8-sig') as f:
    str1=f.read(5)
    print(str1)  # 123中文


print("測試f.seek")
# file.bin 內容
'''Hello Python
中文字測試
Welcome
'''

f=open('file.bin','rb')
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
f=open('fileUTF8.txt','r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()



    
