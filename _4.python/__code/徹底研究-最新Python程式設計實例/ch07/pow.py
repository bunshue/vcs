#引數：x 為底數       
#y 為指數       
#傳回值：次方運算結果 
def Pow(x,y):
    p=1
    for i in range(y):
        p *= x
    return p
print("請輸入次方運算（ex.2 3）：")
x,y=input().split()
print('x=',x)
print('y=',y)
print("次方運算結果: %d" %Pow(int(x), int(y)))
