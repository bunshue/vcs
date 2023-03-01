#各種寫入檔案範例

print("附加模式寫檔案")
filename_w = "TestFileW1.txt"
f = open(filename_w, "a")

data = "123456789\n"
f.write(data)
f.close()


print("寫入檔案範例")
filename_w = "TestFileW2.txt"

#寫資料到檔案中
#打開一個文件
f = open(filename_w, "w")

#寫資料
num = f.write("python讀和寫文件python讀和寫文件\npython讀和寫文件python讀和寫文件\n")

print("總共寫了 ", num, " 拜")

#關閉文件
f.close()

print("讀取一檔並將資料寫到另檔的範例")

#python讀和寫文件

filename_r = "poetry.txt"
filename_w = "poetry_another.txt"

with open(filename_r, 'rt', encoding = 'utf8') as f:
    data = f.read()
    
print("data :\n", data)

#關閉文件
f.close()

with open(filename_w, 'wt') as f:
    f.write(data)
    
#關閉文件
f.close()


