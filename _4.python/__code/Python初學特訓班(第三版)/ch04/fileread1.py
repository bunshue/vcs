f=open('file1.txt','r')
for line in f:
    print(line,end="")
f.close()