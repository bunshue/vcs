"""
calc_tax函數會接收實際售價與消費稅率這兩個參數
再傳回消費稅額
"""
def calc_tax(price,rate):
    tax = price * rate / 100
    #使用int函數傳回整數
    return int(tax)
    

a = calc_tax(1249,10)
print(a)