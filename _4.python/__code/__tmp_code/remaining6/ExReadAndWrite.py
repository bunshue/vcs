file_a = open("book.txt", "a")
file_a.write("Python程式設計")
file_a.writelines(["\n資料結構與演算法", "\n網路行銷與電子商務"])
file_a.close()

file_r = open("book.txt", "r")
print("讀取檔案(read)：", file_r.read())
file_r.seek(0)
print("讀取檔案(readline)：", file_r.readline())
file_r.seek(0)
print("讀取檔案(readlines)：", file_r.readlines())
file_r.close()

print('------------------------------------------------------------')	#60個

file = open("tmp_RelatedFunctions.bin", "w+")
file.write("HIHI!!! I like Program, Do you like this?")

file.flush()

print("寫入之後的游標位置：", file.tell())

file.seek(8, 0)
file.truncate(22)

print(file.read())


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


