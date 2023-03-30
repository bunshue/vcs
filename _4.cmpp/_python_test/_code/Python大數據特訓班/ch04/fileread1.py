f=open('file1.txt','r',encoding='UTF-8')
for line in f:
    print(line,end="")
f.close()