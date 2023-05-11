f=open('file1.txt','r')
for line in f:
    print(line,end="")
f.close()


with open('file1.txt','r') as f:
    for line in f:
        print(line,end="")


f=open('file1.txt','r')
str1=f.read(5)
print(str1)  # Hello
f.close()

with open('file1.txt','r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)

with open('file2.txt','r',encoding ='UTF-8') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open('file2.txt','r',encoding ='UTF-8')
str1=f.read(5)
print(str1)  # 123中
f.close()







        
