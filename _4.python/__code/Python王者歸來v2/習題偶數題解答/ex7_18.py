# ex7_18.py
sc = [[1, '洪錦魁', 80, 95, 88, 0, 0, 0],
      [2, '洪冰儒', 98, 97, 96, 0, 0, 0],
      [3, '洪雨星', 91, 93, 95, 0, 0, 0],
      [4, '洪冰雨', 92, 94, 90, 0, 0, 0],
      [5, '洪星宇', 92, 97, 90, 0, 0, 0],
     ]
# 計算總分與平均
print("原始成績單")
for i in range(len(sc)):
    print(sc[i])
    sc[i][5] = sum(sc[i][2:5])              # 填入總分
    sc[i][6] = round((sc[i][5] / 3), 1)     # 填入平均
sc.sort(key=lambda x:x[5],reverse=True)     # 依據總分高往低排序
# 以下填入名次
for i in range(len(sc)):                    # 填入名次
    sc[i][7] = i + 1
# 以下修正相同成績應該有相同名次
for i in range((len(sc)-1)):
    if sc[i][5] == sc[i+1][5]:              # 如果成績相同
        sc[i+1][7] = sc[i][7]               # 名次應該相同
# 以下依座號排序
sc.sort(key=lambda x:x[0])                  # 依據座號排序
print("最後成績單")
for i in range(len(sc)):
    print(sc[i])

















