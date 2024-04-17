# Filename: ex04_03.py
# 讀取串列資料
list1 = []
sum = 0
for i in range(1,7):
    score=int(input("請輸入第%d位學生成績:"%i))
    list1.append(score)
    sum += score
print("分數總分為:",sum)
print(list1)