# Python 新進測試 file

#尋找檔案
import glob
print('尋找目前目錄下之 *.py *.txt')
files = glob.glob("glob.py") + glob.glob("os*.py") + glob.glob("*.txt") 
for file in files:
    print(file)

import os,shutil
cur_path = os.path.dirname(__file__) # 取得目前路徑
print("現在路徑："+cur_path)


#拷貝檔案
destfile = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/' + "ccccc.py"
print("拷貝檔案 " + destfile)
shutil.copy("test10_new12_file2.py",destfile )  # 檔案複製

print("拷貝檔案 " + destfile)
destfile = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/' + "ccccc2.py"
shutil.copyfile('test10_new12_file2.py', destfile)  # 檔案複製


#目錄拷貝
import shutil
source_dir = 'C:/_git/vcs/_4.cmpp/_python_test/data/source_pic'
dest_dir = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/source_pic'
print('cp -r ' + source_dir + ' ' + dest_dir)
#shutil.copytree(source_dir, dest_dir)  # 目錄複製

'''
print("刪除目錄, 直接刪除, 不會放入資源回收筒")
import shutil
shutil.rmtree("C:\\dddddddddd\\aaa" )  # 刪除目錄
'''

filename_rw = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/file.bin'

print("建立一個檔案 binary, 檔名 : " + filename_rw)
content='''Hello Python
中文字測試
Welcome
'''

content=content.encode("utf-8") #轉成 bytes
with open(filename_rw,'wb') as f:
    f.write(content)


print("讀取一個檔案 binary, 檔名 : " + filename_rw)
with open(filename_rw,'rb') as f:
    content=f.read().decode("utf-8") 
    print(content) 


filename1 = 'C:/_git/vcs/_4.cmpp/_python_test/__temp/file1.txt'

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

filename2 = 'C:/_git/vcs/_4.cmpp/_python_test/data/file2.txt'

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
filename_utf8 = 'C:/_git/vcs/_4.cmpp/_python_test/data/fileUTF8.txt'
f=open(filename_utf8,'r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()

print('測試完成')

    
