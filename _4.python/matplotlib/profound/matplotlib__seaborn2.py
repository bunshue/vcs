"""

seaborn


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import seaborn as sns

print("------------------------------------------------------------")  # 60個

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

sns.set()
fig, axes = plt.subplots(1,2, figsize=(6,4))
ax1 = sns.lineplot(x=x, y=sinus, ax=axes[0])
ax2 = sns.scatterplot(x=x, y=cosinus, ax=axes[1])

plt.show()

print("------------------------------------------------------------")  # 60個
 
x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

df = pd.DataFrame()
df["x"] = x
df["sin"]= sinus
df["cos"] = cosinus
print(df.head())
df.head().to_html("tmp_ch10-3-1a-01.html")
df2 = pd.melt(df, id_vars=['x'], value_vars=['sin', 'cos'])
print(df2.head())
df2.head().to_html("tmp_ch10-3-1a-02.html")

sns.set()
sns.relplot(x="x", y="value", kind="scatter", col="variable", data=df2)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]

sns.set_style("whitegrid")
sns.lineplot(x=x, y=sinus)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]

sns.set_style("whitegrid")
sns.lineplot(x=x, y=sinus)
sns.despine()

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]

sns.set_style("darkgrid", {"axes.axisbelow": False})
sns.lineplot(x=x, y=sinus)

plt.show()

print(sns.axes_style())

print("------------------------------------------------------------")  # 60個

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]

plt.rcParams["axes.unicode_minus"] = False
sns.set_style("darkgrid", {"axes.axisbelow": False,
                           "font.sans-serif":['Microsoft JhengHei']})
sns.lineplot(x=x, y=sinus)
plt.title("Sinus三角函數的波型")
plt.xlim(-2, 12)
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.show()

print("------------------------------------------------------------")  # 60個

x = [0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,
     5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]
sinus = [math.sin(v) for v in x]
cosinus = [math.cos(v) for v in x]

df = pd.DataFrame()
df["x"] = x
df["sin"]= sinus
df["cos"] = cosinus
print(df.head())
df.head().to_html("tmp_ch10-3-2d-01.html")
df2 = pd.melt(df, id_vars=['x'], value_vars=['sin', 'cos'])
print(df2.head())
df2.head().to_html("tmp_ch10-3-2d-02.html")

sns.set()
sns.relplot(x="x", y="value", kind="scatter", col="variable",
            height=4, aspect=1.2, data=df2)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據
print(df.head())
df.head().to_html("tmp_ch10-3-3.html")

print("------------------------------------------------------------")  # 60個

print(sns.get_dataset_names())

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.relplot(x="total_bill", y="tip", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.relplot(x="total_bill", y="tip", hue="smoker", data=df)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.relplot(x="total_bill", y="tip", hue="smoker",
            style="smoker", data=df)
plt.show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_data/Kobe_stats.csv")
data = pd.DataFrame()
data["Season"] = pd.to_datetime(df["Season"])
data["PTS"] = df["PTS"]

sns.set()
sns.relplot(x="Season", y="PTS", data=data, kind="line")
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("fmri")  # 示例中的基本數據

sns.set()
sns.relplot(x="timepoint", y="signal", data=df, kind="line")

sns.relplot(x="timepoint", y="signal", ci=None, data=df, kind="line")
sns.relplot(x="timepoint", y="signal", ci="sd", data=df, kind="line")

sns.relplot(x="timepoint", y="signal", 
            estimator=None, data=df, kind="line")

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.histplot(df["total_bill"], kde=False)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.histplot(df["total_bill"], kde=False)
sns.histplot(df["total_bill"], kde=False, bins=20, color="red")
sns.histplot(df["total_bill"], kde=False, bins=30, color="green")

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.kdeplot(df["total_bill"], label="default")
sns.kdeplot(df["total_bill"], bw_adjust=2, label="bw_adjust: 2")
sns.kdeplot(df["total_bill"], bw_adjust=5, label="bw_adjust: 5")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.histplot(df["total_bill"], kde=True)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.displot(df["total_bill"], kde=True, rug=True)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

print(df.head())
df.head().to_html("tmp_ch10-5-2.html")

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.jointplot(x="petal_length", y="petal_width", data=df)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.jointplot(x="petal_length", y="petal_width", kind="hex", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.jointplot(x="petal_length", y="petal_width", kind="kde", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.pairplot(df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.pairplot(df, kind="scatter", diag_kind="kde",
             hue="species", palette="husl")
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.stripplot(x="species", y="sepal_length", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.stripplot(x="species", y="sepal_length", jitter=False, data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.swarmplot(x="species", y="sepal_length", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.boxplot(x="species", y="petal_length", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.violinplot(x="day", y="total_bill", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.violinplot(x="day", y="total_bill", hue="sex", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.violinplot(x="day", y="total_bill", hue="sex", 
               split=True, data=df)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.barplot(x="sex", y="total_bill", hue="day", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.countplot(x="sex", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.pointplot(x="sex", y="total_bill", hue="day", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.catplot(x="day", y="total_bill", data=df,
               kind="bar", hue="sex")
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.catplot(x="day", y="total_bill", data=df,
               kind="bar", col="sex")
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.catplot(x="sex", y="total_bill", data=df,
               kind="bar", col="day", col_wrap=2)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.boxplot(x="petal_length", y="species", data=df)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("iris")  # 示例中的基本數據

sns.set()
sns.boxplot(data=df, orient="h")

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.regplot(x="total_bill", y="tip", data=df)
sns.lmplot(x="total_bill", y="tip", data=df)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("tips")  # 示例中的基本數據

sns.set()
sns.regplot(x=df["total_bill"], y=df["tip"])

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("anscombe")  # 示例中的基本數據

sns.set()
sns.lmplot(x="x", y="y", col="dataset", hue="dataset", data=df,
           col_wrap=2, ci=None, height=4)
plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("anscombe")  # 示例中的基本數據

sns.set()
sns.lmplot(x="x", y="y", data=df.query("dataset=='II'"), order=2)

plt.show()

print("------------------------------------------------------------")  # 60個

df = sns.load_dataset("anscombe")  # 示例中的基本數據

sns.set()
sns.residplot(x="x", y="y", data=df.query("dataset=='III'"))
plt.show()

print("------------------------------------------------------------")  # 60個

import seaborn as sns

tips=sns.load_dataset("tips")  # 示例中的基本數據

# violinplot小提琴圖
sns.violinplot(x="day", y="total_bill", hue="sex", split=True, data=tips)

plt.show()



print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



