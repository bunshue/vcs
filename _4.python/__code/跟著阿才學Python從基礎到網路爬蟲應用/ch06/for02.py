name = ["PS4 Slim主機 CUH-2117", "任天堂 Nintendo Switch",
        "Xbox One S 500G同捆組"] #name串列存放產品名稱
price = [9980, 12999, 11000]    #price串列存放產品單價
#len()函式取得name串列個數並指定給count
count = len(name)  
#count等於3，因此range(count)會產生[0, 1, 2]串列
#for迴圈中的i會逐一被指定為0, 1, 2
for i in range(count):  
    print("%s \t" %name[i],end="")         #印出產品
    print("單價%d元" %price[i])          #印出單價   

