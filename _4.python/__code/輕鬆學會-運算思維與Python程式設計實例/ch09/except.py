try:
    money=int(input("請輸入總業績: "))
    no=int(input("請輸入有多少位業務人員: "))
    average_sales=money/no
except ZeroDivisionError:
    print("人數不可以為0")
except Exception as e1:
    print("錯誤訊息",e1.args)
else:
    print("全體業務同仁平均業績= ", average_sales)
finally:
    print("最後一定要執行的程式區塊")
