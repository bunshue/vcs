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
interested_travel,computer_owner,age,home_value,loan_ratio,risk_score,marital,interested_sport,HH_grandparent,HH_dieting,HH_head_age,auto_member,interested_golf,interested_gambling,HH_has_children,HH_adults_num,interested_reading

|字段|含义|类型|
|:--:|:--:|
|interested_travel |旅行偏好|二分类|
|computer_owner |是否有家用电脑|二分类|
|age |估计的年龄|连续|
|home_value |房产价格|连续|
|loan_ratio|贷款比率|连续|
|risk_score |风险分数|连续|
|marital |婚姻状况估计|连续|
|interested_sport |运动偏好|连续|
|HH_grandparent|户主祖父母是否健在估计|连续|
|HH_dieting |户主节食偏好|连续|
|HH_head_age|户主年龄|连续|
|auto_member |驾驶俱乐部估计|连续|
|interested_golf |高尔夫偏好|二分类|
|interested_gambling |博彩偏好|二分类|
|HH_has_children |户主是否有孩子|二分类|
|HH_adults_num |家庭成年人数量|连续|
|interested_reading |阅读偏好|有序分类|

1、数据集中的变量较多，如果全部进入模型会导致模型解释困难。因此，一方面我们对于有相关性的变量进行降维，减少变量数目；另一方面，基于业务理解，我们预先将变量进行分组，使得同一组的变量能尽量解释业务的一个方面。比如本例中将变量分成三组，分别是家庭基本情况、财务状况和用户爱好，通过对每组变量分别进行聚类，获取用户的侧写，再将三个聚类结果进行综合，以获得较完整的用户画像。

2、本例中数据类型复杂，包含了连续变量、无序分类和有序分类变量。
由于K-means最好仅用于连续型变量聚类，因此需要对变量进行预处理。
对于有序分类变量，如果分类水平较多可以视作连续变量处理，否则视作无序分类变量一样处理，再进入模型；无序分类变量数目较少时，可以使用其哑变量编码进入模型。
本例中由于有较多的二分类变量，又集中在用户爱好这一方面，因此我们将interested_reading这一有序分类变量二值化，再与其他几个二分类变量一起进行汇总，
得到用户的“爱好广度”，使用“爱好广度”与其他连续型的爱好类变量进行聚类。

