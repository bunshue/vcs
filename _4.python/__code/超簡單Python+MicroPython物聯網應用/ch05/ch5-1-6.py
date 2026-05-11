t = 1
def increment():
    global t  # 全域變數t 
    t += 1
    print("increment()中 : t = ", str(t))
    
print("全域變數初值: t = ", t)
increment()
print("呼叫increment()後 : t = ", t)
    
x = 50
def print_x():
    print("print_x()中 : x = ", x)

print("全域變數初值: x = ", x)
print_x()
print("呼叫print_x()後 : x = ", x)
