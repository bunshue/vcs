# ch5_3.py
print("奇數偶數判斷")
num = eval(input("請輸入任意整值: "))
rem = num % 2
if rem:
    print("完成功能 : %d 是奇數" % num )
else:
    print("完成功能 : %d 是偶數" % num )
# PEP 8
if rem:
    print("一般用法 : %d 是奇數" % num )
else:
    print("一般用法 : %d 是偶數" % num )
# 高手用法
print("高手用法 :" ,"%d 是奇數" % num  if rem else "%d 是偶數" % num )


