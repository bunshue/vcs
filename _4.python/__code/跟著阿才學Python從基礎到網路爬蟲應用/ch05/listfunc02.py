listScore = []
listScore.append(int(input("第 1 位學生成績：")))
listScore.append(int(input("第 2 位學生成績：")))
listScore.append(int(input("第 3 位學生成績：")))
listScore.append(int(input("第 4 位學生成績：")))

print("成績列表：", listScore)
listScore.sort()
print("遞增排序：", listScore)
listScore.reverse()
print("遞減排序：", listScore)


