# ch5_13.py
ans = 0                         # 讀者心中的數字
print("猜數字遊戲,請心中想一個 0 - 7之間的數字, 然後回答問題")

truefalse = "輸入y或Y代表有, 其它代表無 : "
# 檢測2進位的第1位是否含1
q1 = "有沒有看到心中的數字 : \n" + \
     "1, 3, 5, 7 \n"
num = input(q1 + truefalse)
print(num)
if num == "y" or num == "Y":
    ans += 1
# 檢測2進位的第2位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q2 = "有沒有看到心中的數字 : \n" + \
     "2, 3, 6, 7 \n"
num = input(q2 + truefalse)
if num == "y" or num == "Y":
    ans += 2
# 檢測2進位的第3位是否含1
truefalse = "輸入y或Y代表有, 其它代表無 : "
q3 = "有沒有看到心中的數字 : \n" + \
     "4, 5, 6, 7 \n"
num = input(q3 + truefalse)
if num == "y" or num == "Y":
    ans += 4

print("讀者心中所想的數字是 : ", ans)


    







