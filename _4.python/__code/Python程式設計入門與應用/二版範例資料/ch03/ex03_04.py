# Filename: ex03_04.py
# 巢狀判斷式  輸入3個數字判斷最大值
a = int(input("請輸入第1個數"))
b = int(input("請輸入第2個數"))
c = int(input("請輸入第3個數"))
max=-9999
if(a>=b):
    if(a>=c):
        max=a
    else:
        max=c
elif(b>=c):
    max=b
else:
    max=c
print("最大值為:",max)        