import random as r

print( r.random() ) #產生隨機浮點數n,0 <= n < 1.0
print( r.uniform(101, 200) ) #產生101-200之間的隨機浮點數
print( r.randint(-50, 0) ) #產生-50-0之間的隨機整數
print( r.randrange(0, 88, 11) ) #從序列中取一個隨機數
print( r.choice(["健康", "運勢", "事業", "感情", "流年"]) ) #

items = ['a','b','c','d']
r.shuffle(items) #將items序列打亂
print( items )
#從序列或集合擷取12個不重複的元素
print( r.sample('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', 12))
