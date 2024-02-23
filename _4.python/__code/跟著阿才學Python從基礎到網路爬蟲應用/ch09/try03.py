pid = ["E01", "E02", "E03", "E04"]
name = ["碁峰可樂", "阿才肉乾", "龍哥豆漿", "五香牛肉"]
price = [100, 690, 25, 300]
num = int(input("查詢第幾項產品(1~4)："))
try:
    index = num-1
    print("編號：%s" %pid[index])
    print("品名：%s" %name[index])
    print("單價：%d" %price[index])
except IndexError:
    print("無第 %d 項產品" %num)

