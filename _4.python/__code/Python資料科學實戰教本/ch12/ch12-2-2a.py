import pandas as pd

friends = [110, 1017, 1127, 417, 624, 957, 89, 
           951, 947, 797, 981, 125, 455, 731, 
           1641, 486, 1307, 472, 1131, 1771, 905,
           532, 742, 622]

s_friends = pd.Series(friends)
m = s_friends.mean()
print("平均數: ", m)
s = s_friends.std()
print("標準差: ", s)

z_scores = []
for x in friends:
    z = (x - m)/s   # 公式
    z_scores.append(z)
print(z_scores)
