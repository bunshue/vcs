import numpy as np

print("讀取 .csv 檔 1")
na = np.genfromtxt('data\scores.csv', delimiter=',', skip_header=1)
print("資料寬高")
print(na.shape)

print('國文最高分數：', na[:,1].max())
print('英文最低分數：', na[:,2].min())
print('數學平均分數：', na[:,3].mean())
total1 = na[:,1] + na[:,2] + na[:,3]
print(total1)
print('全班最高總分：',total1.max())

total2 = na[:,1:4].sum(axis=1)
print(total2)
print('全班最高總分：',total2.max())


print("讀取 .csv 檔 2")
import pandas as pd

data = pd.read_csv("data\scores2.csv", header=0, index_col=0)
print('打印資料')
print(data)
#print('打印資料型態')
#print(type(data))


