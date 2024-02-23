listScore = []		# 建立listScore為空串列
count = int(input("請輸入學生數："))  # 指定學生數
# 輸入學生成績並逐一放入listScore串列，append()方法可將資料附加到串列中
i = 0
while i<count:
    print("第 %d 位學生：" %(i+1), end='')
    listScore.append(int(input("")))	
    i+=1

print("成績列表：", listScore)	# 顯示listScore所有元素
listScore.sort()				      # 呼叫sort()方法將listScore中的元素進行由小到大非序
print("遞增排序：", listScore)	# 印出listScore由小到大排序的結果
listScore.reverse()			     # 呼叫reverse()方法將listScore中的元素進行反轉
print("遞減排序：", listScore)	# 印出listScore由大到小排序的結果

