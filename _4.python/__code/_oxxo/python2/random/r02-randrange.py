import random

# random.randrange 和 random.randint 都可產生隨機整數

a = random.randrange(2, 500, 2) # randrange 可指定隨機數階層，一定偶數
print(a)
b = random.randrange(0, 1)   # randrange 不包含設定的最後一個數值，一定出現 0
print(b)
c = random.randint(0, 1)   # randint 包含設定的最後一個數值，0 和 1 隨機挑選
print(c)