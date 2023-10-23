"""
程式名稱：九九乘法表
"""
for x in range(1, 10):
    for y in range(1, 10):
        print("{0}*{1}={2: ^2}".format(y, x, x * y), end=" ")
    print()
