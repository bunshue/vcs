with open('file2.txt','r',encoding ='UTF-8') as f:
    content=f.readlines() 
    print(content)      
    
f=open('file2.txt','r',encoding ='UTF-8')
str1=f.read(5)
print(str1)  # 123中
f.close()