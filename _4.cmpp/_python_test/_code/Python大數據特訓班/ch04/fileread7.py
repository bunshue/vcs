f=open('file2.txt','r',encoding ='UTF-8-sig')
print(f.readline())  # 123中文字\n
print(f.readline(3)) # abc
f.close()