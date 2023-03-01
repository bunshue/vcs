#python讀和寫文件

filename_w = "TestFileW.txt"
filename_r = "TestFileR.txt"

#寫資料到TestFileW.txt中
#打開一個文件
f = open(filename_w, "w")

#寫資料
num = f.write("python讀和寫文件python讀和寫文件\npython讀和寫文件python讀和寫文件\n")

print("總共寫了 ", num, " 拜")

#關閉文件
f.close()


#從TestFileR.txt把資料讀出來，一次讀完
#打開一個文件
f = open(filename_r, "r")

#一次讀完資料
str = f.read()
print(str)

#關閉文件
f.close()


#從TestFileR.txt把資料讀出來，一次讀一行
#打開一個文件
f = open(filename_r, "r")

#一次讀一行
str = f.readline()
print(str)

#一次讀一行
str = f.readline()
print(str)

#一次讀一行
str = f.readline()
print(str)

#關閉文件
f.close()


#從TestFileR.txt把資料讀出來，一次讀所有行
#打開一個文件
f = open(filename_r, "r")

#一次讀所有行
str = f.readlines()
print(str)

#關閉文件
f.close()

