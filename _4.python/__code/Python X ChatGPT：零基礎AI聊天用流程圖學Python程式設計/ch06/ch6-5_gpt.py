# 使用外層for迴圈從1到9
for i in range(1, 10):
    # 使用內層while迴圈從1到9
    j = 1
    while j <= 9:
        # 顯示乘法運算式
        print(i, "*", j, "=", (i*j), end="\t")
        j += 1
    # 換行
    print()
