# Python 新進測試 04 讀寫檔案

file_object = open('sample.txt', 'w')
file_object.write('this is sample of python.')
file_object.close()


file_object = open('sample.txt', 'w')
file_object.write('this is sample of python.\n')

file_object.flush()	


file_object = open('sample.txt', 'r')
file_object.read()

file_object = open('sample.txt', 'a') 
file_object.write('Add data from program!!')
file_object.close()

file_object = open('sample.txt', 'r+')
file_object.read()
file_object.write('Add data from program!!')

with open('sample.txt', 'w') as file_object:
	file_object.write('using with!')




