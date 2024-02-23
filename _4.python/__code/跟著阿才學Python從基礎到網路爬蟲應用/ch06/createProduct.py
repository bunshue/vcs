product = []
count = int(input("請輸入產品建檔數量："))

i = 0
while i<count:
    print("第 %d 項產品資訊" %(i+1))
    temp = []
    temp.append((input("編號：")))
    temp.append((input("品名：")))
    temp.append((input("單價：")))
    product.append(temp)
    i+=1

print("\n產品資訊如下：")
for row in product:             # 印出每列
    for col in row:             # 印出每欄
        print(col, end='\t')
    print()