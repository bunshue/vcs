# break練習
total=0
for i in range(1,201,2):
    if i==101:
        break #跳出迴圈
    total+=i
print("1~99的奇數總和:%d" %total)
