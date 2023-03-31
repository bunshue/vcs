f=open('file1.txt','r',encoding='UTF-8')
for line in f:
    print(line,end="")
f.close()

with open('file1.txt','r',encoding='UTF-8') as f:
    for line in f:
        print(line,end="")


with open('file1.txt','r',encoding='UTF-8') as f:
    str1=f.read(5)
    print(str1)  # Hello


with open('file1.txt','r',encoding='UTF-8') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)



with open('file2.txt','r',encoding ='UTF-8') as f:
    content=f.readlines() 
    print(content)      
    
f=open('file2.txt','r',encoding ='UTF-8')
str1=f.read(5)
print(str1)  # 123中
f.close()


with open('file2.txt','r',encoding ='UTF-8-sig') as f:
    content=f.readlines() 
    print(content)      
    
f=open('file2.txt','r',encoding ='UTF-8-sig')
str1=f.read(5)
print(str1)  # 123中文
f.close()


f=open('file2.txt','r',encoding ='UTF-8-sig')
print(f.readline())  # 123中文字\n
print(f.readline(3)) # abc
f.close()

f=open('file1.txt','r',encoding ='cp950')
for line in f:
    print(line,end="")
f.close()




