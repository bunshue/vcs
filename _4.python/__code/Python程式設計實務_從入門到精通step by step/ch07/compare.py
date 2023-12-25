def mymax(x,y):
    if x>y:
        return x
    else:
        return y

print('數字比大小')
a=int(input('請輸入a:'))
b=int(input('請輸入b:'))
print("較大者之值為:%d" %mymax(a,b))#函數呼叫
