import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

dists = {"區名": ["中正區", "板橋區", "桃園區", "北屯區", 
                  "安南區", "三民區", "大安區", "永和區", 
                  "八德區", "前鎮區", "鳳山區", 
                  "信義區", "新店區"],
         "人口": [159598, 551452, 441287, 275207,
                  192327, 343203, 309835, 222531,
                  198473, 189623, 359125, 
                  225561, 302070],
         "面積": [7.6071, 23.1373, 34.8046, 62.7034, 
                  107.2016, 19.7866, 11.3614, 5.7138, 
                  33.7111, 19.1207, 26.7590, 
                  11.2077, 120.2255]}

df = pd.DataFrame(dists, 
                  columns=["人口", "面積"],
                  index=dists["區名"])
print(df)
fig, ax = plt.subplots()
fig.suptitle("分區統計")
ax.set_ylabel("人口")
ax.set_xlabel("分區")
ax2 = ax.twinx()
ax2.set_ylabel("面積")
df["人口"].plot( ax=ax, 
                 style="b--o",
                 use_index=True,
                 rot=90)
df["面積"].plot( ax=ax2, 
                 style="g-s",
                 use_index=True,
                 rot=90)
plt.show()