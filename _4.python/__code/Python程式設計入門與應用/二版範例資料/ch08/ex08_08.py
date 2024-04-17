# Filename: ex08_08.py
f=open('file_u8.txt','r',encoding='UTF-8-sig')
print(f.readline())
print(f.readline())
print(f.readline(5))
print(f.readline(8))
f.close()