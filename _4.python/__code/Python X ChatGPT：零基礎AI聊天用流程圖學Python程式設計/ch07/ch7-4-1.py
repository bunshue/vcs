# 全域變數
a = 1
b = 2
# 函數: funcA
def funcA():
    c = 3  # 區域變數    
    print("funcA中 : a = ", a)
    print("funcA中 : b = ", b)
    print("funcA中 : c = ", c)
    
# 函數: funcB
def funcB():
    a = 3  # 區域變數
    print("funcB中 : a = ", a)
    print("funcB中 : b = ", b)
    # print("funcB中 : c = ", c)

print("全域變數初值: a = ", a)
print("全域變數初值: b = ", b)
funcA()  # 呼叫funcA
print("呼叫funcA後 : a = ", a)
print("呼叫funcA後 : b = ", b)
funcB()  # 呼叫funcB
print("呼叫funcB後 : a = ", a)
print("呼叫funcB後 : b = ", b)
