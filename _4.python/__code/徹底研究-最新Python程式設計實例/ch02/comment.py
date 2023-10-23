'''
   範例程式:comment.py
   程式功能:本程式示範如何使用多行註解及單行註解
'''
number = 10 #將數值10設定給number
print(number) #輸出number變數值
a=b=c=55 #a, b, c三個變數的值都是55
a,b,c = 55,55,55 #也可以利用","隔開變數名稱,就能在同一列設定值
print(a) #輸出a變數值
print(b) #輸出b變數值
print(c) #輸出c變數值
a,f,name = 66,10.58, "Michael " #也可以混搭不同型態的變數一起宣告
print(a) #輸出a變數值,各位可以發現其值已被重新給定
print(f) #輸出f變數值
print(name) #輸出name變數值
