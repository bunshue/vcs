# Python 新進測試 04 讀寫本地檔案

filename_rw = '__temp\sample.txt'

print("寫入檔案 : " + filename_rw)
file_object = open(filename_rw, 'w')
file_object.write('this is sample of python.')
file_object.close()


print("寫入檔案 : " + filename_rw)
file_object = open(filename_rw, 'w')
file_object.write('this is sample of python.\n')

file_object.flush()	

print("讀取檔案 : " + filename_rw)
file_object = open(filename_rw, 'r')
file_object.read()

print("附加檔案 : " + filename_rw)
file_object = open(filename_rw, 'a') 
file_object.write('Add data from program!!')
file_object.close()

print("讀取檔案 : " + filename_rw)
file_object = open(filename_rw, 'r+')
file_object.read()

print("寫入檔案 : " + filename_rw)
file_object.write('Add data from program!!')

with open(filename_rw, 'w') as file_object:
	file_object.write('using with!')


filename_rw2 = '__temp\sample2.txt'
print("寫入檔案 : " + filename_rw2)
fo = open(filename_rw2, "w")
fo.write("abcdefghijklmnopqrstuvwxyz");
fo.close()

print("開啟檔案 : " + filename_rw2)
fo = open(filename_rw2, "r+")
str = fo.read(10);
print("read 10 string is : ", str)

print("讀取檔案 : " + filename_rw2)
# Check current position
position = fo.tell();
print("current file position : ", position)

print("seek to position 20")
fo.seek(20)

str = fo.read(10);
print("read 10 string is : ", str)

print("go to file head")
fo.seek(0)
str = fo.read(10);
print("read 10 string is : ", str)
fo.close()



