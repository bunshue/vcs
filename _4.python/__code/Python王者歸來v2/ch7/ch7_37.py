# ch7_37.py
players = ['Curry', 'Jordan', 'James', 'Durant', 'Obama', 'Kevin', 'Lin']
n = int(input("請輸入人數 = "))
if n > len(players) : n = len(players)  # 列出人數不大於串列元素數
index = 0                               # 索引index
while index < len(players):             # 是否index在串列長度範圍
    if index == n:                      # 是否達到想列出的人數
        break
    print(players[index], end=" ")
    index += 1                          # 索引index加1

