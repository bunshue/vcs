import os
#   讀檔作業
def fnRead():
    if (os.path.exists(filename)):
        f = open(filename, "r")
        listProduct = f.readlines();
        print("編號\t品名\t單價\t9折折扣")
        for row in listProduct:
            data = row.strip()
            listcol = data.split(",")
            colNum=1
            for col in listcol:
                print(col, end="\t")
                colNum+=1
                if(colNum==4):
                    print("$%.2f" %(float(col)*0.9), end="\t")
            print()
        print("產品讀取成功")
        f.close()
    else:
        print("%s 檔案不存在，請先使用新增功能建檔" %(filename))
        
 # 新增作業       
def fnWrite():
    f = open(filename, "a")   # 以附加資料模式開啟檔案
    pid = input("編號：")      # 輸入編號並指定給pid
    name = input("品名：")      # 輸入品名並指定給name
    price = int(input("單價："))  # 輸入單價並指定給price
    data = pid+","+name+","+str(price)+"\n"
    f.write(data)
    f.close()
    print("產品新增成功")
# 主程式
filename = "product.txt"
print("==DTC產品管理系統==")
while True:
    try:
        n = int(input("請選擇功能：1.新增 2.讀取 3.離開->"))
        if n==1:
            fnWrite()
        elif n==2:
            fnRead()
        elif n==3:
            print("離開系統")
            break
        else:
            print("無此選項")
    except Exception:
        print("錯誤，功能選項為1~3數字")


