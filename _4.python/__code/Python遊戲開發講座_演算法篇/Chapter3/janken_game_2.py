import random
hand = ["石頭", "剪刀", "布"]
print("跟電腦猜拳。")

for i in range(3):
    print("\n", i+1, "回合的猜拳")
    y = input("你要出什麼？\n0=石頭 1=剪刀 2=布 ")
    y = int(y)
    c = random.randint(0, 2)
    print("電腦出的是"+hand[c])
    if y==c:
        print("平手")
    if y == 0:
        if c == 1:
            print("你贏了")
        if c == 2:
            print("電腦贏了")
    if y == 1:
        if c == 0:
            print("電腦贏了")
        if c == 2:
            print("你贏了")
    if y == 2:
        if c == 0:
            print("你贏了")
        if c == 1:
            print("電腦贏了")
