file = open("RelatedFunctions", "w+")
file.write("HIHI!!! I like Program, Do you like this?")

file.flush()

print("寫入之後的游標位置：", file.tell())

file.seek(8, 0)
file.truncate(22)

print(file.read())
