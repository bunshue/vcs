# Python 新進測試 04 讀寫本地檔案

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




# Open a file
fo = open("foo.txt", "w")
fo.write("abcdefghijklmnopqrstuvwxyz");

# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10);
print("read 10 string is : ", str)

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
# Close opend file
fo.close()



