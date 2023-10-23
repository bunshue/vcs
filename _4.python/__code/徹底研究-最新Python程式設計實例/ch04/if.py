Money=int(input("請輸入消費的金額:"))
if Money<1200:
    Money*=1.1; #消費未滿 1200，加收服務費1成
print("需繳付的實際金額是 %5.0f 元" %Money)   
