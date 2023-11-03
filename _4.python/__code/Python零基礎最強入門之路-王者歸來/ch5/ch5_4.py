# ch5_4.py
print("奇數偶數判斷")
num = input("請輸入任意整值: ")
rem = int(num) % 2
if (rem == 0):
    print("%d 是偶數" % int(num))
else:
    print("%d 是奇數" % int(num))
