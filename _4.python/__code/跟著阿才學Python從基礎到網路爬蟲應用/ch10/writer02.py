import csv
 
listProduct=["","",""] # 建立listProduct串列，用來存放一筆產品記錄
while True:
     option = input("功能選單：1.新增 2.查詢 3.離開：")
     if option=="1":
         # 以附加模式開啟tProduct.csv檔案
         f=open('tProduct.csv','a', newline='') 
         csvWriter=csv.writer(f) 
         listProduct[0] = input("編號：")   #listProduct[0]存放編號
         listProduct[1] = input("品名：")   #listProduct[1]存放品名
         listProduct[2] = input("單價：")   #listProduct[2]存放單價
         csvWriter.writerow(listProduct)
         print("新增成功")
         f.close()
     elif option=="2" :
         # 以讀檔模式開啟tProduct.csv檔案
         f=open ('tProduct.csv')
         data=csv.DictReader(f)  
         print("編號\t品名\t單價")
         for row in data:   		
             print("{}\t{}\t{}".format(row['編號'],row['品名'],row['單價']))
         f.close()
     else:
         break
