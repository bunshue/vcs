import sys
import pandas as pd
import matplotlib.pyplot as plt

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個
#      "國文","數學","英文","自然","社會"
datas = [[65,92,78,83,70],  #學生A
         [90,72,76,93,56],  #學生B
         [81,85,91,89,77],  #學生C
         [79,53,47,94,80]]  #學生D

columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, index=list(range(1,5)), columns=columns)
df.plot(xticks=range(1,5))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV5_Kobe_stats.csv'
df = pd.read_csv(filename)
data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]
data["AST"] = df["AST"]
data["REB"] = df["TRB"]
data = data.set_index("Season")
data.plot(kind = 'line')

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV5_HOU_players_stats.csv'
df = pd.read_csv(filename)
df_grouped = df.groupby("Pos")
points = df_grouped["PTS/G"].mean()
data = pd.DataFrame()
data["Points"] = points
points.plot(kind = 'bar')

plt.show()

print('------------------------------------------------------------')	#60個

