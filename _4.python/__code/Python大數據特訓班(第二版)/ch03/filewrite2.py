content='''Hello Python
中文字測試
Welcome'''
with open('file1.txt', 'w' ,encoding='utf-8', newline="") as f:
    f.write(content)