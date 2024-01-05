fp = open("note.txt", "r")
print("檔案內容(有換行):")
for line in fp:
    print(line)
fp.close() 
fp = open("note.txt", "r")   
print("檔案內容(沒換行):")
for line in fp:
    print(line, end="")    
fp.close()
