"""


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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

"""
第4讲 描述性统计分析基础

    数据集描述与属性说明
    ID 客户编号
    Suc_flag 成功入网标识
    ARPU 入网后ARPU
    PromCnt12 12个月内的营销次数
    PromCnt36 36个月内的营销次数
    PromCntMsg12 12个月内发短信的次数
    PromCntMsg36 36个月内发短信的次数
    Class 客户重要性等级(根据前运营商消费情况)
    Age 年龄
    Gender 性别
    HomeOwner 是否拥有住房
    AvgARPU 当地平均ARPU
    AvgHomeValue 当地房屋均价
    AvgIncome 当地人均收入
"""

# 读取数据
camp = pd.read_csv("data/teleco_camp2.csv")

# 数据预处理
camp.dtypes

camp.describe(include="all")

camp["Suc_flag"] = camp["Suc_flag"].astype("category")
camp["Class"] = camp["Class"].astype("category")

# 3.1 描述性统计与探索型数据分析

# 1.分类变量分析

cc = camp["Suc_flag"].groupby(camp["Suc_flag"]).count()
print(cc)

# 2.连续变量分析
# 2.1.数据的集中趋势 ARPU的均值与中位数

fs = camp["ARPU"]  # 可以使用camp.ARPU
type(fs)

print("mean = %6.4f" % fs.mean())  # 求fs的均值
print("median = %6.4f" % fs.median())  # 求fs的中位数
print("quantiles\n", fs.quantile([0.25, 0.5, 0.75]))  # 求a的上下四分位数与中位数

fs.plot(kind="hist")
plt.show()

# 2.2.数据的离散程度

# print ('mad = %6.4f' %fs.mad())      # 求平均绝对偏差 mad = np.abs(fs - fs.mean()).mean()
print("range = %6.4f" % (fs.max(skipna=True) - fs.min(skipna=True)))  # 求极差
print("var = %6.4f" % fs.var())  # 求方差
print("std = %6.4f" % fs.std())  # 求标准差

# 2.3.数据的偏度与峰度- ARPU:右偏

plt.hist(fs.dropna(), bins=15)
plt.show()

print("skewness = %6.4f" % fs.skew(skipna=True))
print("kurtosis = %6.4f" % fs.kurt(skipna=True))
"""
#2.4.分布- 正态分布模拟函数

from scipy import stats

x = map(lambda x: x / 10., range(-40, 41))
norm = stats.norm.pdf(x, loc=0, scale=1) # 随机正态分布概率密度(均值为0，标准差为1)
plt.plot(x, norm)
plt.show()

points = map(lambda x: x / 10.0, range(-40, 41))
plt.plot(points, stats.norm.cdf(points,loc=0, scale=1)) # 正态分布函数
plt.show()

#卡方分布模拟

x = range(1, 31)
chi = stats.chi2.pdf(x, df=3, loc=0, scale=1) #生成自由度为3的卡方分布概率密度
plt.plot(x, chi)
plt.show()

#t分布模拟

