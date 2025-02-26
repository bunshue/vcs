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
|变量名|变量说明|
|:--:|:--:|
|ID	|数据库中每个人的ID|
|target_flag|	是否购买过目标产品|
|gender|	性别|
|education	|教育背景|
|home_value|	所住房屋的价值|
|age	|年龄信息，以类似25-35分组表示|
|buy_online	|有无网购记录|
|mosaic_group	|根据居住区域归纳的描述消费心理的变量|
|marital	|婚姻状态|
|poc	|有无小孩|
|occupation	|职业信息|
|mortgage	|住房贷款信息|
|home_owner	|所住房屋是否自有|
|region	|所处地区信息|
|new_car|	购买新车的可能性（1代表最可能）|
|home_income|	家庭收入信息（A代表最低，L代表最高）|
"""
# 读取数据，并对数据进行初步探索

# get_ipython().magic('matplotlib inline')

pd.set_option("display.max_columns", None)

train = pd.read_csv("data/response_data_train.csv", skipinitialspace=True)
test = pd.read_csv("data/response_data_test.csv", skipinitialspace=True)
print(train.shape)
print(test.shape)

# (30000, 15)
# (10000, 15)

train.describe(include="all")

cols = train.columns.tolist()
x_c = ["home_value", "new_car"]
x_d = list(set(cols) - set(x_c))
x_d.remove("target_flag")

# 数据预处理

# 编码同时填补缺失值


def label_encoder(series):
    cat = series.value_counts(dropna=False)
    len_series = len(series)
    return {k: v for k, v in zip(cat.index, range(len_series))}


pd.set_option("future.no_silent_downcasting", True)

for col in x_d:
    encoder = label_encoder(train[col])
    train[col].replace(encoder, inplace=True)  # Encode train
    test[col].replace(encoder, inplace=True)  # Encode test


encoder = label_encoder(train.target_flag)
train.target_flag.replace(encoder, inplace=True)
test.target_flag.replace(encoder, inplace=True)

# WOE编码；sklearn中的决策树算法默认所有输入变量作为连续变量处理，因此对于分类变量，需要进行WOE转换。鉴于此，可以将所有变量统一作WOE转换

# Jupyter中引入包，只要包放在同一个文件加下即可

from woe import WoE

for col in x_d:
    woe = WoE(v_type="d", t_type="b")
    woe.fit(train[col], train.target_flag)
    train[col] = woe.transform(train[col])["woe"]
    test[col] = woe.transform(test[col])["woe"]

cc = test.head()
print(cc)

# 建模
# 通过搜索参数网格，选择模型的最优超参


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

dt = DecisionTreeClassifier()
grid = {
    "max_leaf_nodes": np.arange(32, 64, 6),
    "min_samples_split": np.arange(50, 301, 50),
}
cv = GridSearchCV(dt, grid, scoring="roc_auc", cv=4, n_jobs=-1)
cv.fit(train.ix[:, 1:], train["target_flag"])

print("best_score:%2.4f" % cv.best_score_)
print("best_params: %s" % cv.best_params_)

"""
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

"""
# best_score:0.7405
# best_params: {'max_leaf_nodes': 56, 'min_samples_split': 50}

from sklearn.metrics import roc_auc_score, roc_curve

test_p = cv.predict_proba(test.ix[:, 1:])
print(roc_auc_score(test.target_flag, test_p[:, 1]))

"""
0.7376618176618177

.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

# 通过筛选变量可以改善模型过拟合的情况
# 决策树生长中，每一步都会计算变量的重要性，最终能够汇总各变量对整个模型的重要性。因此自然会想到利用决策树本身计算的变量重要性进行变量筛选
"""
imp = cv.best_estimator_.feature_importances_
list(zip(train.ix[:, 1:].columns, imp))
"""
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing



[('gender', 0.17690022113950998),
 ('education', 0.10046755505360414),
 ('home_value', 0.075251210069869),
 ('age', 0.13261235794759016),
 ('buy_online', 0.0739696987615009),
 ('mosaic_group', 0.33670508714260966),
 ('marital', 0.030026959065899927),
 ('poc', 0.0),
 ('occupation', 0.035910899584784925),
 ('mortgage', 0.01803367198613054),
 ('home_owner', 0.0),
 ('region', 0.002560147359173822),
 ('new_car', 0.009602062467822884),
 ('home_income', 0.007960129421504128)]

