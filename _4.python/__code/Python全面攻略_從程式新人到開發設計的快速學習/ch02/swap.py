a = 100	     	
b = 20			   
print(a, b)  	        # 輸出a和b的變數值,分別為100,20
print(id(a), id(b))     # 顯示a和b變數所在的記憶體位址
a, b = b, a             # a,b兩變數的記憶體位址交換
print(a, b)  	        # 輸出a和b的變數值,分別為20,100
print(id(a), id(b))     # 顯示a和b變數所在的記憶體位址