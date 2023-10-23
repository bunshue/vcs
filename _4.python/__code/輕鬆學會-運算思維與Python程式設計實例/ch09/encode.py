obj=open('test_encode.txt','r', encoding='cp950')  #開啟檔案
for line in obj:
	print(line)
obj.close()
