content='''Hello Python
中文字測試
Welcome'''
f=open('file1.txt', 'w' ,encoding='utf-8', newline="")
f.write(content)
f.close()