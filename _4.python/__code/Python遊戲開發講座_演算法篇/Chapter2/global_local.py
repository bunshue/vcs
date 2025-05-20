total = 0
def kasan():
    global total
    loops = 11
    for i in range(loops):
        total += i

print("total的初始值", total)
kasan()
print("執行函數之後的total的值", total)
