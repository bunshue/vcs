persons = ["林小明","曾山水","鄭美麗","林小明","曾山水","林小明"]
s = set(persons) # 串列轉集合
print(s)         # {'林小明', '曾山水', '鄭美麗'}
list1 = list(s)  # 集合轉串列
print(list1)     # ['林小明', '曾山水', '鄭美麗']
print(list1[0])  # 林小明