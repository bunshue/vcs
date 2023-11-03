import pandas as pd

friends = [110, 1017, 1127, 417, 624, 957, 89, 
           951, 947, 797, 981, 125, 455, 731, 
           1641, 486, 1307, 472, 1131, 1771, 905,
           532, 742, 622]

s_friends = pd.Series(friends)
print(s_friends.describe())
