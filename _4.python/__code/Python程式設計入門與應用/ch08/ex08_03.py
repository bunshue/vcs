# Filename: ex08_03.py
f=open('file.txt','r',encoding='UTF-8')
for line in f:
    print(line, end="")
f.close() 