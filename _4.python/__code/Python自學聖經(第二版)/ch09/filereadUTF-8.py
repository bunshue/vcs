f=open('file2.txt','r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()