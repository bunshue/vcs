import random

# random.choices

a = random.choice([1, 2, 3, 4, 5])  # choice 從 list 中選擇一個隨機元素
print(a)

# choices 從 list 中選擇指定數量的隨機元素 ( 可能會重複 )
b = random.choices([1, 2, 3, 4, 5, 6, 7, 8], k=5)
print(b)

# choices 可透過 weight 定義權重，有相對和累績兩種選一種的設定
# weights 為相對，cum_weights 為累積，下面的例子出現 8 的機率是 1 的八倍
c = random.choices([1, 2, 3, 4, 5, 6, 7, 8], weights=[1, 2, 3, 4, 5, 6, 7, 8], k=5)
print(c)

# shuffle 可以把清單打散為隨機位置
d = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(d)
print(d)

# sample 可以從清單中隨機取出不重複的值
e = random.sample([1, 2, 3, 4, 5, 6, 7, 8], k=4)
print(e)
f = random.sample(range(1,50), k = 6) # 大樂透一行搞定？
print(f)
