Regression

    Simple linear regression with t-statistic generation
    Linear regression as a statistical estimation problem
    Multiple ways to perform linear regression in Python and their speed comparison. Also check the article I wrote on freeCodeCamp
    Multi-variate regression with regularization
    Polynomial regression using scikit-learn pipeline feature. Also check the article I wrote on Towards Data Science.
    Decision trees and Random Forest regression (showing how the Random Forest works as a robust/regularized meta-estimator rejecting overfitting).
    Detailed visual analytics and goodness-of-fit diagnostic tests for a linear regression problem.

Classification

    Logistic regression/classification.
    k-nearest neighbor classification.
    Decision trees and Random Forest Classification.
    Support vector machine classification. Also check the article I wrote in Towards Data Science on SVM and sorting algorithm.
    Naive Bayes classification.
    Classification using Stochastic Gradient Descent (SGD).

Clustering

    K-means clustering.
    Affinity propagation (showing its time complexity and the effect of damping factor).
    Mean-shift technique (showing its time complexity and the effect of noise on cluster discovery).
    DBSCAN (showing how it can generically detect areas of high density irrespective of cluster shapes, which the k-means fails to do).
    Hierarchical clustering with Dendograms showing how to choose optimal number of clusters.
    Clustering metrics better than the elbow-method.

Dimensionality reduction

    Principal component analysis
    Clustering combined with dimensionality reduction technqieus

recurrent neural network (RNN)




資料		資料分割	資料取得、資料清理、資料分割

模型訓練	模型訓練	模型訓練、讀取模型

預測		預測		預測、儲存模型、模型評估、資料輸出、資料畫圖

資料來源
1. 標準資料範本：iris、titanic、wine、cancer、糖、、
2. sklearn合成資料：、、、
3. 抓網路資料分析：、、、
4. 自己建立資料



ML四大部分
regression			SVR、Ridge、Lasso、SGD、、、
classification			SVC、KNN、SGD、NaiveBayes、、、
clustering			KMeans、MeanShift、GMM、、、
dimensionality-reduction	PCA、、、



Python Machine Learning

regression, classification, clustering, dimensionality reduction, 

and some basic neural network algorithms

Regression
    Simple linear regression with t-statistic generation
    Multiple ways to do linear regression in Python and their speed comparison (check the article I wrote on freeCodeCamp)
    Multi-variate regression with regularization
    Polynomial regression with how to use scikit-learn pipeline feature (check the article I wrote on Towards Data Science)
    Decision trees and Random Forest regression (showing how the Random Forest works as a robust/regularized meta-estimator rejecting overfitting)

Classification
    Logistic regression/classification
    k-nearest neighbor classification
    Decision trees and Random Forest Classification
    Support vector machine classification
    Naive Bayes classification

Clustering
    K-means clustering
    Affinity propagation (showing its time complexity and the effect of damping factor)
    Mean-shift technique (showing its time complexity and the effect of noise on cluster discovery)
    Hierarchical clustering with Dendograms showing how to choose optimal number of clusters
    DBSCAN (showing how it can generically detect areas of high density irrespective of cluster shapes, which the k-means fails to do)

Dimensionality reduction
    Principal component analysis(PCA)

Deep Learning/Neural Network

    Demo notebook to illustrate the superiority of deep neural network for complex nonlinear function approximation task.
    Step-by-step building of 1-hidden-layer and 2-hidden-layer dense network using basic TensorFlow methods




Sepal花萼
Petal花瓣

SL   SW   PL   PW   y
萼長 萼寬 瓣長 瓣寬 類別

# 取前四欄位當作訓練資料

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
         Id,SepalLengthCm,   SepalWidthCm,   PetalLengthCm,   PetalWidthCm,Species

from sklearn.model_selecting import train_test_spilt()
参数stratify： 依据标签y，按原数据y中各类比例，分配给train和test，使得train和test中各类数据的比例与原数据集一样。
A:B:C=1:2:3
split后，train和test中，都是A:B:C=1:2:3
将stratify=X就是按照X中的比例分配
将stratify=y就是按照y中的比例分配
一般都是=y


stratify是为了保持split前类的分布：
比如有100个数据，80个属于A类，20个属于B类。如果train_test_split(… test_size=0.25, stratify = y_all), 那么split之后数据如下：
training: 75个数据，其中60个属于A类，15个属于B类。
testing: 25个数据，其中20个属于A类，5个属于B类。

