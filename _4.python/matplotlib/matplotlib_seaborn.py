"""
import seaborn as sns       #海生, 自動把圖畫得比較好看

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

font_filename = (
    "C:/_git/vcs/_1.data/______test_files1/_font/TaipeiSansTCBeta-Regular.ttf"
)

import matplotlib as mpl
import matplotlib.font_manager as fm

fm.fontManager.addfont(font_filename)
mpl.rc("font", family="Taipei Sans TC Beta")

x = np.linspace(-5, 5, 200)
y = np.sinc(x)

plt.plot(x, y)
plt.title("原圖, 無海生")
plt.show()

# 把預設狀態存起來
saved_state = mpl.rcParams.copy()

# plt.xkcd()  #加此行變成搞笑風格

# 多此三行 變成海生風格
import seaborn as sns

sns.set()
plt.rcParams[
    "font.sans-serif"
] = "Microsoft JhengHei"  # 海生設定中文字型 將字體換成 Microsoft JhengHei

plt.plot(x, y)
plt.title("使用海生")
plt.show()

print("------------------------------------------------------------")  # 60個

plt.plot(x, y)
plt.title("再畫一新圖, 還是海生風格")
plt.show()

print("------------------------------------------------------------")  # 60個

mpl.rcParams.update(saved_state)

plt.plot(x, y)
plt.title("恢復成原風格, 無海生")
plt.show()

print("------------------------------------------------------------")  # 60個


"""
import seaborn as sns       #海生, 自動把圖畫得比較好看

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

plt.title("二項式分布 Binomial")
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=5, p=0.75, size=1000), kde=False)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.title("二項式分布 Binomial")
plt.xlabel("銷售張數", fontsize=14)
plt.ylabel("成功次數", fontsize=14)
sns.histplot(np.random.binomial(n=10, p=0.35, size=1000), kde=False)

plt.show()

print("------------------------------------------------------------")  # 60個

sns.set(color_codes=True)
x = np.linspace(-10, 10, 200)
y = np.sinc(x)

plt.plot(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

N = 200
data = np.random.randn(N)
print(np.mean(data))

ax = plt.subplot()
sns.histplot(data, kde=False, ax=ax)
_ = ax.set(title="Histogram", xlabel="x", ylabel="y")

plt.show()

print("------------------------------------------------------------")  # 60個

sns.get_dataset_names()

tips = sns.load_dataset("tips")
print(tips.shape)
print(tips.head())

print("------------------------------------------------------------")  # 60個

sns.set()
tips = sns.load_dataset("tips")
plt.scatter(tips.total_bill, tips.tip)
plt.xlabel("Total Bill")
plt.ylabel("Tip")

plt.show()

print("------------------------------------------------------------")  # 60個

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
male_tips = tips[tips.sex == "Male"]
female_tips = tips[tips.sex == "Female"]
plt.scatter(male_tips.total_bill, male_tips.tip, label="Male tips")
plt.scatter(female_tips.total_bill, female_tips.tip, label="Female tips")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

tips = sns.load_dataset("tips")
sns.catplot(x="day", y="tip", data=tips)

print("------------------------------------------------------------")  # 60個

titanic = sns.load_dataset("titanic")
print(titanic.head())

print("------------------------------------------------------------")  # 60個

titanic = sns.load_dataset("titanic")
sns.countplot(x="class", hue="survived", data=titanic)

print("------------------------------------------------------------")  # 60個

titanic = sns.load_dataset("titanic")
sns.countplot(x="sex", hue="survived", data=titanic)

print("------------------------------------------------------------")  # 60個

sns.set()
ranking = {
    "Toyota RAV4": 2958,
    "CMC Veryca": 1312,
    "Nissan Kicks": 1267,
    "Honda CRV": 1209,
    "Toyota Sienta": 1163,
    "Toyota Yaris": 936,
    "Toyota": 911,
    "Ford Focus": 873,
    "M-Benz C-Class": 749,
    "Honda HR-V": 704,
}

plt.bar(range(len(ranking.values())), ranking.values(), width=0.8)
plt.xticks(range(len(ranking.values())), ranking.keys(), rotation=45)

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("作業完成")
