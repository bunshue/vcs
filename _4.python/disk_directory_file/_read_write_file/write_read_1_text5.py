filename1 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file1.txt'


f = open(filename1, 'r')
for line in f:
    print(line,end="")
f.close()


with open(filename1, 'r') as f:
    for line in f:
        print(line,end="")


f=open(filename1, 'r')
str1=f.read(5)
print(str1)  # Hello
f.close()

with open(filename1, 'r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)

filename2 = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/python_file2.txt'
with open(filename2, 'r',encoding = 'UTF-8') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open(filename2, 'r',encoding = 'UTF-8')
str1=f.read(5)
print(str1)  # 123中
f.close()


with open(filename2, 'r',encoding ='UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open(filename2, 'r',encoding ='UTF-8-sig')
str1=f.read(5)
print(str1)  # 123中文
f.close()







        