用了stratify参数，training集和testing集的类的比例是 A：B= 4：1，等同于split前的比例（80：20）。通常在这种类分布不平衡的情况下会用到stratify。
将stratify=X就是按照X中的比例分配
将stratify=y就是按照y中的比例分配



【分類分析(Classification)】是分析者做出人為主觀的分類(人主動決定結果)
【群集分析(Clustering)】是演算法做出系統客觀的分類(人被動接受結果)





t-分佈隨機鄰居嵌入 t-distributed Stochastic Neighbor Embedding, t-SNE	降維演算法

監督式學習 : 線性迴歸、邏輯斯迴歸、支援向量機、神經網路、決策樹、K近鄰法、、

非監督式學習 : 分群、降維

K折交叉驗證 K-fold Cross Validation

自助聚合法 Bootstrap Aggregation => bagging

提升法 Boosting(2)
1. 適應提升法 adaptive boosting (AdaBoost)
2. 梯度提升法 gradient boosting XGBoost


機器學習 SVM

機器學習其實基本上和我們一直以來說的一樣, 就是我們要學一個未知的函數
f(x)=y

如果是分類, 基本上就是有一筆資料 x=(x1,x2,…,xk), 我們想知道這
f(x)=y

其中的 y 就是某一個類別。

這種學函數的方法, 又可以分為:

1. supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。
2. unsupervised learning 我們不知道答案, 卻要電腦自己去學!

最基本的方式, 一個是 SVM, 一個是 K-Means。
# Supervised Learning SVM

徑向基函數核
在機器學習中，（高斯）徑向基函數核（英語：Radial basis function kernel），或稱為RBF核，是一種常用的核函數。它是支持向量機分類中最為常用的核函數


# 接著進入 AI 建模三部曲。

# step 1. 開一台「函數學習機」
# step 2. fit 學習、訓練
# step 3. predict 預測


常見的人工智慧的技術(4)
1.機器學習 Machine Learning
2.自然語言處理 Natural Language Processing, NLP
3.影像處理 Image Processing 圖像分類、圖像分割、物體識別、圖像生成、圖像風格轉換
4.語言處理 Speech Processing 語音辨識Speech Recognition 語音合成 Speech Synthesis


機器學習 Machine Learning
1. 監督式學習 supervised learning
	分類學習 classification learning / 回歸學習 regression learning
	傳統監督式學習模型(6)
	1. 線性迴歸 linear regression
	2. 邏輯迴歸 logistic regression
	3. 決策樹 decision tree
	4. 隨機森林 random forest
	5. 支持向量機 support vector machines, SVM
	6. 單純貝氏分類器 naive Bayes classifier
2. 非監督式學習 unsupervised learning
	1. 分群 clustering
	2. 分布密度估計 density estimation
	3. 維度約簡 dimensionality reduction
3. 半監督式學習 semi-supervised learning
4. 強化學習 reinforcement learning

print("------------------------------------------------------------")	#60個

Machine Learning

Regression

    Simple linear regression with t-statistic generation
    Multiple ways to do linear regression in Python and their speed comparison (check the article I wrote on freeCodeCamp)
    Multi-variate regression with regularization
    Polynomial regression with how to use scikit-learn pipeline feature (check the article I wrote on Towards Data Science)
    Decision trees and Random Forest regression (showing how the Random Forest works as a robust/regularized meta-estimator rejecting overfitting)

Classification

    Logistic regression/classification
    k-nearest neighbor classification
    Decision trees and Random Forest Classification
    Support vector machine classification
    Naive Bayes classification

Clustering

    K-means clustering
    Affinity propagation (showing its time complexity and the effect of damping factor)
    Mean-shift technique (showing its time complexity and the effect of noise on cluster discovery)
    Hierarchical clustering with Dendograms showing how to choose optimal number of clusters
    DBSCAN (showing how it can generically detect areas of high density irrespective of cluster shapes, which the k-means fails to do)

Dimensionality reduction

    Principal component analysis

Deep Learning/Neural Network

print("------------------------------------------------------------")	#60個

深度學習的基本神經網路類型
1. 前饋神經網路 Feedforward Neural Network, FNN
2. 卷積神經網路 Convolutional Neural Network, CNN
3. 循環神經網路 Recurrent Neural Network, RNN

