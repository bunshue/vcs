def payment():
    price = float(input("產品單價："))
    num = float(input("銷售數量："))
    rate = 0.35  #抽取獎金的百分比
    total = price*num * rate
    return price*num, total
 
e1 ,e2 = payment()
print("總銷售業績{},應付獎金：{}".format(e1, e2))
