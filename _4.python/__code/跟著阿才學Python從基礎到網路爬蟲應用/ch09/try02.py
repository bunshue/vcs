try:
    a = 10 
    b = 0
    c = a / b
except NameError as e:
    print("錯誤訊息：",e)
except ZeroDivisionError as e:
    print("錯誤訊息：",e)
finally:
    print("程式執行完成")