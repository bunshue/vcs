import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


#df = pd.DataFrame(np.random.randn(3,3), columns=list("甲乙丙"))
#print(df)

df = pd.DataFrame(np.random.randn(5, 3), index=list(range(1,6)), columns=list("ABC"))
print(df)

print('常用統計數據')
print(df.describe())

print('相關係數')
print(df.corr())

print('data_frame 存檔')
df.to_csv("df_data.csv")


print('data_frame 畫點圖')

x = df.A.values
y = df.B.values

plt.scatter(x,y)

print('存圖')
plt.savefig('df_data.png')

plt.show()


'''
loc 的用法
df.loc[列的範圍, 行的範圍]

df.loc[2:3, "B":"C"]


列或行只要一個
df.loc[2, "B"]

df.loc[2, "B"]=-1

'''

plt.show()

print('------------------------------------------------------------')	#60個



