# 定義Sort()函式，此函式可將傳入的三個數值進行由小到大排序， 並將排序後的結果傳回
def Sort(x, y, z) :
    # 判斷三個數的大小，並做調整
    if (x > y):
        t=x
        x=y
        y=t
    if (y > z):
        t=y
        y=z
        z=t
    if (x > z):
        t=x
        x=z
        z=t
    return x, y, z

# 將輸入的數值1~數值3依序放到a, b, c三個變數
a = int(input("數值1："))
b = int(input("數值2："))
c = int(input("數值3："))
# 呼叫Sort()函式傳入a, b, c三個數，最後將由小到大排序的結果依序指定給a, b, c
a, b, c = Sort(a, b, c) 
print("\n由小到大排序：%d %d %d" %(a, b, c))




