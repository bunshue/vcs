def CallReference(x):
    for i in range(len(x)):
        x[i] += 10
    print("函式呼叫中：x位址={}, x={}".format(id(x), x))

a=[1, 2, 3, 4]    
print("函式呼叫前：a位址={}, a={}".format(id(a), a))
CallReference(a)
print("函式呼叫後：a位址={}, a={}".format(id(a), a))
