cost=float(input("請輸入消費總金額:"))    
if cost>=100000:
    cost=cost*0.85 #10萬元以上打85折       
elif cost>=50000:
    cost=cost*0.9  #5萬元到10萬元之間打9折     
else:
    cost=cost*0.95 #5萬元以下打95折
print("實際消費總額:%.1f元" %cost)
