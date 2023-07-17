with open('file1.txt', 'r', encoding='utf-8') as f:
    content=f.readlines()
    print(type(content))
    print(content)