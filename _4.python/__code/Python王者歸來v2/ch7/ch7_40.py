# ch7_40.py
buyers = [['James', 1030],              # 建立買家購買紀錄
           ['Curry', 893],
           ['Durant', 2050],
           ['Jordan', 990],
           ['David', 2110]]
goldbuyers = []                         # Gold買家串列
vipbuyers =[]                           # VIP買家串列
while buyers:                           # 執行買家分類迴圈分類完成迴圈才會結束
    index_buyer = buyers.pop()
    if index_buyer[1] >= 1000:          # 用1000圓執行買家分類條件
        vipbuyers.append(index_buyer)   # 加入VIP買家串列
    else:
        goldbuyers.append(index_buyer)  # 加入Gold買家串列
print("VIP 買家資料", vipbuyers)
print("Gold買家資料", goldbuyers)
    



