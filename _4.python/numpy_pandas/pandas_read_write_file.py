import pandas as pd
import matplotlib.pyplot as plt

print('pandas DataFrame資料輸出到csv檔')

import pandas as pd

scores = {'國文':{'王小明':65,'李小美':90,'陳大同':81,'林小玉':79},
          '英文':{'王小明':92,'李小美':72,'陳大同':85,'林小玉':53},
          '數學':{'王小明':78,'李小美':76,'陳大同':91,'林小玉':47},
          '自然':{'王小明':83,'李小美':93,'陳大同':89,'林小玉':94},
          '社會':{'王小明':70,'李小美':56,'陳大同':94,'林小玉':80}}
df = pd.DataFrame(scores)

print("另存新檔");
filename = 'C:/______test_files3/score_this.csv'
df.to_csv(filename, encoding='utf-8-sig')
print("寫入完成")


print('pandas 讀取 csv檔')

import numpy as np

print("讀取 .csv 檔 1")
filename = 'C:/_git/vcs/_1.data/______test_files1/scores.csv'
na = np.genfromtxt(filename, delimiter=',', skip_header=1)
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

print('pandas 讀取 csv檔')

import pandas as pd
filename = 'C:/_git/vcs/_1.data/______test_files1/scores2.csv'
data = pd.read_csv(filename, header=0, index_col=0)
print('打印資料')
print(data)
#print('打印資料型態')
#print(type(data))



filename = 'C:/______test_files3/score333.csv'

import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_csv(filename, encoding="utf-8-sig")


import pandas as pd
data = pd.read_csv(filename, encoding="utf-8-sig",index_col=0)

print(data)



filename = 'C:/______test_files3/score444.json'

import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_json(filename, force_ascii=False)


import pandas as pd
data = pd.read_json(filename, typ='series')

print(data)


filename = 'C:/______test_files3/score555.xlsx'

import pandas as pd
datas = [[65,92,78,83,70], [90,72,76,93,56], [81,85,91,89,77], [79,53,47,94,80]]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns,  index=indexs)
print(df)

df.to_excel(filename, encoding="utf-8-sig")


import pandas as pd
data = pd.read_excel(filename, encoding="utf-8-sig",index_col=0)

print(data)










