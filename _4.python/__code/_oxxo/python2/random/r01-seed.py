import random

# random.seed 
# random.seed 隨機數的「種子」，數值一樣則產生的隨機數相同，若不設定則使用系統提供隨機源
# random.random() 並不是真正的隨機數

random.seed(5)
a = random.random()
random.seed(5)
b = random.random()
c = random.random()   # 重複 print 出來的結果是相同的
d = random.random()
print(f'{a}\n{b}\n{c}\n{d}')

