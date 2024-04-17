# Filename: ex08_13.py
try:   
    print("welcome")
except NameError:
    print("變數不存在!")
finally:
    print("程式執行結束例外處理區塊")