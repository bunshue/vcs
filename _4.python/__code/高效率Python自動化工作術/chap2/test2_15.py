def calc(max):
    a = 1
    while a < max:
        a = a * 2
    return a

ans = calc(1000)
print("  超過1000之後的第一個值為",ans)
ans = calc(10000)
print(" 超過10000之後的第一個值為",ans)
ans = calc(100000)
print("超過100000之後的第一個值為",ans)
