strName = str(input("\n郵局："))
strCode = str(input("郵局代號："))
intAount = int(input ("戶頭："))
intMoney = int(input("金額："))
	
print("\n郵局：%s" %(strName))
print("郵局代號為%s，轉帳戶頭為%02d" %(strCode, intAount))
print("匯入金額：%c%.2f" %(36, intMoney))
	
if intMoney < 20000:
    print("%c\n" %("成"))
