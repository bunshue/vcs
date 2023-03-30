with open('file1.txt','r',encoding='UTF-8') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  