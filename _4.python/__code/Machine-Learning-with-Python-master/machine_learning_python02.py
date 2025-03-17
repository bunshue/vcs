"""
machine_learning_python02

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

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Complexity and learning curve analysis for classification

#Synthetic data set from scikit-learn

sns.set_style("white")

from sklearn import datasets

X, y = datasets.make_hastie_10_2(n_samples=12000, random_state=1)

df=pd.DataFrame(data=X,columns=['X'+str(i) for i in range(1,11)])
cc = df.head()
print(cc)

df['y']=pd.Series(y)
cc = df.head()
print(cc)

#Basic visualizations

i=1
plt.figure(figsize=(20,20))
for c in df.columns[:-1]:
    plt.subplot(4,3,i)
    plt.title(f"Histogram of variable {c}")
    plt.yticks()
    plt.xticks()
    plt.hist(df[c],bins=20,color='orange',edgecolor='k')
    i+=1
show()

i=1
plt.figure(figsize=(20,20))
for c in df.columns[:-1]:
    plt.subplot(4,3,i)
    plt.title(f"Boxplot of {c}")
    plt.yticks()
    plt.xticks()
    sns.boxplot(y=df[c],x=df['y'])
    i+=1
show()

df_sample=df.sample(frac=0.01)
sns.set(style="ticks")
""" NG pairplot
g=sns.pairplot(df_sample,vars=["X1","X2","X3"],
               hue="y",markers=["o", "s"],
               diag_kind="kde",diag_kws=dict(shade=True),plot_kws=dict(s=100,alpha=0.75))
