# Filename: ex08_07.py
f=open('file_u8.txt','r',encoding='UTF-8')
str=f.readlines()
print(str)
f.close()

f=open('file_u8.txt','r',encoding='UTF-8')
str1=f.read(7)
print(str1)
f.close()