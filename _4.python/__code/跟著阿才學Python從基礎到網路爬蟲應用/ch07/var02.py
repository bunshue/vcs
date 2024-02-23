def func():
    global n 
    n = 10
    print("函式內 全域變數n 位址=%d, 值=%d" %(id(n), n))
            
n = 100
print("函式外 全域變數n 位址=%d, 值=%d" %(id(n), n))
func()
print("函式外 全域變數n 位址=%d, 值=%d" %(id(n), n))



