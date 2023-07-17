f=open('file1.txt','rt')
for line in f:
    print(line,end="")
f.close()