x = np.arange(-4, 4, 0.1)
student_t = stats.t.pdf(x, df=5, loc=0, scale=1)#生成自由度为5的t分布的概率密度值
norm = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x, student_t, 'b-')
plt.plot(x, norm, 'r--')
plt.show()
"""
# 3.2 apply\map\groupby及其它相关

data = pd.DataFrame(data={"a": range(1, 11), "b": np.random.randn(10)})
data.T

data.apply(np.mean)  # 等价于data.mean()，是其完整形式

data.apply(lambda x: x.astype("str")).dtypes  # DataFrame没有astype方法，只有Series有

(data["a"] - data["a"].mean()) / data["a"].std()

data["a"].map(
    lambda x: (x - data["a"].mean()) / data["a"].std()
)  # 等价于(data['a']- data['a'].mean()) / data['a'].std()

data["a"].map(lambda x: int(str(x), base=16))  # 不支持“广播”时，可以使用map进行函数映射

# 分组-应用/聚合

key = [1, 2] * 5
print(key)

group1, group2 = data.groupby(key)  # 使用groupby可按照‘key’进行分组，‘key’需与待分组数据有同样长度
print(group1)
print(group2)

data.groupby(key).aggregate(np.mean)
# 聚合函数在各分组中进行聚合，是data.groupby(key).mean()的完整形式，可传入函数或字符串(sum/mean/median/std/var等)，也可传入列表

data.groupby(key).agg({"a": "sum", "b": "count"})  # agg可以在多列上使用不同的聚合函数

data.groupby(key).transform(np.mean)  # 转换函数可在各分组内进行运算，将结果广播到原数据中

data.groupby(key).apply(np.mean)  # apply是一般化的‘分组-应用/聚合’函数，更灵活地实现aggregate或transform的功能

# *练习：对camp数据集，按照客户级别汇总ARPU

camp["ARPU"].groupby(camp["Class"]).apply(lambda x: x.describe())

camp[["PromCnt12", "PromCnt36"]].groupby(camp["Suc_flag"]).mean()

# crosstab 和pivot_table

pd.crosstab(camp.Suc_flag, camp.Class)

camp.pivot_table(
    ["PromCnt12", "PromCnt36"], index="Suc_flag", columns="Class", aggfunc=np.mean
)  # index、columns、aggfunc参数均可传入列表

# 3.3绘图

# 散点图

camp.plot(x="AvgARPU", y="ARPU", kind="scatter")  # 散点图
plt.text(60, 1100, "ARPU VS AvgARPU")  # 加标签
plt.show()

# 柱图/条形图、折线图

data.b.plot(kind="bar")  # 柱图
plt.show()

data.b.plot(kind="line")  # 折线图
plt.show()

# 直方图

camp[["PromCnt12", "PromCnt36"]].plot(stacked=False, kind="hist", alpha=0.3, bins=20)
camp[["PromCnt12", "PromCnt36"]].hist(alpha=0.8, bins=20, figsize=(10, 2))

# 饼图

gb = camp["Suc_flag"].groupby(camp["Suc_flag"]).count()
gb.plot(
    kind="pie",
    labels=["Yes", "No"],
    colors=["r", "g"],
    autopct="%.2f",
    fontsize=20,
    figsize=(6, 6),
)
plt.show()

# 箱线图

camp[["PromCnt12", "Suc_flag"]].boxplot(by="Suc_flag")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def stack2dim(raw, i, j, rotation=0, location="upper right"):
    """
    此函数是为了画两个维度标准化的堆积柱状图
    raw为pandas的DataFrame数据框
    i、j为两个分类变量的变量名称，要求带引号，比如"school"
    rotation：水平标签旋转角度，默认水平方向，如标签过长，可设置一定角度，比如设置rotation = 40
    location：分类标签的位置，如果被主体图形挡住，可更改为'upper left'
    """
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import math

    data_raw = pd.crosstab(raw[i], raw[j])
    data = data_raw.div(data_raw.sum(1), axis=0)  # 交叉表转换成比率，为得到标准化堆积柱状图

    # 计算x坐标，及bar宽度
    createVar = locals()
    x = [0]  # 每个bar的中心x轴坐标
    width = []  # bar的宽度
    k = 0
    for n in range(len(data)):
        # 根据频数计算每一列bar的宽度
        createVar["width" + str(n)] = list(data_raw.sum(axis=1))[n] / sum(
            data_raw.sum(axis=1)
        )
        width.append(createVar["width" + str(n)])
        if n == 0:
            continue
        else:
            k += (
                createVar["width" + str(n - 1)] / 2
                + createVar["width" + str(n)] / 2
                + 0.05
            )
            x.append(k)

    # 以下是通过频率交叉表矩阵生成一串对应堆积图每一块位置数据的数组，再把数组转化为矩阵
    y_mat = []
    n = 0
    y_level = len(data.columns)
    for p in range(data.shape[0]):
        for q in range(data.shape[1]):
            n += 1
            y_mat.append(data.iloc[p, q])
            if n == data.shape[0] * data.shape[1]:
                break
            elif n % y_level != 0:
                y_mat.extend([0] * (len(data) - 1))
            elif n % y_level == 0:
                y_mat.extend([0] * len(data))

    y_mat = np.array(y_mat).reshape(-1, len(data))
    y_mat = pd.DataFrame(y_mat)  # bar图中的y变量矩阵，每一行是一个y变量

    # 通过x，y_mat中的每一行y，依次绘制每一块堆积图中的每一块图

    from matplotlib import cm

    cm_subsection = [level for level in range(y_level)]
    colors = [cm.Pastel1(color) for color in cm_subsection]

    bottom = [0] * y_mat.shape[1]
    createVar = locals()
    for row in range(len(y_mat)):
        createVar["a" + str(row)] = y_mat.iloc[row, :]
        color = colors[row % y_level]

        if row % y_level == 0:
            bottom = bottom = [0] * y_mat.shape[1]
            if math.floor(row / y_level) == 0:
                label = data.columns.name + ": " + str(data.columns[row])
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    width=width[math.floor(row / y_level)],
                    label=label,
                    color=color,
                )
            else:
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    width=width[math.floor(row / y_level)],
                    color=color,
                )
        else:
            if math.floor(row / y_level) == 0:
                label = data.columns.name + ": " + str(data.columns[row])
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    bottom=bottom,
                    width=width[math.floor(row / y_level)],
                    label=label,
                    color=color,
                )
            else:
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    bottom=bottom,
                    width=width[math.floor(row / y_level)],
                    color=color,
                )

        bottom += createVar["a" + str(row)]

    plt.title(j + " vs " + i)
    group_labels = [str(name) for name in data.index]
    plt.xticks(x, group_labels, rotation=rotation)
    plt.ylabel(j)
    plt.legend(shadow=True, loc=location)
    plt.show()


# # 一、使用sndHsPr

import matplotlib

# get_ipython().magic('matplotlib inline')

snd = pd.read_csv("data/sndHsPr.csv")

snd["all_pr2"] = snd[["price", "AREA"]].apply(lambda x: x[0] * x[1], axis=1)
snd.head()

# ## 1、把dist變量重新編碼為中文，比如chaoyang改為朝陽區。1）先作頻次統計，然后繪制柱形圖圖展現每個區樣本的數量；

# ###  把dist變量重新編碼為中文，比如chaoyang改為朝陽區。

district = {
    "fengtai": "豐臺區",
    "haidian": "海淀區",
    "chaoyang": "朝陽區",
    "dongcheng": "東城區",
    "xicheng": "西城區",
    "shijingshan": "石景山區",
}
snd["district"] = snd.dist.map(district)
# snd_new = snd.drop('dist',axis = 1)
snd.head()

# 4.1 描述性統計與探索型數據分析
# ### 1單因子頻數:描述名義變量的分布

# snd.dist.value_counts()
snd.district.value_counts()
# type(snd.district.value_counts())
# snd.district.value_counts()/snd.district.count()

snd.district.value_counts().plot(kind="bar")
# snd.district.value_counts().plot(kind = 'pie')

# ### 2 單變量描述:描述連續變量的分布

snd.price.mean()

snd.price.median()

snd.price.std()

snd.price.skew()

snd.price.agg(["mean", "median", "sum", "std", "skew"])

snd.price.quantile([0.01, 0.5, 0.99])

snd.price.hist(bins=40)

# 4.2 描述統計方法大全
# ### 1.1表分析

sub_sch = pd.crosstab(snd.district, snd.school)
sub_sch

pd.crosstab(snd.dist, snd.subway).plot(kind="bar")

# pd.crosstab(snd.district,snd.school).plot(kind = 'bar')
t1 = pd.crosstab(snd.district, snd.school)
t1.plot(kind="bar", stacked=True)
type(t1)

sub_sch = pd.crosstab(snd.district, snd.school)
sub_sch["sum1"] = sub_sch.sum(1)
sub_sch.head()

sub_sch = sub_sch.div(sub_sch.sum1, axis=0)
sub_sch

sub_sch[[0, 1]].plot(kind="bar", stacked=True)

stack2dim(snd, i="district", j="school")

from pyecharts import Map

# from echarts-china-cities-pypkg import *
"""
官網給的解釋如下：
自從 0.3.2 開始，為了縮減項目本身的體積以及維持 pyecharts 項目的輕量化運行，pyecharts 將不再自帶地圖 js 文件。如用戶需要用到地圖圖表，可自行安裝對應的地圖文件包。下面介紹如何安裝。
全球國家地圖: echarts-countries-pypkg (1.9MB): 世界地圖和 213 個國家，包括中國地圖
中國省級地圖: echarts-china-provinces-pypkg (730KB)：23 個省，5 個自治區
中國市級地圖: echarts-china-cities-pypkg (3.8MB)：370 個中國城市:https://github.com/echarts-maps/echarts-china-cities-js
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
別注明，中國地圖在 echarts-countries-pypkg 里。
"""
snd_price = list(
    zip(
        snd.price.groupby(snd.district).mean().index,
        snd.price.groupby(snd.district).mean().values,
    )
)
attr, value = Map.cast(snd_price)
min_ = snd.price.groupby(snd.dist).mean().min()
max_ = snd.price.groupby(snd.dist).mean().max()

map = Map("北京各區房價", width=1200, height=600)
map.add(
    "",
    attr,
    value,
    maptype="北京",
    is_visualmap=True,
    visual_range=[min_, max_],
    visual_text_color="#000",
    is_label_show=True,
)
map.render()

# ![北京房價](北京各區房價.png)

# ### 1.2 分類匯總
snd.price.groupby(snd.district).mean().plot(kind="bar")

snd.price.groupby(snd.district).mean().sort_values(ascending=True).plot(kind="barh")

sns.boxplot(x="district", y="price", data=snd)

# ### 1.3 匯總表

snd.pivot_table(values="price", index="district", columns="school", aggfunc=np.mean)

snd.pivot_table(
    values="price", index="district", columns="school", aggfunc=np.mean
).plot(kind="bar")

# ### 1.4、兩個連續變量---使用area和price做散點圖，分析area是否影響單位面積房價

snd.plot.scatter(x="AREA", y="price")

# ### 1.5 雙軸圖 需要導入GDP數據

# - 按年度匯總GDP，并計算GDP增長率。繪制雙軸圖。GDP為柱子，GDP增長率為線。

gdp = pd.read_csv("data/gdp_gdpcr.csv", encoding="gbk")
gdp.head()

x = list(gdp.year)
GDP = list(gdp.GDP)
GDPCR = list(gdp.GDPCR)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.bar(x, GDP)
ax1.set_ylabel("GDP")
ax1.set_title("GDP of China(2000-2017)")
ax1.set_xlim(2000, 2018)

ax2 = ax1.twinx()
ax2.plot(x, GDPCR, "r")
ax2.set_ylabel("Increase Ratio")
ax2.set_xlabel("Year")


sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

######################################################################################################################################
# 以下內容為第8章內容
# ### 3、對age按照5歲間隔分段，命名為age_group，用loss_flag對age_group作logit圖。
# ### 1）手工計算Logit,即WOE

from sklearn import tree
from sklearn.model_selection import cross_val_score

class WoE:
    """
    Basic functionality for WoE bucketing of continuous and discrete variables
    :param self.bins: DataFrame WoE transformed variable and all related statistics
    :param self.iv: Information Value of the transformed variable
    """

    def __init__(
        self,
        qnt_num=16,
        min_block_size=16,
        spec_values=None,
        v_type="c",
        bins=None,
        t_type="b",
    ):
        """
        :param qnt_num: Number of buckets (quartiles) for continuous variable split
        :param min_block_size: minimum number of observation in each bucket (continuous variables)
        :param spec_values: List or Dictionary {'label': value} of special values (frequent items etc.)
        :param v_type: 'c' for continuous variable, 'd' - for discrete
        :param bins: Predefined bucket borders for continuous variable split
        :t_type : Binary 'b' or continous 'c' target variable
        :return: initialized class
        """
        self.__qnt_num = qnt_num  # Num of buckets/quartiles
        self._predefined_bins = (
            None if bins is None else np.array(bins)
        )  # user bins for continuous variables
        self.type = v_type  # if 'c' variable should be continuous, if 'd' - discrete
        self._min_block_size = min_block_size  # Min num of observation in bucket
        self._gb_ratio = None  # Ratio of good and bad in the sample
        self.bins = None  # WoE Buckets (bins) and related statistics
        self.df = None  # Training sample DataFrame with initial data and assigned woe
        self.qnt_num = (
            None  # Number of quartiles used for continuous part of variable binning
        )
        self.t_type = t_type  # Type of target variable
        if (
            type(spec_values) == dict
        ):  # Parsing special values to dict for cont variables
            self.spec_values = {}
            for k, v in spec_values.items():
                if v.startswith("d_"):
                    self.spec_values[k] = v
                else:
                    self.spec_values[k] = "d_" + v
        else:
            if spec_values is None:
                self.spec_values = {}
            else:
                self.spec_values = {i: "d_" + str(i) for i in spec_values}

    def fit(self, x, y):
        """
        Fit WoE transformation
        :param x: continuous or discrete predictor
        :param y: binary target variable
        :return: WoE class
        """
        # Data quality checks
        if not isinstance(x, pd.Series) or not isinstance(y, pd.Series):
            raise TypeError("pandas.Series type expected")
        if not x.size == y.size:
            raise Exception("Y size don't match Y size")
        # Calc total good bad ratio in the sample
        t_bad = np.sum(y)
        if t_bad == 0 or t_bad == y.size:
            raise ValueError("There should be BAD and GOOD observations in the sample")
        if np.max(y) > 1 or np.min(y) < 0:
            raise ValueError("Y range should be between 0 and 1")
        # setting discrete values as special values
        if self.type == "d":
            sp_values = {i: "d_" + str(i) for i in x.unique()}
            if len(sp_values) > 100:
                raise type(
                    "DiscreteVarOverFlowError",
                    (Exception,),
                    {
                        "args": (
                            "Discrete variable with too many unique values (more than 100)",
                        )
                    },
                )
            else:
                if self.spec_values:
                    sp_values.update(self.spec_values)
                self.spec_values = sp_values
        # Make data frame for calculations
        df = pd.DataFrame({"X": x, "Y": y, "order": np.arange(x.size)})
        # Separating NaN and Special values
        df_sp_values, df_cont = self._split_sample(df)
        # # labeling data
        df_cont, c_bins = self._cont_labels(df_cont)
        df_sp_values, d_bins = self._disc_labels(df_sp_values)
        # getting continuous and discrete values together
        # self.df = df_sp_values.append(df_cont)
        # self.df = df_sp_values.append(df_cont, ignore_index=True)
        #print(df_sp_values.shape)
        #print(df_cont.shape)
        self.df = pd.concat([df_sp_values, df_cont], axis=0, ignore_index=True)
        
        #self.bins = d_bins.append(c_bins)
        #self.bins = d_bins.append(c_bins)
        self.bins = pd.concat([d_bins, c_bins], axis=0, ignore_index=True)
        
        # calculating woe and other statistics
        self._calc_stat()
        # sorting appropriately for further cutting in transform method
        self.bins.sort_values("bins", inplace=True)
        # returning to original observation order
        self.df.sort_values("order", inplace=True)
        self.df.set_index(x.index, inplace=True)
        return self

    def fit_transform(self, x, y):
        """
        Fit WoE transformation
        :param x: continuous or discrete predictor
        :param y: binary target variable
        :return: WoE transformed variable
        """
        self.fit(x, y)
        return self.df["woe"]

    def _split_sample(self, df):
        if self.type == "d":
            return df, None
        sp_values_flag = (
            df["X"].isin(self.spec_values.keys()).values | df["X"].isnull().values
        )
        df_sp_values = df[sp_values_flag].copy()
        df_cont = df[np.logical_not(sp_values_flag)].copy()
        return df_sp_values, df_cont

    def _disc_labels(self, df):
        df["labels"] = df["X"].apply(
            lambda x: self.spec_values[x]
            if x in self.spec_values.keys()
            else "d_" + str(x)
        )
        d_bins = pd.DataFrame({"bins": df["X"].unique()})
        d_bins["labels"] = d_bins["bins"].apply(
            lambda x: self.spec_values[x]
            if x in self.spec_values.keys()
            else "d_" + str(x)
        )
        return df, d_bins

    def _cont_labels(self, df):
        # check whether there is a continuous part
        if df is None:
            return None, None
        # Max buckets num calc
        self.qnt_num = (
            int(
                np.minimum(df["X"].unique().size / self._min_block_size, self.__qnt_num)
            )
            + 1
        )
        # cuts - label num for each observation, bins - quartile thresholds
        bins = None
        cuts = None
        if self._predefined_bins is None:
            try:
                cuts, bins = pd.qcut(df["X"], self.qnt_num, retbins=True, labels=False)
            except ValueError as ex:
                if ex.args[0].startswith("Bin edges must be unique"):
                    ex.args = (
                        "Please reduce number of bins or encode frequent items as special values",
                    ) + ex.args
                    raise
            bins = np.append((-float("inf"),), bins[1:-1])
        else:
            bins = self._predefined_bins
            if bins[0] != float("-Inf"):
                bins = np.append((-float("inf"),), bins)
            cuts = pd.cut(
                df["X"],
                bins=np.append(bins, (float("inf"),)),
                labels=np.arange(len(bins)).astype(str),
            )
        df["labels"] = cuts.astype(str)
        c_bins = pd.DataFrame(
            {"bins": bins, "labels": np.arange(len(bins)).astype(str)}
        )
        return df, c_bins

    def _calc_stat(self):
        # calculating WoE
        stat = (
            self.df.groupby("labels")["Y"]
            .agg(mean=np.mean, bad=np.count_nonzero, obs=np.size)
            .copy()
        )
        if self.t_type != "b":
            stat["bad"] = stat["mean"] * stat["obs"]
        stat["good"] = stat["obs"] - stat["bad"]
        t_good = np.maximum(stat["good"].sum(), 0.5)
        t_bad = np.maximum(stat["bad"].sum(), 0.5)
        stat["woe"] = stat.apply(self._bucket_woe, axis=1) + np.log(t_good / t_bad)
        iv_stat = (stat["bad"] / t_bad - stat["good"] / t_good) * stat["woe"]
        self.iv = iv_stat.sum()
        # adding stat data to bins
        self.bins = pd.merge(stat, self.bins, left_index=True, right_on=["labels"])
        label_woe = self.bins[["woe", "labels"]].drop_duplicates()
        self.df = pd.merge(self.df, label_woe, left_on=["labels"], right_on=["labels"])

    def transform(self, x):
        """
        Transforms input variable according to previously fitted rule
        :param x: input variable
        :return: DataFrame with transformed with original and transformed variables
        """
        if not isinstance(x, pd.Series):
            raise TypeError("pandas.Series type expected")
        if self.bins is None:
            raise Exception("Fit the model first, please")
        df = pd.DataFrame({"X": x, "order": np.arange(x.size)})
        # splitting to discrete and continous pars
        df_sp_values, df_cont = self._split_sample(df)

        # function checks existence of special values, raises error if sp do not exist in training set
        def get_sp_label(x_):
            if x_ in self.spec_values.keys():
                return self.spec_values[x_]
            else:
                str_x = "d_" + str(x_)
                if str_x in list(self.bins["labels"]):
                    return str_x
                else:
                    raise ValueError(
                        "Value " + str_x + " does not exist in the training set"
                    )

        # assigning labels to discrete part
        df_sp_values["labels"] = df_sp_values["X"].apply(get_sp_label)
        # assigning labels to continuous part
        c_bins = self.bins[self.bins["labels"].apply(lambda z: not z.startswith("d_"))]
        if not self.type == "d":
            cuts = pd.cut(
                df_cont["X"],
                bins=np.append(c_bins["bins"], (float("inf"),)),
                labels=c_bins["labels"],
            )
            df_cont["labels"] = cuts.astype(str)
        # Joining continuous and discrete parts
        # df = df_sp_values.append(df_cont)
        # df = df_sp_values.append(df_cont)
        df = pd.concat([df_sp_values, df_cont], axis=0, ignore_index=True)
        
        # assigning woe
        df = pd.merge(
            df, self.bins[["woe", "labels"]], left_on=["labels"], right_on=["labels"]
        )
        # returning to original observation order
        df.sort_values("order", inplace=True)
        return df.set_index(x.index)

    def merge(self, label1, label2=None):
        """
        Merge of buckets with given labels
        In case of discrete variable, both labels should be provided. As the result labels will be marget to one bucket.
        In case of continous variable, only label1 should be provided. It will be merged with the next label.
        :param label1: first label to merge
        :param label2: second label to merge
        :return:
        """
        spec_values = self.spec_values.copy()
        c_bins = self.bins[
            self.bins["labels"].apply(lambda x: not x.startswith("d_"))
        ].copy()
        if label2 is None and not label1.startswith(
            "d_"
        ):  # removing bucket for continuous variable
            c_bins = c_bins[c_bins["labels"] != label1]
        else:
            if not (label1.startswith("d_") and label2.startswith("d_")):
                raise Exception("Labels should be discrete simultaneously")
            bin1 = self.bins[self.bins["labels"] == label1]["bins"].iloc[0]
            bin2 = self.bins[self.bins["labels"] == label2]["bins"].iloc[0]
            spec_values[bin1] = label1 + "_" + label2
            spec_values[bin2] = label1 + "_" + label2
        new_woe = WoE(
            self.__qnt_num,
            self._min_block_size,
            spec_values,
            self.type,
            c_bins["bins"],
            self.t_type,
        )
        return new_woe.fit(self.df["X"], self.df["Y"])

    def plot(self):
        """
        Plot WoE transformation and default rates
        :return: plotting object
        """
        index = np.arange(self.bins.shape[0])
        bar_width = 0.8
        figsize=(6, 6)
        woe_fig = plt.figure(figsize=figsize)
        plt.title("Number of Observations and WoE per bucket")
        ax = woe_fig.add_subplot(111)
        ax.set_ylabel("Observations")
        plt.xticks(index + bar_width / 2, self.bins["labels"])
        plt.bar(index, self.bins["obs"], bar_width, color="b", label="Observations")
        ax2 = ax.twinx()
        ax2.set_ylabel("Weight of Evidence")
        ax2.plot(
            index + bar_width / 2,
            self.bins["woe"],
            "bo-",
            linewidth=4.0,
            color="r",
            label="WoE",
        )
        handles1, labels1 = ax.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels()
        handles = handles1 + handles2
        labels = labels1 + labels2
        plt.legend(handles, labels)
        woe_fig.autofmt_xdate()
        return woe_fig

    def optimize(self, criterion=None, fix_depth=None, max_depth=None, cv=3):
        """
        WoE bucketing optimization (continuous variables only)
        :param criterion: binary tree split criteria
        :param fix_depth: use tree of a fixed depth (2^fix_depth buckets)
        :param max_depth: maximum tree depth for a optimum cross-validation search
        :param cv: number of cv buckets
        :return: WoE class with optimized continuous variable split
        """
        if self.t_type == "b":
            tree_type = tree.DecisionTreeClassifier
        else:
            tree_type = tree.DecisionTreeRegressor
        m_depth = int(np.log2(self.__qnt_num)) + 1 if max_depth is None else max_depth
        cont = self.df["labels"].apply(lambda z: not z.startswith("d_"))
        x_train = np.array(self.df[cont]["X"])
        y_train = np.array(self.df[cont]["Y"])
        x_train = x_train.reshape(x_train.shape[0], 1)
        start = 1
        cv_scores = []
        if fix_depth is None:
            for i in range(start, m_depth):
                if criterion is None:
                    d_tree = tree_type(max_depth=i)
                else:
                    d_tree = tree_type(criterion=criterion, max_depth=i)
                scores = cross_val_score(d_tree, x_train, y_train, cv=cv)
                cv_scores.append(scores.mean())
            best = np.argmax(cv_scores) + start
        else:
            best = fix_depth
        final_tree = tree_type(max_depth=best)
        final_tree.fit(x_train, y_train)
        opt_bins = final_tree.tree_.threshold[final_tree.tree_.threshold > 0]
        opt_bins = np.sort(opt_bins)
        new_woe = WoE(
            self.__qnt_num,
            self._min_block_size,
            self.spec_values,
            self.type,
            opt_bins,
            self.t_type,
        )
        return new_woe.fit(self.df["X"], self.df["Y"])

    @staticmethod
    def _bucket_woe(x):
        t_bad = x["bad"]
        t_good = x["good"]
        t_bad = 0.5 if t_bad == 0 else t_bad
        t_good = 0.5 if t_good == 0 else t_good
        return np.log(t_bad / t_good)

""" 測試上面這個class
# Examples
if __name__ == "__main__":
    # Set target type: 'b' for default/non-default, 'c' for continous pd values
    t_type_ = "c"
    # Set sample size
    N = 300
    # Random variables
    x1 = np.random.rand(N)
    x2 = np.random.rand(N)
    if t_type_ == "b":
        y_ = np.where(
            np.random.rand(
                N,
            )
            + x1
            + x2
            > 2,
            1,
            0,
        )
    else:
        y_ = np.random.rand(N) + x1 + x2
        y_ = (y_ - np.min(y_)) / (np.max(y_) - np.min(y_)) / 2
    # Inserting special values
    x1[0:20] = float("nan")
    x1[30:50] = float(0)
    x1[60:80] = float(1)
    x2[0:20] = float("nan")
    # Initialize WoE object
    woe_def = WoE()
    woe = WoE(7, 30, spec_values={0: "0", 1: "1"}, v_type="c", t_type=t_type_)
    # Transform x1
    woe.fit(pd.Series(x1), pd.Series(y_))
    # Transform x2 using x1 transformation rules
    woe.transform(pd.Series(x2))
    # Optimize x1 transformation using tree with maximal depth = 5 (optimal depth is chosen by cross-validation)
    woe2 = woe.optimize(max_depth=5)
    # Merge discrete buckets
    woe3 = woe.merge("d_0", "d_1")
    # Merge 2 and 3 continuous buckets
    woe4 = woe3.merge("2")
    # Print Statistics
    print(woe.bins)
    # print(woe2.bins)
    # print(woe3.bins)
    print(woe4.bins)
    # Plot and show WoE graph
    woe.plot()
    plt.show()
    woe2.plot()
    plt.show()
"""


auto = pd.read_csv("data/auto_ins.csv", encoding="gbk")

auto.Loss = auto.Loss.map(lambda x: 1 if x > 0 else 0)

bins = [21, 26, 31, 36, 41, 46, 51, 56, 61, 67]
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
auto["age_group"] = pd.cut(auto.Age, bins, labels=labels, right=False)

log_tab = pd.crosstab(auto.age_group, auto.Loss)
log_tab

log_tab[["p0", "p1"]] = log_tab[[0, 1]].apply(lambda x: x / sum(x))
log_tab["log"] = log_tab[["p1", "p0"]].apply(lambda x: np.log(x[0] / x[-1]), axis=1)
log_tab

log_tab.log.plot()

woe = WoE(v_type="d")
woe.fit(auto.age_group, auto.Loss)
woe.plot()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