"""
# Test/train/validation split

X=df.drop('y',axis=1)
y=df['y']

# First divide train and test data in 70:30 ratio

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# Then further divide the test set in 50:50 ratio into validation set and test set

X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.50)

cc = X_test.head()
print(cc)

cc = X_val.head()
print(cc)

# Show the shape of these sets

print("Shape of validation set:", X_val.shape)
print("Shape of test set:", X_test.shape)
print("Shape of training set:", X_train.shape)

# Decision Tree model

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(criterion='gini',max_depth=10,min_samples_leaf=5)

dtree.fit(X_train,y_train)

# Predictions and evaluation

predictions = dtree.predict(X_val)

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

score1=accuracy_score(y_val,predictions)
print(score1)

# 0.7088888888888889

# Varying hyperparameters
# Varying max_depth

val_acc_max_depth=[]
val_f1_max_depth=[]
train_acc_max_depth=[]
train_f1_max_depth=[]
val_range=(1,81,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    dtree = DecisionTreeClassifier(criterion='gini',max_depth=i,min_samples_leaf=1)
    dtree.fit(X_train,y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    train_acc_max_depth.append(acc_train)
    train_f1_max_depth.append(f1_train)
    val_acc_max_depth.append(acc_val)
    val_f1_max_depth.append(f1_val)

plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_max_depth,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_max_depth,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Max depth of the decision tree")
plt.ylabel("Accuracy")
plt.ylim(0.5,1.05)
show()

# Varying min_samples_leaf with max_depth = 20

val_acc_min_samples_leaf=[]
val_f1_min_samples_leaf=[]
train_acc_min_samples_leaf=[]
train_f1_min_samples_leaf=[]
val_range=(1,41,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    dtree = DecisionTreeClassifier(criterion='gini',max_depth=20,min_samples_leaf=i)
    dtree.fit(X_train,y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    train_acc_min_samples_leaf.append(acc_train)
    train_f1_min_samples_leaf.append(f1_train)
    val_acc_min_samples_leaf.append(acc_val)
    val_f1_min_samples_leaf.append(f1_val)

plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_min_samples_leaf,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_min_samples_leaf,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Minimum samples/leaf (max depth=20)")
plt.ylabel("Accuracy")
#plt.ylim(0.7,1.0)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size=[]
val_f1_train_size=[]
train_acc_train_size=[]
train_f1_train_size=[]
val_range=(10,101,5)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    percentage=i*0.01
    dtree = DecisionTreeClassifier(criterion='gini',max_depth=20,min_samples_leaf=5)
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled=df_sampled.drop('y',axis=1)
    y_train_sampled=df_sampled['y']
    # Fitting and Predictions
    dtree.fit(X_train_sampled,y_train_sampled)
    pred_train = dtree.predict(X_train_sampled)
    pred_val = dtree.predict(X_val)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train_sampled,pred_train)
    f1_train = f1_score(y_train_sampled,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    if i%10==0:
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_train_size,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_train_size,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75,1.0)
show()

# Boosting algorithm model

from sklearn.ensemble import AdaBoostClassifier

adaboost=AdaBoostClassifier(DecisionTreeClassifier(min_samples_leaf=2,max_depth=3),
                            n_estimators=20,learning_rate=0.01)

adaboost.fit(X_train,y_train)

# Predictions and evaluation

predictions = adaboost.predict(X_val)

score1=accuracy_score(y_val,predictions)
print(score1)

# 0.7422222222222222

# Varying number of estimators

val_acc_num_trees=[]
val_f1_num_trees=[]
train_acc_num_trees=[]
train_f1_num_trees=[]
time_adaboost=[]
val_range=(1,152,5)
for i in range(val_range[0],val_range[1],val_range[2]):
    t1=time.time()
    # Fitting
    adaboost = AdaBoostClassifier(DecisionTreeClassifier(min_samples_leaf=20,max_depth=2),
                            n_estimators=i,learning_rate=0.2)
    adaboost.fit(X_train,y_train)
    pred_train = adaboost.predict(X_train)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_num_trees.append(acc_train)
    train_f1_num_trees.append(f1_train)
    val_acc_num_trees.append(acc_val)
    val_f1_num_trees.append(f1_val)
    t2=time.time()
    time_adaboost.append(t2-t1)
    print(f"Done for number of trees: {i}")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_num_trees,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_num_trees,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Accuracy")
plt.ylim(0.5,1.05)
show()

plt.plot(range(val_range[0],val_range[1],val_range[2]),time_adaboost,c='red')
#plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_num_trees,c='blue')
#plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Model training time (seconds)")
#plt.ylim(0.7,1.05)
show()

# Tweaking the learning_rate of AdaBoostClassifier

val_acc_lr=[]
val_f1_lr=[]
train_acc_lr=[]
train_f1_lr=[]
val_range=(1,21,1)
lr_range=[]
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    lr=0.1*i
    lr_range.append(lr)
    adaboost = AdaBoostClassifier(DecisionTreeClassifier(min_samples_leaf=20,max_depth=2),
                            n_estimators=100,learning_rate=lr)
    adaboost.fit(X_train,y_train)
    pred_train = adaboost.predict(X_train)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_lr.append(acc_train)
    train_f1_lr.append(f1_train)
    val_acc_lr.append(acc_val)
    val_f1_lr.append(f1_val)
    print(f"Done for learning rate: {lr}")


plt.plot(lr_range,train_acc_lr,c='red')
plt.plot(lr_range,val_acc_lr,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Learning rate of AdaBoostClassifier")
plt.ylabel("Accuracy")
#plt.ylim(0.7,1.05)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size=[]
val_f1_train_size=[]
train_acc_train_size=[]
train_f1_train_size=[]
val_range=(10,101,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Model
    percentage=i*0.01
    adaboost = adaboost=AdaBoostClassifier(DecisionTreeClassifier(min_samples_leaf=20,max_depth=20),
                            n_estimators=20,learning_rate=0.5)
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled=df_sampled.drop('y',axis=1)
    y_train_sampled=df_sampled['y']
    # Fitting and prediction
    adaboost.fit(X_train_sampled,y_train_sampled)
    pred_train = adaboost.predict(X_train_sampled)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train_sampled,pred_train)
    f1_train = f1_score(y_train_sampled,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    
    if i%10==0:
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_train_size,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_train_size,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
#plt.ylim(0.75,1.0)
show()

# SVM model
# Scaling the data using StandardScaler

from sklearn.preprocessing import StandardScaler

X_train_scaled=StandardScaler().fit_transform(X_train)
X_val_scaled=StandardScaler().fit_transform(X_val)

from sklearn.svm import SVC

svc_clf=SVC(kernel="poly", C=1,degree=2)

svc_clf.fit(X_train_scaled,y_train)

# Predictions and evaluation

predictions=svc_clf.predict(X_val_scaled)

score1=accuracy_score(y_val,predictions)
print(score1)

# 0.9788888888888889

# Varying degree of polynomial kernel

val_acc_degree=[]
val_f1_degree=[]
train_acc_degree=[]
train_f1_degree=[]
val_range=(1,11,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    svc_clf=SVC(kernel="poly", C=0.01,degree=i)
    svc_clf.fit(X_train_scaled,y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"Done for number of degree: {i}")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_degree,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_degree,c='blue')
plt.grid(True)
plt.legend(["Training","Validation"])
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
#plt.ylim(0.8,0.9)
show()

# But what if we put a penalty for misclassification? C = 10

val_acc_degree=[]
val_f1_degree=[]
train_acc_degree=[]
train_f1_degree=[]
val_range=(1,11,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    svc_clf=SVC(kernel="poly", C=10,degree=i)
    svc_clf.fit(X_train_scaled,y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"Done for number of degree: {i}")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_degree,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_degree,c='blue')
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
#plt.ylim(0.8,0.9)
show()

# Varying regularization parameter C

val_acc_C=[]
val_f1_C=[]
train_acc_C=[]
train_f1_C=[]
C_range=[]
val_range=(-8,2,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    C=2**(i)
    C_range.append(C)
    # Fitting
    svc_clf=SVC(kernel="poly", C=C,degree=2)
    svc_clf.fit(X_train_scaled,y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_C.append(acc_train)
    train_f1_C.append(f1_train)
    val_acc_C.append(acc_val)
    val_f1_C.append(f1_val)
    print(f"Done for number of C: {2**(i)}")


plt.semilogx(C_range,train_acc_C,c='red')
plt.semilogx(C_range,val_acc_C,c='blue')
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Regularization/penalty parameter $C$")
plt.ylabel("Accuracy")
#plt.ylim(0.81,0.85)
show()

# Radial basis function (RBF) kernel - varying gamma

val_acc_gamma=[]
val_f1_gamma=[]
train_acc_gamma=[]
train_f1_gamma=[]
gamma_range=[]
val_range=(-25,10,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    gamma=10**(i/5.0)
    gamma_range.append(gamma)
    # Fitting9
    svc_clf=SVC(kernel="rbf", C=1,gamma=gamma)
    svc_clf.fit(X_train_scaled,y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_gamma.append(acc_train)
    train_f1_gamma.append(f1_train)
    val_acc_gamma.append(acc_val)
    val_f1_gamma.append(f1_val)
    print(f"Done for gamma: {gamma}")


plt.semilogx(gamma_range,train_acc_gamma,c='red')
plt.semilogx(gamma_range,val_acc_gamma,c='blue')
plt.grid(True)
plt.legend(["Training","Validation"])
plt.xticks()
plt.yticks()
plt.xlabel("Gamma of the SVM classifier RBF kernel")
plt.ylabel("Accuracy")
#plt.ylim(0.8,0.9)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size=[]
val_f1_train_size=[]
train_acc_train_size=[]
train_f1_train_size=[]
val_range=(10,101,5)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    percentage=i*0.01
    svc_clf=SVC(kernel="rbf",C=1,gamma=0.01)
    # Sampling (and scaling)
    df_sampled = df.sample(frac=percentage)
    X_train_sampled=df_sampled.drop('y',axis=1)
    y_train_sampled=df_sampled['y']
    X_train_sampled=StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    svc_clf.fit(X_train_sampled,y_train_sampled)
    pred_train = svc_clf.predict(X_train_sampled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train_sampled,pred_train)
    f1_train = f1_score(y_train_sampled,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    
    print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_train_size,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_train_size,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.9,1.0)
show()

# K-nearest neighbor model

from sklearn.neighbors import KNeighborsClassifier

knn=KNeighborsClassifier(3)

knn.fit(X_train_scaled,y_train)

predictions=knn.predict(X_val_scaled)

score1=accuracy_score(y_val,predictions)
print(score1)

#0.7255555555555555

#Varying number of neighbors

val_acc_k=[]
val_f1_k=[]
train_acc_k=[]
train_f1_k=[]
val_range=(1,21,1)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    knn=KNeighborsClassifier(i)
    knn.fit(X_train_scaled,y_train)
    pred_train = knn.predict(X_train_scaled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train,pred_train)
    f1_train = f1_score(y_train,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_k.append(acc_train)
    train_f1_k.append(f1_train)
    val_acc_k.append(acc_val)
    val_f1_k.append(f1_val)
    print(f"Done for number of neighbors: {i}")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_k,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_k,c='blue')
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neighbors ($K$)")
plt.ylabel("Accuracy")
plt.ylim(0.5,1.05)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size=[]
val_f1_train_size=[]
train_acc_train_size=[]
train_f1_train_size=[]
val_range=(10,101,5)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    percentage=i*0.01
    knn=KNeighborsClassifier(10)
   # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled=df_sampled.drop('y',axis=1)
    y_train_sampled=df_sampled['y']
    X_train_sampled=StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    knn.fit(X_train_sampled,y_train_sampled)
    pred_train = knn.predict(X_train_sampled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train=accuracy_score(y_train_sampled,pred_train)
    f1_train = f1_score(y_train_sampled,pred_train,average='micro')
    acc_val=accuracy_score(y_val,pred_val)
    f1_val = f1_score(y_val,pred_val,average='micro')
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    
    if i%10==0:
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_train_size,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_train_size,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
#plt.ylim(0.7,0.9)
plt.xlim(0,110)
show()

# Neural Networks (Multi-layer perceptron)

import keras
# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout

n_input=X_train_scaled.shape[0]
num_classes = len(y_train.unique())
input_dim=X_train_scaled.shape[1]

# Function to construct 2-hidden-layer Keras model

def make_NN_model(input_dim, num_classes, neuron_layer_1=20, neuron_layer_2=10, dropout_prob=0.25, \
                  activation_func='relu', learning_rate=0.01,optimizer='SGD'):
    """
    Creates a 2-hidden-layer Keras Neural Network model by adding densely connected layers, \
    dropout layers, and an output layer with 'softmax' activation with appropriate number of nodes for classification
    """
    model = Sequential()
    model.add(Dense(neuron_layer_1, input_shape=(input_dim,),activation=activation_func))
    model.add(Dropout(dropout_prob))
    model.add(Dense(neuron_layer_2,activation=activation_func))
    #model.add(Dense(50,activation='relu'))
    model.add(Dropout(dropout_prob))
    # Softmax activation for the last layer for classification
    model.add(Dense(1, activation='sigmoid'))
    
    if optimizer=='SGD':
        optimizer=keras.optimizers.SGD(lr=learning_rate)
    if optimizer=='Adam':
        optimizer=keras.optimizers.Adam(lr=learning_rate)
    if optimizer=='RMSprop':
        optimizer=keras.optimizers.RMSprop(lr=learning_rate)
    
    model.compile(loss='binary_crossentropy', optimizer=optimizer,metrics=['accuracy'])
    
    return model

# Function to run the NN model

def run_NN(model,X_train,y_train,X_val,y_val,num_epochs=200,batch_size=16,plot_loss=False,verbosity=0):
    #save best model as checkpointer
    from keras.callbacks import ModelCheckpoint
    checkpointer = ModelCheckpoint(filepath='model.weights.best.hdf5', 
                                   verbose=verbosity, save_best_only=True)
    
    # train the model
    hist = model.fit(X_train, y_train, batch_size=batch_size, epochs=num_epochs,
              validation_data=(X_val, y_val), 
              verbose=verbosity, shuffle=False)
    
    if plot_loss:
        plt.plot(hist.history['acc'],color='red')
        plt.plot(hist.history['val_acc'],color='blue')
        plt.title("Training and validation set accuracy")
        plt.grid(True)
        plt.xlabel("Epochs")
        plt.legend(['Training','Validation'])
        show()
    
    return hist

# Function to test the NN model

def test_NN(hist,X_test,y_test):
    """
    Test a NN model with test data set for accuracy
    hist: A History object generated by the Keras model fitting process
    """
    score=hist.model.evaluate(X_test, y_test,verbose=0)[1]
    return score

# Basic run of the neural network (using Adam optimizer)

nn_model=make_NN_model(input_dim=input_dim,num_classes=num_classes,dropout_prob=0.2,learning_rate=0.02,
                      neuron_layer_1=20,neuron_layer_2=10,optimizer='Adam')

hist=run_NN(nn_model,X_train_scaled,y_train,X_val_scaled,y_val,verbosity=1,batch_size=256,
            num_epochs=500,plot_loss=True)


# Basic run of the neural network (using Stochastic Gradient Descent optimizer)

nn_model=make_NN_model(input_dim=input_dim,num_classes=num_classes,dropout_prob=0.2,learning_rate=0.02,
                      neuron_layer_1=100,neuron_layer_2=50,optimizer='SGD')

hist=run_NN(nn_model,X_train_scaled,y_train,X_val_scaled,y_val,verbosity=1,batch_size=256,
            num_epochs=1000,plot_loss=True)


#Varying hyperparameters
#Number of neurons per layer

train_acc_n=[]
val_acc_n=[]

val_range=(10,200,10)
for i in range(val_range[0],val_range[1],val_range[2]):
    # Fitting
    nn_model=make_NN_model(input_dim=input_dim,num_classes=num_classes,dropout_prob=0.1,learning_rate=0.02,
                      neuron_layer_1=i,neuron_layer_2=i,optimizer='SGD')
    hist=run_NN(nn_model,X_train_scaled,y_train,X_val_scaled,y_val,verbosity=0,batch_size=256,
            num_epochs=100,plot_loss=False)
    # Accuracy score
    acc_train=hist.model.evaluate(X_train_scaled, y_train,verbose=0)[1]
    acc_val=hist.model.evaluate(X_val_scaled,y_val,verbose=0)[1]
   # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_n,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_n,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
#plt.ylim(0.0,0.9)
show()

# Learning rate

train_acc_lr=[]
val_acc_lr=[]

val_range=(-40,-10,1)
lr_range=[]
for i in range(val_range[0],val_range[1],val_range[2]):
    t1=time.time()
    lr=10**(i/10.0)
    lr_range.append(lr)
    # Fitting
    nn_model=make_NN_model(input_dim=input_dim,num_classes=num_classes,dropout_prob=0.1,learning_rate=lr,
                      neuron_layer_1=100,neuron_layer_2=100,optimizer='SGD')
    hist=run_NN(nn_model,X_train_scaled,y_train,X_val_scaled,y_val,verbosity=0,batch_size=256,
            num_epochs=100,plot_loss=False)
    # Accuracy score
    acc_train=hist.model.evaluate(X_train_scaled, y_train,verbose=0)[1]
    acc_val=hist.model.evaluate(X_val_scaled,y_val,verbose=0)[1]
   # Appending to the lists
    train_acc_lr.append(acc_train)
    val_acc_lr.append(acc_val)
    t2=time.time()
    print(f"Done for learning rate: {lr}. Time took {round((t2-t1),2)} seconds")

plt.plot(lr_range,train_acc_lr,c='red')
plt.plot(lr_range,val_acc_lr,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Learning rate")
plt.ylabel("Accuracy")
plt.ylim(0.0,0.9)
show()

# How to improve neural network performance?

model = Sequential()
model.add(Dense(100, input_shape=(input_dim,),activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(100,activation='selu'))
model.add(Dropout(0.1))
model.add(Dense(50,activation='selu'))
model.add(Dropout(0.1))
# sigmoid activation for the last layer for classification
model.add(Dense(1, activation='sigmoid'))

#Optimizer
optimizer=keras.optimizers.Adam(lr=0.01)

model.compile(loss='binary_crossentropy', optimizer=optimizer,metrics=['accuracy'])

model.summary()

hist=run_NN(model,X_train_scaled,y_train,X_val_scaled,y_val,verbosity=1,batch_size=256,
            num_epochs=100,plot_loss=True)

#LEARNING CURVE: Varying training set size

val_acc_train_size=[]
train_acc_train_size=[]

val_range=(10,101,5)
for i in range(val_range[0],val_range[1],val_range[2]):
    t1=time.time()
    percentage=i*0.01
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled=df_sampled.drop('y',axis=1)
    y_train_sampled=df_sampled['y']
    X_train_sampled=StandardScaler().fit_transform(X_train_sampled)
    # Fitting and Predictions
    nn_model=make_NN_model(input_dim=input_dim,num_classes=num_classes,dropout_prob=0.0,learning_rate=0.05,
                      neuron_layer_1=100,neuron_layer_2=100,optimizer='SGD')
    hist=run_NN(nn_model,X_train_sampled,y_train_sampled,X_val_scaled,y_val,verbosity=0,batch_size=256,
            num_epochs=100,plot_loss=False)
    # Accuracy score
    acc_train=hist.model.evaluate(X_train_sampled, y_train_sampled,verbose=0)[1]
    acc_val=hist.model.evaluate(X_val_scaled,y_val,verbose=0)[1]
   # Appending to the lists
    train_acc_train_size.append(acc_train)
    val_acc_train_size.append(acc_val)
    
    t2=time.time()
    print(f"Done for: {i}% training set size. Took {round((t2-t1),2)} seconds.")


plt.plot(range(val_range[0],val_range[1],val_range[2]),train_acc_train_size,c='red')
plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_train_size,c='blue')
plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
#plt.ylim(0.8,0.9)
plt.xlim(0,110)
show()

# At the end, comparison of performance (accuracy) on test set and wall time

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(criterion='gini',max_depth=20,min_samples_leaf=10)
dtree.fit(X_train,y_train)
predictions = dtree.predict(X_test)
score_dt=accuracy_score(y_test,predictions)
print(score_dt)

from sklearn.ensemble import AdaBoostClassifier
adaboost=AdaBoostClassifier(DecisionTreeClassifier(min_samples_leaf=20,max_depth=2),
                            n_estimators=80,learning_rate=0.5)
adaboost.fit(X_train,y_train)
predictions = adaboost.predict(X_test)
score_adaboost=accuracy_score(y_test,predictions)
print(score_adaboost)

X_train_scaled=StandardScaler().fit_transform(X_train)
X_test_scaled=StandardScaler().fit_transform(X_test)

from sklearn.svm import SVC
svc_clf=SVC(kernel="rbf", C=1,gamma=0.05)
svc_clf.fit(X_train_scaled,y_train)
predictions = svc_clf.predict(X_test_scaled)
score_SVC=accuracy_score(y_test,predictions)
print(score_SVC)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(5)
knn.fit(X_train_scaled,y_train)
predictions = knn.predict(X_test_scaled)
score_KNN=accuracy_score(y_test,predictions)
print(score_KNN)

accuracy_scores = [0.79, 0.93, 0.97, 0.69, 0.45]
timing = [0.23, 2.72, 2.27, 0.667, 3.5]

plt.figure(figsize=(15,5))
plt.title("Accuracy of the ML model")
plt.bar(x=['Decision Tree with pruning','AdaBoost','Support vector machine','k-nearest neighbor','Multi-layer perceptron'],
        height=accuracy_scores,width=0.5,color='red',edgecolor='k')
plt.xticks()
plt.yticks()
show()

plt.figure(figsize=(15,5))
plt.title("Wall time of running the ML model")
plt.bar(x=['Decision Tree with pruning','AdaBoost','Support vector machine','k-nearest neighbor','Multi-layer perceptron'],
        height=timing,width=0.5,color='blue',edgecolor='k')
plt.xticks()
plt.yticks()
show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Complexity and learning curve analysis for classification

sns.set_style("white")

df = pd.read_csv("Datasets/loan_data.csv")

# Look at first 5 rows
# df.head()

# Basic descriptive statistics

# df.describe()

# One-hot encoding of categorical features

df_final = pd.get_dummies(df, ["purpose"], drop_first=True)
df_final = df_final.drop("credit.policy", axis=1)

# df_final.shape
# (9578, 18)

# Basic visualizations

i = 1
plt.figure(figsize=(20, 20))
for c in df.describe().columns[:-1]:
    plt.subplot(4, 3, i)
    plt.title(f"Histogram of {c}")
    plt.yticks()
    plt.xticks()
    plt.hist(df[c], bins=20, color="orange", edgecolor="k")
    i += 1
show()

""" plot NG
i=1
plt.figure(figsize=(20,33))
for c in df_final.columns[:-1]:
    plt.subplot(6,3,i)
    plt.title(f"Boxplot of {c}")
    plt.yticks()
    plt.xticks()
    sns.boxplot(y=df_final[c],x=df_final['not.fully.paid'])
    i+=1
