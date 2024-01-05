def Pow(x, y):
    p = 1;
    for i in range(y+1):
        p *= x
    return p
print('請輸入兩數x及y的值函數：')
x=int(input('x='))
y=int(input('y='))
print('次方運算結果：%d' %Pow(x, y))
