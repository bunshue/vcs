x = 50
def print_x():
    x = 100
    print("print_x()中 : x = ", x)

print("全域變數初值: x = ", x)
print_x()
print("呼叫print_x()後 : x = ", x)
