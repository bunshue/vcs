# ex7_14.py
title = "9 * 9 Multiplication Table"
print("%s" % title.center(40))
for i in range(1,10):
    print(f"{i:4d}", end='')
print()                                 # 跳列輸出
for i in range(40):
    print("=", end='')                  # 列印分隔符號
print()                                 # 跳列輸出
for i in range(1, 10):
    print(i, '|', end='')
    for j in range(1, 10):
        print(f"{i*j:4d}", end='')      # 列印乘法值
    print()                             # 跳列輸出




    
   




