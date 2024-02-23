import os
filename = "product.txt"
if (os.path.exists(filename)):
    f = open(filename, "r")
    while True:
        row = f.readline()
        if row!="" and row!="\n":
            data = row.strip()
            listcol = data.split(",")
            colNum = 1
            for col in listcol:
                print(col, end="\t")
                colNum+=1
                if(colNum==4):
                    print("$%.2f" %(float(col)*0.9), end="\t")
            print()
        else:
            print("檔案讀取完成")
            f.close()
            break
else:
    print("%s 檔案不存在" %(filename))