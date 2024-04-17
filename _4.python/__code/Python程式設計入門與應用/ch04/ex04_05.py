# Filename: ex04_040.py
list1 = []
for i in range(1,7):
    score=int(input("請輸入第%d位學生成績:"%i))
    list1.append(score)
list2 = sorted(list1)
list3 = sorted(list1, reverse=True)
print("原始成績:",list1)
print("由小到大:",list2)
print("由大到小:",list3)