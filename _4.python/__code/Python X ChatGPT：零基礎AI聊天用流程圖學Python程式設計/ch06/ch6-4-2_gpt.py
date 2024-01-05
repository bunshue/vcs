# 顯示1到6之中的偶數，而不顯示奇數

# 使用for迴圈從1到6進行迭代
for i in range(1, 7):
    # 如果i是奇數，就跳過這一次迴圈
    if i % 2 == 1:
        continue
    # 如果i是偶數，就顯示它
    print(i)
