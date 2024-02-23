import os
filename = "product.txt"
print("請輸入產品記錄：")
f = open(filename, "a")   # 以附加資料模式開啟檔案
pid = input("編號：")      # 輸入編號並指定給pid
name = input("品名：")      # 輸入品名並指定給name
price = int(input("單價："))  # 輸入單價並指定給price
data = pid+","+name+","+str(price)+"\n"
f.write(data)
print("產品記錄新增成功")
f.close()


