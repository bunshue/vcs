with open('file2.txt','r',encoding ='UTF-8-sig') as f:
    doc=f.readlines() 
    print(doc)      
    
f=open('file2.txt','r',encoding ='UTF-8-sig')
str1=f.read(5)
print(str1)  # 123中文
f.close()