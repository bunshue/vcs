'''
    函數功能：計算獎金的百分比
    price:產品單價
    num:銷售數量
    price*num:銷售業績總額
    total:實得獎金
'''
def payment():
    price = float(input("產品單價："))
    num = float(input("銷售數量："))
    rate = 0.35  #抽取獎金的百分比
    total = price * num * rate
    return price*num, total
