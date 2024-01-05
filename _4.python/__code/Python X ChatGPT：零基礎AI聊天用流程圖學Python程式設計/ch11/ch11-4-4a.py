fp = open("note.txt", "r")
list1 = fp.readlines()
print("檔案內容:")
print(list1)
for line in list1:
    print(line, end="")    
fp.close()
