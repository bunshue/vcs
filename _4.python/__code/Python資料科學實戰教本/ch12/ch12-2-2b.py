import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

friends = [110, 1017, 1127, 417, 624, 957, 89, 
           951, 947, 797, 981, 125, 455, 731, 
           1641, 486, 1307, 472, 1131, 1771, 905,
           532, 742, 622]

s_friends = pd.Series(friends)
m = s_friends.mean()
s = s_friends.std()
z_scores = []
for x in friends:
    z = (x - m)/s   # 公式
    z_scores.append(z)
index = np.arange(len(friends))
plt.bar(index, z_scores)
plt.show()
