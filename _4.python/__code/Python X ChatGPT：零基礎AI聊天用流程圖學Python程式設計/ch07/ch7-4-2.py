# 全域變數
t = 1
# 函數: 計數函數
def increment():
    # global t = 1
    global t  # 全域變數t 
    t += 1
    print("在increment中 : t = ", t)
    
# 函數: 在函數建立全域變數
def global_var():
    # global x = 100
    global x
    x = 100
    print("在global_var中 : x = ", x)

print("全域變數初值: t = ", t)
increment()  # 呼叫increment
print("呼叫increment後 : t = ", t)
global_var()  # 呼叫global_var
print("呼叫global_var後 : x = ", x)