show()
"""

""" plot NG
sns.set(style="ticks", color_codes=True)
g=sns.pairplot(df_final,vars=["log.annual.inc","dti","fico","revol.bal"],
               plot_kws=dict(s=30, edgecolor="b", linewidth=1),
               hue="not.fully.paid",markers=["o", "s"],
               diag_kind="kde",diag_kws=dict(shade=True))
"""

# Test/train/validation split

X = df_final.drop("not.fully.paid", axis=1)
y = df["not.fully.paid"]

# First divide train and test data in 70:30 ratio

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# X_train.head(10)

# y.head()

# Then further divide the test set in 50:50 ratio into validation set and test set

X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.50)

# X_test.head()

# X_val.head()

# Show the shape of these sets

print("Shape of validation set:", X_val.shape)
print("Shape of test set:", X_test.shape)
print("Shape of training set:", X_train.shape)

# Decision Tree model

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(criterion="gini", max_depth=10, min_samples_leaf=5)

dtree.fit(X_train, y_train)

# Predictions and evaluation

predictions = dtree.predict(X_val)

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8058455114822547

# Varying hyperparameters: Pruning the tree

# Varying max_depth

val_acc_max_depth = []
val_f1_max_depth = []
train_acc_max_depth = []
train_f1_max_depth = []
for i in range(3, 21):
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=i, min_samples_leaf=1)
    dtree.fit(X_train, y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    train_acc_max_depth.append(acc_train)
    train_f1_max_depth.append(f1_train)
    val_acc_max_depth.append(acc_val)
    val_f1_max_depth.append(f1_val)

plt.plot(range(3, 21), train_acc_max_depth, c="red")
plt.plot(range(3, 21), val_acc_max_depth, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Max depth of the decision tree")
plt.ylabel("Accuracy")
plt.ylim(0.7, 1.0)
show()

# Varying min_samples_leaf with max_depth = 20

val_acc_min_samples_leaf = []
val_f1_min_samples_leaf = []
train_acc_min_samples_leaf = []
train_f1_min_samples_leaf = []
for i in range(1, 41):
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=i)
    dtree.fit(X_train, y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    train_acc_min_samples_leaf.append(acc_train)
    train_f1_min_samples_leaf.append(f1_train)
    val_acc_min_samples_leaf.append(acc_val)
    val_f1_min_samples_leaf.append(f1_val)

plt.plot(range(1, 41), train_acc_min_samples_leaf, c="red")
plt.plot(range(1, 41), val_acc_min_samples_leaf, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Minimum samples/leaf (max depth=20)")
plt.ylabel("Accuracy")
plt.ylim(0.7, 1.0)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []
val_range = (10, 101, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    percentage = i * 0.01
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=20)
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    # Fitting and Predictions
    dtree.fit(X_train_sampled, y_train_sampled)
    pred_train = dtree.predict(X_train_sampled)
    pred_val = dtree.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    if i % 10 == 0:
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75, 1.0)
show()

# Boosting algorithm model

from sklearn.ensemble import AdaBoostClassifier

adaboost = AdaBoostClassifier(
    DecisionTreeClassifier(min_samples_leaf=2), n_estimators=20, learning_rate=0.01
)

adaboost.fit(X_train, y_train)

# Predictions and evaluation

predictions = adaboost.predict(X_val)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8322894919972165

# Varying number of estimators

val_acc_num_trees = []
val_f1_num_trees = []
train_acc_num_trees = []
train_f1_num_trees = []
val_range = (1, 53, 3)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=20),
        n_estimators=i,
        learning_rate=0.2,
    )
    adaboost.fit(X_train, y_train)
    pred_train = adaboost.predict(X_train)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_num_trees.append(acc_train)
    train_f1_num_trees.append(f1_train)
    val_acc_num_trees.append(acc_val)
    val_f1_num_trees.append(f1_val)
    print(f"Done for number of trees: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_num_trees, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_num_trees, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Accuracy")
plt.ylim(0.7, 1.05)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []
val_range = (10, 101, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Model
    percentage = i * 0.01
    adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=20),
        n_estimators=20,
        learning_rate=0.2,
    )
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    # Fitting and prediction
    adaboost.fit(X_train_sampled, y_train_sampled)
    pred_train = adaboost.predict(X_train_sampled)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    if i % 10 == 0:
        print(f"Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75, 1.05)
show()

# SVM model

# Scaling the data using StandardScaler

from sklearn.preprocessing import StandardScaler

X_train_scaled = StandardScaler().fit_transform(X_train)
X_val_scaled = StandardScaler().fit_transform(X_val)

from sklearn.svm import SVC

svc_clf = SVC(kernel="poly", C=1, degree=2)

svc_clf.fit(X_train_scaled, y_train)

# Predictions and evaluation

predictions = svc_clf.predict(X_val_scaled)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8350730688935282

# Varying degree of polynomial kernel

val_acc_degree = []
val_f1_degree = []
train_acc_degree = []
train_f1_degree = []
val_range = (1, 11, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    svc_clf = SVC(kernel="poly", C=0.01, degree=i)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"Done for number of degree: {i}")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_degree, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_degree, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
plt.ylim(0.8, 0.9)
show()

# But what if we put a penalty for misclassification? C = 10

val_acc_degree = []
val_f1_degree = []
train_acc_degree = []
train_f1_degree = []
val_range = (1, 11, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    svc_clf = SVC(kernel="poly", C=1, degree=i)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"Done for number of degree: {i}")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_degree, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_degree, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# Varying regularization parameter C (i.e. in the Lagrangian formulation of SVM)

val_acc_C = []
val_f1_C = []
train_acc_C = []
train_f1_C = []
C_range = []
val_range = (-8, 2, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    C = 2 ** (i)
    C_range.append(C)
    # Fitting
    svc_clf = SVC(kernel="poly", C=C, degree=2)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_C.append(acc_train)
    train_f1_C.append(f1_train)
    val_acc_C.append(acc_val)
    val_f1_C.append(f1_val)
    print(f"Done for number of C: {2**(i)}")


plt.plot(C_range, train_acc_C, c="red")
plt.plot(C_range, val_acc_C, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Regularization/penalty parameter $C$")
plt.ylabel("Accuracy")
# plt.ylim(0.81,0.85)
show()

# Radial basis function (RBF) kernel - varying gamma

val_acc_gamma = []
val_f1_gamma = []
train_acc_gamma = []
train_f1_gamma = []
gamma_range = []
val_range = (-5, 2, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    gamma = 10 ** (i)
    gamma_range.append(gamma)
    # Fitting
    svc_clf = SVC(kernel="rbf", C=10, gamma=gamma)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_gamma.append(acc_train)
    train_f1_gamma.append(f1_train)
    val_acc_gamma.append(acc_val)
    val_f1_gamma.append(f1_val)
    print(f"Done for gamma: {gamma}")


plt.semilogx(gamma_range, train_acc_gamma, c="red")
plt.semilogx(gamma_range, val_acc_gamma, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Gamma of the SVM classifier RBF kernel")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []
val_range = (10, 101, 5)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    percentage = i * 0.01
    svc_clf = SVC(kernel="poly", C=0.001, degree=2)
    # Sampling (and scaling)
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    svc_clf.fit(X_train_sampled, y_train_sampled)
    pred_train = svc_clf.predict(X_train_sampled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.82, 0.86)
show()

# K-nearest neighbor model

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(3)

knn.fit(X_train_scaled, y_train)

predictions = knn.predict(X_val_scaled)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8058455114822547

# Varying number of neighbors

val_acc_k = []
val_f1_k = []
train_acc_k = []
train_f1_k = []
val_range = (1, 21, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    knn = KNeighborsClassifier(i)
    knn.fit(X_train_scaled, y_train)
    pred_train = knn.predict(X_train_scaled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_k.append(acc_train)
    train_f1_k.append(f1_train)
    val_acc_k.append(acc_val)
    val_f1_k.append(f1_val)
    print(f"Done for number of neighbors: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_k, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_k, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neighbors ($K$)")
plt.ylabel("Accuracy")
# plt.ylim(0.81,0.85)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []
val_range = (10, 101, 5)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    percentage = i * 0.01
    knn = KNeighborsClassifier(5)
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    knn.fit(X_train_sampled, y_train_sampled)
    pred_train = knn.predict(X_train_sampled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    if i % 10 == 0:
        print(f"Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.7, 0.9)
plt.xlim(0, 110)
show()

# Neural Networks (Multi-layer perceptron)

import keras

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout

n_input = X_train_scaled.shape[0]
num_classes = len(y_train.unique())
input_dim = X_train_scaled.shape[1]

# Function to construct 2-hidden-layer Keras model


def make_NN_model(
    input_dim,
    num_classes,
    neuron_layer_1=20,
    neuron_layer_2=10,
    dropout_prob=0.25,
    activation_func="relu",
    learning_rate=0.01,
    optimizer="SGD",
):
    """
    Creates a 2-hidden-layer Keras Neural Network model by adding densely connected layers, \
    dropout layers, and an output layer with 'softmax' activation with appropriate number of nodes for classification
    """
    model = Sequential()
    model.add(
        Dense(neuron_layer_1, input_shape=(input_dim,), activation=activation_func)
    )
    model.add(Dropout(dropout_prob))
    model.add(Dense(neuron_layer_2, activation=activation_func))
    # model.add(Dense(50,activation='relu'))
    model.add(Dropout(dropout_prob))
    # Softmax activation for the last layer for classification
    model.add(Dense(1, activation="sigmoid"))

    if optimizer == "SGD":
        optimizer = keras.optimizers.SGD(lr=learning_rate)
    if optimizer == "Adam":
        optimizer = keras.optimizers.Adam(lr=learning_rate)
    if optimizer == "RMSprop":
        optimizer = keras.optimizers.RMSprop(lr=learning_rate)

    model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])

    return model


# Function to run the NN model


def run_NN(
    model,
    X_train,
    y_train,
    X_val,
    y_val,
    num_epochs=200,
    batch_size=16,
    plot_loss=False,
    verbosity=0,
):
    # save best model as checkpointer
    from keras.callbacks import ModelCheckpoint

    checkpointer = ModelCheckpoint(
        filepath="model.weights.best.hdf5", verbose=verbosity, save_best_only=True
    )

    # train the model
    hist = model.fit(
        X_train,
        y_train,
        batch_size=batch_size,
        epochs=num_epochs,
        validation_data=(X_val, y_val),
        verbose=verbosity,
        shuffle=False,
    )

    if plot_loss:
        plt.plot(hist.history["acc"], color="red")
        plt.plot(hist.history["val_acc"], color="blue")
        plt.title("Training and validation set accuracy")
        plt.grid(True)
        plt.xlabel("Epochs")
        plt.legend(["Training", "Validation"])
        show()

    return hist


# Function to test the NN model


def test_NN(hist, X_test, y_test):
    """
    Test a NN model with test data set for accuracy
    hist: A History object generated by the Keras model fitting process
    """
    score = hist.model.evaluate(X_test, y_test, verbose=0)[1]
    return score


# Basic run of the neural network (using Adam optimizer)

nn_model = make_NN_model(
    input_dim=input_dim,
    num_classes=num_classes,
    dropout_prob=0.0,
    learning_rate=0.0001,
    neuron_layer_1=10,
    neuron_layer_2=5,
    optimizer="Adam",
)

hist = run_NN(
    nn_model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=64,
    num_epochs=25,
    plot_loss=True,
)


# Basic run of the neural network (using Stochastic Gradient Descent optimizer)

nn_model = make_NN_model(
    input_dim=input_dim,
    num_classes=num_classes,
    dropout_prob=0.0,
    learning_rate=0.0001,
    neuron_layer_1=10,
    neuron_layer_2=5,
    optimizer="SGD",
)

hist = run_NN(
    nn_model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=64,
    num_epochs=25,
    plot_loss=True,
)


# Varying hyperparameter - number of neurons per layer? How many epochs should we run for?

# Running for num_epochs = 5

train_acc_n = []
val_acc_n = []

val_range = (2, 21, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=5,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# Running for num_epochs = 10

train_acc_n = []
val_acc_n = []

val_range = (2, 21, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=10,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# Running for num_epochs = 25

train_acc_n = []
val_acc_n = []

val_range = (2, 21, 1)
for i in range(val_range[0], val_range[1], val_range[2]):
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=25,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
train_acc_train_size = []

val_range = (10, 101, 5)
for i in range(val_range[0], val_range[1], val_range[2]):
    percentage = i * 0.01
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and Predictions
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=5,
        neuron_layer_2=5,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_sampled,
        y_train_sampled,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=25,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_sampled, y_train_sampled, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    val_acc_train_size.append(acc_val)

    print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
plt.xlim(0, 110)
show()

# To smooth out the dependence on training set size, can we tweak the learning rate?

val_acc_train_size = []
train_acc_train_size = []

val_range = (10, 101, 5)
for i in range(val_range[0], val_range[1], val_range[2]):
    percentage = i * 0.01
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and Predictions
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.001,
        neuron_layer_1=5,
        neuron_layer_2=5,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_sampled,
        y_train_sampled,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=25,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_sampled, y_train_sampled, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    val_acc_train_size.append(acc_val)

    print(f"Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed (lr=0.001)")
plt.ylabel("Accuracy")
plt.ylim(0.5, 0.9)
plt.xlim(0, 110)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
