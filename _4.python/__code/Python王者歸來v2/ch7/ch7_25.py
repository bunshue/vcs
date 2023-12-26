# ch7_25.py
scores = [94, 82, 60, 91, 88, 79, 61, 93, 99, 77]
scores.sort(reverse = True)         # 從大到小排列
count = 0
for sc in scores:
    count += 1
    print(sc, end=" ")
    if count == 5:                  # 取前5名成績
        break                       # 離開for迴圈



