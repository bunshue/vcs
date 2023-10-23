file1=open("phrase.txt","r")
text=file1.read(1) #以read()方法讀取檔案
print(text)
text=file1.read(3) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
text=file1.read(2) #以read()方法讀取檔案
print(text)
file1.close()
