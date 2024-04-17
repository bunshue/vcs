# Filename: ex03_09.py
# while迴圈計算n!
result = i = 1
pn = int(input("請輸入要計算階層的正整數:"))
while(i <= pn):
    result = result*i
    i = i+1
print("%d!=%d"%(pn,result))