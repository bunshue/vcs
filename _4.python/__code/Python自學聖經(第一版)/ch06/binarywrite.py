content='''Hello Python
中文字測試
Welcome
'''

content=content.encode("utf-8") #轉成 bytes
with open('file.bin','wb') as f:
    f.write(content)