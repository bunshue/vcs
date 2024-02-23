#name串列存放產品名稱
name = ["PS4 Slim主機 CUH-2117",
       "任天堂 Nintendo Switch", "Xbox One S 500G同捆組"]
#price串列存放產品單價
price = [9980, 12999, 11000]
#len()函式取得name串列個數並指定給count
count = len(name)   
#count等於3，range(count)會產生0, 1, 2串列，for迴圈中的i會逐一被指定為0, 1, 2
i=0 # i起始為0
while (i<count) :
   print("%s \t" %name[i],end="")         # 印出產品
   print("單價%d元" %price[i])          # 印出單價
   i+=1       
