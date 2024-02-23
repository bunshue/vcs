product = [["E01", "碁峰可樂", 100], ["E02", "阿才肉乾", 690], 
           ["E03", "龍哥豆漿", 25], ["E04", "五香牛肉", 300]]
num = int(input("查詢第幾項產品(1~4)："))
if (num>=1 and num<=4):
    index = num-1
    print("編號：%s" %product[index][0])
    print("品名：%s" %product[index][1])
    print("單價：%d" %product[index][2])
else:
    print("無第 %d 項產品" %num)
