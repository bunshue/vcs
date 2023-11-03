# ch5_2.py
print("輸出絕對值")
num = input("請輸入任意整數值: ")
x = int(num)
if (int(x) < 0):
    x = abs(x)
print("絕對值是 %d" % int(x))
