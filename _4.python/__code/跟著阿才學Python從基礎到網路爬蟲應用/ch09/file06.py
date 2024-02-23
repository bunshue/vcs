import os
filename = "product.txt"
if (os.path.exists(filename)):
    f = open(filename, "r")
    while True:
        row = f.readline()
        if row!="" and row!="\n":
            print(row.strip())
        else:
            print("檔案讀取完成")
            f.close()
            break
else:
    print("%s 檔案不存在" %(filename))