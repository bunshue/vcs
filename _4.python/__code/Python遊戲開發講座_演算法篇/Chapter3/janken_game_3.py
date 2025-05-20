import random
hand = ["石頭", "剪刀", "布"]
you_win = 0
com_win = 0
print("跟電腦猜拳。")
print("猜三次拳，分出勝負。")

for i in range(3):
    print("\n", i+1, "回合的猜拳")
    y = ""
    while True:
        y = input("你要出什麼？\n0=石頭 1=剪刀 2=布 ")
        if y=="0" or y=="1" or y=="2":
            break
    y = int(y)
    c = random.randint(0, 2)
    print("電腦出的是"+hand[c])
    if y==c:
        print("平手")
    if y == 0:
        if c == 1:
            print("你贏了")
            you_win = you_win+1
        if c == 2:
            print("電腦贏了")
            com_win = com_win+1
    if y == 1:
        if c == 0:
            print("電腦贏了")
            com_win = com_win+1
        if c == 2:
            print("你贏了")
            you_win = you_win+1
    if y == 2:
        if c == 0:
            print("你贏了")
            you_win = you_win+1
        if c == 1:
            print("電腦贏了")
            com_win = com_win+1

print("--------------------")
print("你獲勝的次數", you_win)
print("電腦獲勝的次數", com_win)
if you_win>com_win:
    print("你獲勝了！")
elif com_win>you_win:
    print("電腦獲勝了！")
else:
    print("平手")