基於編碼器的神經網路 BERT
BERT :從 Transformer生成的雙向編碼器表示技術


基於解碼器的神經網路 GPT
Generative Pre-training Transformer

YOLO(You Only Look Once) 是一個即時物件偵測網路

生成網路
生成對抗網路 Generative Adversarial Networks, GANs
穩定擴散網路 Stable Diffusion

圖神經網路 Graph Neural Networks, GNN


Scikit-learn的基本功能主要被分為六大部分：
1. 分類（Classification），
2. 回歸（Regression），
3. 集群(聚類)（Clustering）
4. 數據降維（Dimensionality reduction）
5. 模型選擇（Model selection）
6. 數據前置處理（Preprocessing）。


PCA:主成分分析（Principal Component Analysis）, 降低數據維度
1. 載入資料
2. 資料清理/探索/分析
3. 進行特徵工程
4. 資料分割
5. 選擇演算法
6. 模型訓練
7. 模型評估
# 計算準確率
# 混淆矩陣
# 混淆矩陣圖
不進行特徵縮放
# 計算準確率
# 8. 模型評估，暫不進行
# 9. 模型佈署
# 模型存檔
# 10.模型預測

隨機森林(Random Forest)

隨機森林(Random Forest)是用隨機選取部分資料的方式 建立多棵決策數，
每一棵樹都會有自己的預測結果，之後再進行多數決，決定最後的預測結果。


各種演算法

迴歸類：
LinearRegression
SimpleLinearRegression
SMOreg

決策樹＋迴歸：
M5P

決策樹：
RandomTree
REPTree


ML包含
迴歸 regression
分類 classification
分群 clustering

梯度提升 Gradient Boosting

XGBoost 梯度提升法函式庫



線性迴歸（英語：linear regression）
是利用稱為線性迴歸方程式的最小平方函數對一個或多個自變數和應變數之間關係進行建模的一種迴歸分析。
這種函數是一個或多個稱為迴歸係數的模型參數的線性組合。
只有一個自變數的情況稱為簡單迴歸，
大於一個自變數情況的叫做多元迴歸（multivariable linear regression）。





    有监督学习
        数据预处理
        简单线性回归
        多元线性回归
        逻辑回归
        k近邻法(k-NN)
        支持向量机(SVM)
        决策树
        随机森林
    无监督学习
        K-均值聚类
        层次聚类


特徵資料（花萼長、寬等等）
標籤	屬種。







1. 數據
2. 分類
3. 函數學習機
4. 學習訓練.fit 學習訓練 模型訓練
5. 預測.predit預測 模型計分
計算準確率
6. 儲存預測模型/讀取預測模型並預測
7. 畫圖

# 8. 模型評估，暫不進行
# 9. 模型佈署，暫不進行


建立資料
整理資料
特徵工程
資料分割
特徵縮放
選擇演算法


機器學習的種類(3)
1. 監督學習(supervised learning)
	迴歸 regression
	分類 classification
	線性迴歸、邏輯斯迴歸、支援向量機、神經網路、決策樹、K近鄰法
2. 無監督學習(unsupervised learning)
	分群 clustering
	降維
	
	
3. 強化學習(reinforcement learning)


支持向量機 Support Vector Machine, SVM

主成分分析 Principal Components Analysis, PCA

線性迴歸
coef_ : 迴歸係數
intercept_ : 截距

make_regression 準備迴歸模型數據
make_blobs 準備群集數據

常見的監督學習分類器
1. KNN
2. 邏輯迴歸演算法
3. 決策樹 Decision Tree
4. 隨機森林 Random Forest


生成式演算法
1. 自助具合法 Bootstrap Aggregation => bagging
2. 提升法 Boosting
3. 隨機森林 Random Forest



print("------------------------------------------------------------")	#60個



print("------------------------------------------------------------")	#60個




print("------------------------------------------------------------")	#60個

lost
1. UCI波士頓的房價資料集 (https://archive.ics.uci.edu/ml/machine-learning-databases/housing/)
Home - UCI Machine Learning Repository
https://archive.ics.uci.edu/



print("------------------------------------------------------------")	#60個



print("------------------------------------------------------------")	#60個



print("------------------------------------------------------------")	#60個




print("------------------------------------------------------------")	#60個



print("------------------------------------------------------------")	#60個



