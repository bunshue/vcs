with open('file1.txt','r') as f:
    content=f.readlines() 
    print(type(content))   # <class 'list'>
    print(content)  