# 去除部分重要性不高的变量
"""
train = train.drop(["poc", "home_owner", "mortgage", "region", "home_income"], axis=1)
test = test.drop(["poc", "home_owner", "mortgage", "region", "home_income"], axis=1)


# 重新拟合模型


cv.fit(train.ix[:, 1:], train["target_flag"])

print("best_score:%2.4f" % cv.best_score_)
print("best_params: %s" % cv.best_params_)
"""
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

best_score:0.7400
best_params: {'max_leaf_nodes': 56, 'min_samples_split': 300}

当去除了部分变量后，模型的表现有所提升
"""
train_p = cv.predict_proba(train.ix[:, 1:])
test_p = cv.predict_proba(test.ix[:, 1:])
print(roc_auc_score(test.target_flag, test_p[:, 1]))
"""
0.7397821997821997

.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing

  #Entry point for launching an IPython kernel.
.ix is deprecated. Please use
.loc for label based indexing or
.iloc for positional indexing


可以通过绘制ROC曲线来观察模型过拟合的情况
"""

fpr_test, tpr_test, th_test = roc_curve(test.target_flag, test_p[:, 1])

fpr_train, tpr_train, th_train = roc_curve(train.target_flag, train_p[:, 1])

plt.figure(figsize=[4, 4])
plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
plt.show()


# 可视化

import pydotplus
from IPython.display import Image  # 用IPython
import sklearn.tree as tree

# 決策樹可視化存檔
dot_data = tree.export_graphviz(
    cv.best_estimator_,
    out_file=None,
    feature_names=train.columns[1:],
    max_depth=2,
    class_names=["0", "1"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())  # 用IPython顯示圖片
# graph.write_pdf('response_decision_tree.pdf')

from sklearn.tree import _tree


def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, tree_.value[node]))

    recurse(0, 1)


tree_to_code(cv.best_estimator_, train.columns[1:])
"""
def tree(gender, education, home_value, age, buy_online, mosaic_group, marital, occupation, new_car):
  if mosaic_group <= -0.22991183400154114:
    if education <= -0.2986419200897217:
      if buy_online <= -0.1779557317495346:
        if gender <= -0.02771008014678955:
          return [[1338.  181.]]
        else:  # if gender > -0.02771008014678955
          if home_value <= 157472.0:
            return [[765. 169.]]
          else:  # if home_value > 157472.0
            if occupation <= 0.33799272775650024:
              return [[193.  77.]]
            else:  # if occupation > 0.33799272775650024
              return [[14. 21.]]
      else:  # if buy_online > -0.1779557317495346
        if age <= 0.09817798435688019:
          if gender <= -0.02771008014678955:
            return [[729. 180.]]
          else:  # if gender > -0.02771008014678955
            if home_value <= 102020.0:
              return [[252.  87.]]
            else:  # if home_value > 102020.0
              return [[223. 142.]]
        else:  # if age > 0.09817798435688019
          if home_value <= 209607.0:
            return [[610. 357.]]
          else:  # if home_value > 209607.0
            return [[ 87. 112.]]
    else:  # if education > -0.2986419200897217
      if buy_online <= -0.1779557317495346:
        if gender <= -0.02771008014678955:
          return [[887. 265.]]
        else:  # if gender > -0.02771008014678955
          if occupation <= 0.33799272775650024:
            if home_value <= 110806.5:
              if education <= 0.1473049521446228:
                return [[251.  68.]]
              else:  # if education > 0.1473049521446228
                return [[106.  65.]]
            else:  # if home_value > 110806.5
              return [[250. 175.]]
          else:  # if occupation > 0.33799272775650024
            return [[122. 174.]]
      else:  # if buy_online > -0.1779557317495346
        if age <= -0.580400824546814:
          if gender <= -0.02771008014678955:
            return [[341. 112.]]
          else:  # if gender > -0.02771008014678955
            return [[295. 263.]]
        else:  # if age > -0.580400824546814
          if marital <= -0.2965794801712036:
            if occupation <= -0.08785676211118698:
              if age <= 0.09817798435688019:
                return [[188.  77.]]
              else:  # if age > 0.09817798435688019
                return [[165. 133.]]
            else:  # if occupation > -0.08785676211118698
              if gender <= -0.02771008014678955:
                return [[134. 112.]]
              else:  # if gender > -0.02771008014678955
                return [[ 83. 139.]]
          else:  # if marital > -0.2965794801712036
            if new_car <= 5.5:
              if gender <= -0.02771008014678955:
                return [[259. 334.]]
              else:  # if gender > -0.02771008014678955
                return [[249. 538.]]
            else:  # if new_car > 5.5
              return [[291. 278.]]
  else:  # if mosaic_group > -0.22991183400154114
    if gender <= -0.02771008014678955:
      if age <= 0.09817798435688019:
        if buy_online <= -0.1779557317495346:
          if mosaic_group <= 0.17433977127075195:
            return [[405. 100.]]
          else:  # if mosaic_group > 0.17433977127075195
            if occupation <= -0.3222179114818573:
              return [[87. 18.]]
            else:  # if occupation > -0.3222179114818573
              return [[279. 155.]]
        else:  # if buy_online > -0.1779557317495346
          if marital <= -0.2965794801712036:
            return [[821. 404.]]
          else:  # if marital > -0.2965794801712036
            if age <= -0.580400824546814:
              return [[153.  79.]]
            else:  # if age > -0.580400824546814
              return [[305. 306.]]
      else:  # if age > 0.09817798435688019
        if buy_online <= -0.1779557317495346:
          if home_value <= 125104.5:
            return [[137.  58.]]
          else:  # if home_value > 125104.5
            if age <= 0.45266157388687134:
              return [[249. 190.]]
            else:  # if age > 0.45266157388687134
              return [[ 99. 133.]]
        else:  # if buy_online > -0.1779557317495346
          if home_value <= 290463.0:
            if occupation <= -0.3222179114818573:
              return [[118.  81.]]
            else:  # if occupation > -0.3222179114818573
              if new_car <= 6.5:
                return [[539. 722.]]
              else:  # if new_car > 6.5
                return [[54. 33.]]
          else:  # if home_value > 290463.0
            return [[ 663. 1245.]]
    else:  # if gender > -0.02771008014678955
      if home_value <= 209333.0:
        if occupation <= -0.08785676211118698:
          if age <= -0.2590912878513336:
            return [[426. 259.]]
          else:  # if age > -0.2590912878513336
            if new_car <= 5.5:
              if buy_online <= -0.1779557317495346:
                return [[132. 128.]]
              else:  # if buy_online > -0.1779557317495346
                if age <= 0.31054380536079407:
                  return [[128. 153.]]
                else:  # if age > 0.31054380536079407
                  return [[117. 252.]]
            else:  # if new_car > 5.5
              return [[154. 109.]]
        else:  # if occupation > -0.08785676211118698
          if education <= 0.1473049521446228:
            if age <= 0.31054380536079407:
              return [[134. 127.]]
            else:  # if age > 0.31054380536079407
              return [[ 69. 142.]]
          else:  # if education > 0.1473049521446228
            return [[144. 421.]]
      else:  # if home_value > 209333.0
        if age <= -0.2590912878513336:
          if education <= 0.1473049521446228:
            if mosaic_group <= 0.17433977127075195:
              return [[149. 109.]]
            else:  # if mosaic_group > 0.17433977127075195
              return [[280. 402.]]
          else:  # if education > 0.1473049521446228
            if education <= 0.41808974742889404:
              return [[ 15. 122.]]
            else:  # if education > 0.41808974742889404
              return [[273. 565.]]
        else:  # if age > -0.2590912878513336
          if marital <= -0.2965794801712036:
            if occupation <= -0.3222179114818573:
              return [[68. 76.]]
            else:  # if occupation > -0.3222179114818573
              return [[281. 625.]]
          else:  # if marital > -0.2965794801712036
            if education <= -0.2986419200897217:
              if new_car <= 3.5:
                return [[138. 403.]]
              else:  # if new_car > 3.5
                return [[59. 67.]]
            else:  # if education > -0.2986419200897217
              if home_value <= 375504.5:
                if buy_online <= -0.1779557317495346:
                  return [[ 91. 195.]]
                else:  # if buy_online > -0.1779557317495346
                  return [[ 251. 1092.]]
              else:  # if home_value > 375504.5
                if mosaic_group <= 0.4319630265235901:
                  return [[ 66. 193.]]
                else:  # if mosaic_group > 0.4319630265235901
                  return [[ 289. 1972.]]
"""
# 使用组合方法

from sklearn.ensemble import GradientBoostingClassifier

gbc = GradientBoostingClassifier()
gbc.fit(train.ix[:, 1:], train.target_flag)
gbc_train_p = gbc.predict_proba(train.ix[:, 1:])
gbc_test_p = gbc.predict_proba(test.ix[:, 1:])

print(roc_auc_score(train.target_flag, gbc_train_p[:, 1]))
print(roc_auc_score(test.target_flag, gbc_test_p[:, 1]))

# 0.7706014100668234
# 0.7576385376385377

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
