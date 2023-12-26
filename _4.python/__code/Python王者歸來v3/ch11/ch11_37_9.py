# ch11_37_9.py
sc = {'John':80, 'Tom':90, 'Kevin':77}
newsc1 = sorted(sc.items(), key = lambda x:x[0])  # 依照key排序
print("依照人名排序")
print(newsc1)

newsc2 = sorted(sc.items(), key = lambda x:x[1])  # 依照value排序
print("依照分數排序")
print(newsc2)



