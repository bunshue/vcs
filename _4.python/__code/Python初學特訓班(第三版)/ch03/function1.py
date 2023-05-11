innum = 0
list1 = []
while(innum != -1):
    innum = int(input("請輸入正整數 (-1：結束)："))
    list1.append(innum)
list1.pop()
print("共輸入 %d 個數" % len(list1))
print("最大數為：%d" % max(list1))
print("最小數為：%d" % min(list1))
print("輸入數的總和為：%d" % sum(list1))
print("輸入數由大到小排序為：{}".format(sorted(list1, reverse=True)))