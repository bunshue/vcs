def func():
    n = 10
    print("區域變數n 位址=%d, 值=%d" %(id(n), n))
            
n = 100
func()
print("全域變數n 位址=%d, 值=%d" %(id(n), n))


