import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

print('------------------------------------------------------------')	#60個

df = pd.read_csv("grades.csv")

print(df.head())

print(df["國文"])


print(df.國文)


cg = df.國文.values


print(cg)


print(cg.mean())

print(cg.std())


df.國文.plot()
plt.show()


df.國文.hist(bins = 15)
plt.show()



print('------------------------------------------------------------')	#60個



import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("grades.csv")

print(df.head())

#print(df["國文"])

print(df.國文.mean())
print(df.國文.std())
print(df.describe())    #顯示統計資料
print('係數矩陣 :', df.corr())

#只算兩科間的相關係數當然也可以。
print(df.國文.corr(df.數學))

df["總級分"] = df[["國文", "英文", "數學", "社會", "自然"]].sum(1)
print(df.head())

df["主科"] = df.數學*1.5 + df.英文

print(df.head())

print(df.sort_values(by = "總級分", ascending = False).head(20))

print(df.sort_values(by = ["主科", "總級分"], ascending = False).head(20))

print('------------------------------------------------------------')	#60個

print('用 Groupby 看美國哪裡最容易看到 UFO')
df = pd.read_csv("http://bit.ly/uforeports")

print(df.head())


df_state = df.groupby("State").count()

print(df_state)

df_state.sort_values(by = "Time", ascending = False)


print(df_state)


df_state.sort_values(by = "Time", ascending = False, inplace = True)

print(df_state.head(10))

df_state[:10].Time.plot(kind = 'bar')

plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