3、离散变量如HH_has_children一般不参与聚类，因为其本身就可以视作是簇的标签；如果为了后期解释模型时简化处理，在离散变量不多的情况之下，也可以做哑变量变换后进入模型。
读取数据
"""

travel = pd.read_csv("data/data_travel.csv", skipinitialspace=True)
cc = travel.head()
print(cc)

travel.describe(include="all")

# 数据预处理
# 填补缺失值
# 有缺失情况的变量皆为分类变量，且缺失比例并不高，因此用众数进行填补

fill_cols = ["interested_travel", "computer_owner", "HH_adults_num"]
fill_values = {col: travel[col].mode()[0] for col in fill_cols}

travel = travel.fillna(fill_values)

# 修正错误值
# 1)HH_has_children的分类水平以字符形式表示，需要转换为整型，同时其中的缺失值应当表示没有小孩，因此替换为0；
# 2）阅读爱好interested_reading中包含错误值“.”，将其以0进行替换，代表该用户对阅读没有兴趣。

cc = travel["interested_reading"].value_counts(dropna=False)
print(cc)

travel["HH_has_children"] = travel["HH_has_children"].replace(
    {"N": 0, "Y": 1, np.NaN: 0}
)

travel["interested_reading"] = (
    travel["interested_reading"].replace({".": "0"}).astype("int")
)


# 对离散型变量进行处理
# 使用k-means聚类，一般不分析离散变量，但可以根据业务理解，将离散型变量进行变换
# 先对interested_reading进行二值化

from sklearn.preprocessing import Binarizer

binarizer = Binarizer(threshold=1.5)
travel["interested_reading"] = binarizer.fit_transform(travel[["interested_reading"]])

# 生成二分类偏好填充率

interest = [
    "interested_travel",
    "computer_owner",
    "interested_golf",
    "interested_gambling",
    "interested_reading",
]
n_ = len(interest)

travel = travel.drop(interest, axis=1).assign(
    interest=travel[interest].sum(axis=1) / n_
)

cc = travel.head()
print(cc)

# 正态化、标准化
# 对不同类型变量执行不同处理，连续变量、有序分类变量及无序分类变量在处理上均有不同，因此先按类型对变量分组，不同组采用不同的处理策略
# 如果一个连续变量的可能取值很少，如marital（10个水平）、interest（5个水平）、HH_adults_num（8个水平）等，当将其作为普通连续变量一样进行分布转换，可能生成一些离群值（例如对marital使用scikit-learn进行正态转换，会发现1和10对应的数据点离开均值达到5个标准差）。因此本例中将这几个连续变量作为有序分类变量对待，但不进行分布转化，仅做标准化处理。

continuous_cols = [
    "age",
    "home_value",
    "risk_score",
    "interested_sport",
    "HH_dieting",
    "auto_member",
    "HH_grandparent",
    "HH_head_age",
    "loan_ratio",
]

categorical_cols = ["marital", "interest", "HH_adults_num"]

discreate_cols = ["HH_has_children"]

# 为了聚类后的簇大小比较接近，对于偏态严重的连续变量应转换其分布，令其接近正态分布或均匀分布
# 对连续变量正态化

travel[continuous_cols].hist(bins=25)
plt.show()

from sklearn.preprocessing import QuantileTransformer

qt = QuantileTransformer(n_quantiles=100, output_distribution="normal")
qt_data = qt.fit_transform(travel[continuous_cols])

pd.DataFrame(qt_data, columns=continuous_cols).hist(bins=25)
plt.show()

# 对有多个水平的有序分类变量进行标准化
# 如前所述，尽管HH_adults_num、marital和interest属于连续变量，但都仅有不到10个水平，因此与有序分类变量一样，仅做标准化

from sklearn.preprocessing import scale

scale_data = scale(travel[categorical_cols])

# 对二分类变量不做处理，合并各类型的变量
# 由于HH_has_children这个变量无法找到同类型变量,因此对该二分类变量不做处理，合并各类型的变量

data = np.hstack([qt_data, scale_data, travel[discreate_cols]])
data = pd.DataFrame(data, columns=continuous_cols + categorical_cols + discreate_cols)

cc = data.head()
print(cc)

# 连续变量筛选

# 首先查看其相关系数矩阵

cc = data.corr()
print(cc)

# 如果以0.6作为相关系数的上限。在相关系数矩阵中,发现'age'和 'HH_head_age'的相关系数超过0.6，因此决定, 'HH_head_age'不参与聚类运算.

# 对不同维度的数据分别建模并选择K值

household = ["age", "marital", "HH_adults_num", "HH_has_children", "HH_grandparent"]
finance = ["home_value", "risk_score", "loan_ratio"]
hobby = ["HH_dieting", "auto_member", "interest", "interested_sport"]

# 以下函数提供使用轮廓系数探查合理聚类数量的功能
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def cluster_plot(data, k_range=range(2, 12), n_init=5, sample_size=2000, n_jobs=-1):
    scores = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, n_init=n_init)
        kmeans.fit(data)
        sil = silhouette_score(data, kmeans.labels_, sample_size=sample_size)  # 計算輪廓分數
        scores.append([k, kmeans.inertia_, sil])

    scores_df = pd.DataFrame(scores, columns=["k", "sum_square_dist", "sil"])
    plt.figure(figsize=[9, 2])
    plt.subplot(121, ylabel="sum_square")
    plt.plot(scores_df.k, scores_df.sum_square_dist)
    plt.subplot(122, ylabel="silhouette_score 計算輪廓分數")
    plt.plot(scores_df.k, scores_df.sil)
    plt.show()


# 探查根据家庭情况进行聚类的K的数量
cluster_plot(data[household])

# 探查根据财务状况进行聚类的K的数量
cluster_plot(data[finance])

# 探查根据兴趣爱好进行聚类的K的数量
cluster_plot(data[hobby])

# 选择适当K值分别对三个维度聚类，并将相应标签连接至原始数据集


def k_means(data, k=2, n_init=5, n_jobs=-1):
    model = KMeans(n_clusters=k, n_init=n_init)
    model.fit(data)
    return model.labels_


household_labels = k_means(data[household], k=4)
finance_labels = k_means(data[finance], k=2)
hobby_labels = k_means(data[hobby], k=2)

label_names = ["HH", "finance", "hobby"]
labels = np.vstack([household_labels, finance_labels, hobby_labels]).T
travel_labels = travel.join(pd.DataFrame(labels, columns=label_names))

# 对各个簇的特征进行描述——使用原始数据

cc = travel_labels.groupby("hobby")[hobby].mean()
print(cc)

# 可以看到，hobby_labels=0的群体爱好广泛，热衷于运动和节食，有较大可能是汽车俱乐部会员，因此取名为“高兴趣度用户”。以下可以采用决策树方法进行更直观的探查

# 决策树：
from sklearn.tree import DecisionTreeClassifier

clf_hb = DecisionTreeClassifier()
clf_hb.fit(travel_labels[hobby], travel_labels["hobby"])

import pydotplus
from IPython.display import Image
import sklearn.tree as tree

# 決策樹可視化存檔
dot_hb = tree.export_graphviz(
    clf_hb,
    out_file=None,
    feature_names=hobby,
    class_names=["0", "1"],
    max_depth=2,
    filled=True,
)
graph_hb = pydotplus.graph_from_dot_data(dot_hb)
# NG Image(graph_hb.create_png())


cc = travel_labels.groupby("HH")[household].mean()
print(cc)


cc = travel_labels.groupby("finance")[finance].mean()
print(cc)

"""
其中一个用户群特征为：

 重点用户群A:

|标签|特征|
 |:--:|:--:|
 |家庭活跃用户(HH_labels=3)|年龄较轻，已婚有子女，家庭成员数居中|
 |低风险用户(finance_labels=0)|相对较贵的住宅，风险评估相对较低，具有较低的贷款比例|
 |高兴趣度用户(hobby_labels=0)|爱好广泛，热衷于节食与运动，有较大可能是汽车俱乐部会员|
可以进行多维汇总分析
"""
"""
其中一个用户群特征为：

    重点用户群A:

标签 	特征
家庭活跃用户(HH_labels=3) 	年龄较轻，已婚有子女，家庭成员数居中
低风险用户(finance_labels=0) 	相对较贵的住宅，风险评估相对较低，具有较低的贷款比例
高兴趣度用户(hobby_labels=0) 	爱好广泛，热衷于节食与运动，有较大可能是汽车俱乐部会员
可以进行多维汇总分析
"""
cc = travel_labels.groupby(label_names).mean()
print(cc)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
