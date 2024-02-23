def CallValue(x):
    x+=10
    print("函式呼叫中：x位址=%d, x=%d" %(id(x), x))
    
a=6
print("函式呼叫前：a位址=%d, a=%d" %(id(a), a))
CallValue(a)
print("函式呼叫後：a位址=%d, a=%d" %(id(a), a))