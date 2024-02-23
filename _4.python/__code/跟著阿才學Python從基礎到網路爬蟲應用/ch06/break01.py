#pid串列存放產品編號
pid = ["A01", "A02", "A03"]
#name串列存放產品名稱
name = ["PS4 特價包","Switch", "Xbox One"]
#price串列存放產品單價
price = [9980, 12999, 11000]

inputId = input("請輸入欲查詢的產品編號：")

index=-1  # index串列索引為-1表示找不到
count = len(pid)    #len()函式取得name串列個數並指定給count
#count等於3，因此range(count)會產生[0, 1, 2]串列
#for迴圈中的i會逐一被指定為0, 1, 2
for i in range(count):  
    if(inputId==pid[i]):   
        index=i    #若有找到資料將i指定給index
        break      #離開迴圈
#若index等於-1表示找不到資料
if index==-1:
    print("找不到資料")
else:
    print("編號\t品名\t單價")
    print("%s\t%s\t%d" %(pid[index], name[index], price[index]))
    
