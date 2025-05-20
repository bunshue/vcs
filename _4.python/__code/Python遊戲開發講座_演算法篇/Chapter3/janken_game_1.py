import random
hand = ["石頭", "剪刀", "布"]

for i in range(3):
    print("\n", i+1, "回合")
    c = random.randint(0, 2)
    print("電腦出的是"+hand[c])
