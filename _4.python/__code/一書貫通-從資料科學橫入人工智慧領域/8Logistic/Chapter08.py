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

from sklearn import linear_model, metrics
from sklearn.model_selection import train_test_split

model_data = pd.read_csv("date_data.csv")
model_data.head()
Y = model_data["Dated"]
X = model_data.ix[ :,'income':'assets']
train_data, test_data, train_target, test_target = train_test_split(X, Y, test_size=0.2,random_state=0)

#建模

logistic_model = linear_model.LogisticRegression()
logistic_model.fit(train_data, train_target)

test_est = logistic_model.predict(test_data)
train_est = logistic_model.predict(train_data)
test_est_p = logistic_model.predict_proba(test_data)[:,1]
train_est_p = logistic_model.predict_proba(train_data)[:,1]

#决策（Decisions）类检验

print(metrics.classification_report(test_target, test_est))

metrics.accuracy_score(test_target, test_est)

#排序（Rankings）类检验
#ROC曲线

fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_est_p)
plt.figure(figsize=[6,6])
plt.plot(fpr_test, tpr_test,color='red')
plt.plot(fpr_train, tpr_train,color='black')
plt.title('ROC curve')

test_AUC=metrics.roc_auc_score(test_target, test_est_p)
train_AUC=metrics.roc_auc_score(train_target, train_est_p)
print ("test_AUC:",test_AUC, "train_AUC:",train_AUC)

#KS曲线

test_x_axis = np.arange(len(fpr_test))/float(len(fpr_test))
train_x_axis = np.arange(len(fpr_train))/float(len(fpr_train))
plt.figure(figsize=[6,6])
plt.plot(fpr_test, test_x_axis, color='blue')
plt.plot(tpr_test, test_x_axis, color='red')
#plt.plot(fpr_train, train_x_axis, color=red)
#plt.plot(tpr_train, train_x_axis, color=red)
plt.title('KS curve')

plt.show()

from scipy.stats import ks_2samp
ks_2samp(fpr_test,tpr_test)



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

