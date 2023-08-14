m = int(input("請輸入最大值: "))
s = 0
for i in range(m, 0, -1):
    print("i = ", i)
    s += i
print("總和 = " + str(s))
