import os
filename = "product.txt"
if (os.path.exists(filename)):
    f = open(filename, "r")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print(f.readline(), end="")
    print("檔案讀取完成")
    f.close()
else:
    print("%s 檔案不存在" %(filename))


