"""
PythonMachineLearning20_新進測試

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree

import warnings

warnings.filterwarnings("ignore")


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# OLS 迴歸

import statsmodels.api as sm  # 回歸模型套件

df0 = pd.read_csv("data/TaipeiAllBus0105.csv")  # 輸入資料
print(df0)


df0_X = df0.drop("volumn", axis=1)  # 將作為y的變數volunm刪去，並另存為x
df0_X1 = df0_X.drop(
    "transfer01", axis=1
)  # 之後要做相關係數，而因為transfer01變數為虛擬變數，故不須納入做相關係數，故刪除

df0_y = df0[["volumn"]]  # 製作變數y

# 4. 相關係數檢驗。

rDf0 = df0_X1.corr()  # 查看數據間的相關係數
print(rDf0)

sns.set(font_scale=1.5)

sns.set_context({"figure.figsize": (8, 8)})
sns.heatmap(data=rDf0, square=True, cmap="RdBu_r", annot=True)

show()

sns.pairplot(
    df0,
    x_vars=["People", "MRTpax", "shift", "kilometer"],
    y_vars="volumn",
    size=7,
    aspect=0.8,
    kind="reg",
)
show()

df0_X = sm.add_constant(df0_X)  # 增加模型的常數，使更為符合回歸模型

model0 = sm.OLS(df0_y, df0_X)  # OLS回歸
results0 = model0.fit()

print(results0.summary())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀寫XML文件")

from xml.dom import minidom

dom = minidom.Document()
root_node = dom.createElement("root")  # 創建根節點
dom.appendChild(root_node)  # 添加根節點

book_node = dom.createElement("blog")  # 創建第一個子節點
book_node.setAttribute("level", "3")  # 添加屬性
root_node.appendChild(book_node)  # 爲root添加子節點

name_node = dom.createElement("addr")  # 創建第二個子節點
name_text = dom.createTextNode("https://blog.csdn.net/xieyan0811")  # 添加文字
name_node.appendChild(name_text)
root_node.appendChild(name_node)

# toxml() 轉換成字符串, toprettyxml()轉換成樹形縮進版式
print(dom.toprettyxml())
with open("tmp_test_dom.xml", "w") as fh:
    dom.writexml(fh, indent="", addindent="\t", newl="\n", encoding="UTF-8")

print("------------------------------")  # 30個

from xml.dom import minidom

with open("tmp_test_dom.xml", "r") as fh:
    dom = minidom.parse(fh)  # 獲取dom對象
    root = dom.documentElement  # 獲取根節點
    print("node name", root.nodeName)  # 顯示節點名: root
    print("node type", root.nodeType)  # 顯示節點類型
    print("child nodes", root.childNodes)  # 列出所有子節點
    blog = root.getElementsByTagName("blog")[0]  # 根據標籤名獲取元素列表
    print(blog.getAttribute("level"))  # 獲取屬性值
    addr = root.getElementsByTagName("addr")[0]
    print("addr's child nodes", addr.childNodes)
    text_node = addr.childNodes[0]  # 獲取文本節點內容
    print("text data", text_node.data)
    print("parent", addr.parentNode.nodeName)  # 顯示name的父節點名稱

print("------------------------------------------------------------")  # 60個

print("抓取網站數據")
""" NG
import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen("https://blog.csdn.net/xieyan0811")
html = response.read().decode("utf-8","ignore") # 返回網頁爲utf-8編碼，解碼時忽略錯誤
reg = r'http://'  
soup = BeautifulSoup(html, 'html.parser')
for link in soup.find_all('a'):
    addr = link.get('href')
    # 顯示包含關鍵字的所有地址
    if addr != None and addr.find('xieyan0811/article') != -1: 
        print(addr)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("樸素貝葉斯")

import jieba


def load2():
    arr = [
        "不知道該說什麼, 這麼爛的抄襲片也能上映, 我感到很尷尬",
        "天吶。一個大寫的滑稽。",
        "劇情太狗血，演技太浮誇，結局太無語。總體太渣了。這一個半小時廢了。",
        "畫面很美，音樂很好聽，主角演的很到位，很值得一看的電影，男主角很帥很帥，贊贊贊",
        "超級喜歡的一部愛情影片",
        "故事情節吸引人，演員演的也很好，電影裏的歌也好聽，總之值得一看，看了之後也會很感動的。",
    ]
    ret = []
    for i in arr:
        words = jieba.cut(i)  # 將句子切分成詞
        ret.append(words)
    return ret, [0, 0, 0, 1, 1, 1]


def create_vocab(data):
    vocab_set = set([])  # 使用set集合操作去掉重複出現的詞彙
    for document in data:
        vocab_set = vocab_set | set(document)
    return list(vocab_set)


def words_to_vec(vocab_list, vocab_set):  # 將句轉換成詞表格式
    ret = np.zeros(len(vocab_list))  # 創建數據表中的一行，並置初值爲0（不存在）
    for word in vocab_set:
        if word in vocab_list:
            ret[vocab_list.index(word)] = 1  # 若該詞在本句中出現，則設置爲1
    return ret


def my_train(X, y):
    rows = X.shape[0]
    cols = X.shape[1]
    percent = sum(y) / float(rows)  # 正例佔比
    p0_arr = np.ones(cols)  # 設置初值爲1，後作爲分子
    p1_arr = np.ones(cols)
    p0_count = 2.0  # 設初值爲2，後作爲分母
    p1_count = 2.0
    for i in range(rows):  # 按每句遍歷
        if y[i] == 1:
            p1_arr += X[i]  # 數組按每個值相加
            p1_count += sum(X[i])  # 句子所有詞個數相加(只計詞彙表中詞)
        else:
            p0_arr += X[i]
            p0_count += sum(X[i])
    p1_vec = np.log(p1_arr / p1_count)  # 正例時，每個詞出現概率
    p0_vec = np.log(p0_arr / p0_count)
    return p0_vec, p1_vec, percent


def predict(X, p0_vec, p1_vec, percent):
    p1 = sum(X * p1_vec) + np.log(percent)  # 爲1的概率
    p0 = sum(X * p0_vec) + np.log(1.0 - percent)  # 爲0的概率
    if p1 > p0:
        return 1
    else:
        return 0


sentences, y = load2()
vocab_list = create_vocab(sentences)
X = []
for sentence in sentences:
    X.append(words_to_vec(vocab_list, sentence))
p0_vec, p1_vec, percent = my_train(np.array(X), np.array(y))
test = jieba.cut("抄襲得那麼明顯也是醉了！")
print(test)
test_X = np.array(words_to_vec(vocab_list, test))
print(test_X)
print(test, "分類", predict(test_X, p0_vec, p1_vec, percent))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Hyperopt")

# pip install hyperopt
from hyperopt import fmin, tpe, hp, Trials

trials = Trials()
best = fmin(
    fn=lambda x: (x - 1) ** 2,  # 最小化目標，如誤差函數
    space=hp.uniform("x", -10, 10),  # 定義搜索空間, 名稱爲x，範圍-10~10
    algo=tpe.suggest,  # 指定搜索算法
    trials=trials,  # 保存每次迭代的具體信息
    max_evals=50,
)  # 評估次數

print("------")
print(best)  # 返回結果：{'x': 0.980859461591201}
print("------")
print(len(trials.trials))
print(trials.trials)
print("------")
for t in trials.trials:
    print(t["result"])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" some fail
df = pd.read_csv('data/weibo_train_data.txt',sep='\t',header=None)
df = df.rename(columns={0:'uid',1:'m',2:'datetime',3:'f',4:'c',5:'l'})
print(df.shape)

print(df[5:10])
df[6:10].to_csv('weibo.csv',index=False, encoding='gbk',header=None)

print('------------------------------------------------------------')	#60個

counts = df[3].value_counts()
print(type(counts))
plt.plot(counts)

show()

df[3].value_counts()
print(len(df[df[3] == 0])/len(df))
print(len(df[df[3] < 50])/len(df))


grp = df.groupby(0)
print(len(grp))

df['feed_back'] = df[3]+df[4]+df[5]


counts = grp['feed_back'].count()
#plt.hist(counts, 200)

means = grp['feed_back'].mean()
count = 0
for i in means:
    print(i)
    if i == 0:
        count += 1
print(count)


means[means>500]
#print(df[df[0]=='6a989f414896b3ecec9ec9571d2489c5'])

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

"""
手動下載
https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels.h5
https://storage.googleapis.com/tensorflow/keras-applications/resnet/resnet50_weights_tf_dim_ordering_tf_kernels_notop.h5
https://storage.googleapis.com/tensorflow/keras-applications/inception_v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
https://storage.googleapis.com/tensorflow/keras-applications/xception/xception_weights_tf_dim_ordering_tf_kernels_notop.h5
放在
~/.keras/models/
或
C:/Users/070601/.keras/models/
之下
"""

# from keras.applications.resnet50 import ResNet50
from tensorflow.keras.applications.resnet50 import ResNet50

# from keras.preprocessing import image
# from keras.utils import image_utils

# from keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

model = ResNet50(weights="imagenet")

print("檢視模型架構")
model.summary()  # 檢視模型架構

img_path = "elephant.jpg"
# img = image.load_img(img_path, target_size=(224, 224))
img = tf.keras.utils.load_img(img_path, target_size=(224, 224))
# x = image.img_to_array(img)
x = tf.keras.utils.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

preds = model.predict(x)
print("Predicted:", decode_predictions(preds, top=3)[0])

print("------------------------------------------------------------")  # 60個

"""
使用keras下載訓練好的模型（下載每個模型幾十分鐘）, 並用模型對提取圖片的特徵。
訓練集25000張圖式片， 測試集12500張圖片，用三個模型, 如果不使用GPU，約8小時以上。
本例中只使用了幾百張圖片, 花十幾分鍾跑一遍整體流程。 想訓練所有， 只需增加圖片數據即可。
"""

from keras.models import *
from keras.layers import *
from keras.applications import *
from keras.preprocessing.image import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 資料擴增
import h5py


def get_features(MODEL, width, height, lambda_func=None):
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights="imagenet", include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()

    # 注意 train 和 test 是圖片存儲路徑
    train_generator = gen.flow_from_directory(
        "train", (width, height), shuffle=False, batch_size=16
    )
    test_generator = gen.flow_from_directory(
        "test", (width, height), shuffle=False, batch_size=16, class_mode=None
    )
    # 不同的keras版本變量名略有不同，如: train_generator.samples train_generator.samples...
    train = model.predict_generator(train_generator, train_generator.samples)
    test = model.predict_generator(test_generator, test_generator.samples)

    """ some error
    with h5py.File("data_%s.h5"%MODEL.func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)
    """


""" some NG
get_features(ResNet50, 224, 224)
get_features(InceptionV3, 299, 299, inception_v3.preprocess_input)
get_features(Xception, 299, 299, xception.preprocess_input)
"""

print("------------------------------------------------------------")  # 60個

# 訓練模型並預測，此處使用了深度學習模型，也可以換成機器學習模型

import h5py
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *

np.random.seed(12345678)
X_train = []
X_test = []

"""
for filename in ["data_ResNet50.h5", "data_Xception.h5", "data_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)

print('------------------------------------------------------------')	#60個

# 用迭代訓練過程中的錯誤率做圖


def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.legend(["acc", "val_acc"], loc='best')
    plt.title('Training and validation accuracy')
    show()
    loss = history.history['loss']
    val_loss = history.history['val_loss']   
    plt.plot(epochs, loss, 'b')
    plt.plot(epochs, val_loss, 'r')
    plt.legend(["loss", "val_loss"], loc='best')
    plt.title('Training and validation loss')
    show()

plot_training(history)
"""
print("------------------------------------------------------------")  # 60個

# should be the same
print("提取特徵")

from keras.models import *
from keras.layers import *
from keras.applications import *
from keras.preprocessing.image import *
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 資料擴增
import h5py


def get_features(MODEL, width, height, lambda_func=None):
    input_tensor = Input((height, width, 3))
    x = input_tensor
    if lambda_func:
        x = Lambda(lambda_func)(x)

    base_model = MODEL(input_tensor=x, weights="imagenet", include_top=False)
    model = Model(base_model.input, GlobalAveragePooling2D()(base_model.output))

    gen = ImageDataGenerator()

    # 注意 train 和 test 是圖片存儲路徑
    train_generator = gen.flow_from_directory(
        "train", (width, height), shuffle=False, batch_size=16
    )
    test_generator = gen.flow_from_directory(
        "test", (width, height), shuffle=False, batch_size=16, class_mode=None
    )
    train = model.predict_generator(train_generator, train_generator.samples)
    test = model.predict_generator(test_generator, test_generator.samples)
    """ maybe the same
    with h5py.File("data_%s.h5"%MODEL.func_name) as h:
        h.create_dataset("train", data=train)
        h.create_dataset("test", data=test)
        h.create_dataset("label", data=train_generator.classes)
    """


""" some NG
get_features(ResNet50, 224, 224)
get_features(InceptionV3, 299, 299, inception_v3.preprocess_input)
get_features(Xception, 299, 299, xception.preprocess_input)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("訓練模型和預測")
""" NG
import h5py
from sklearn.utils import shuffle
from keras.models import *
from keras.layers import *

np.random.seed(12345678)
X_train = []
X_test = []

for filename in ["data_ResNet50.h5", "data_Xception.h5", "data_InceptionV3.h5"]:
    with h5py.File(filename, 'r') as h:
        X_train.append(np.array(h['train']))
        X_test.append(np.array(h['test']))
        y_train = np.array(h['label'])

X_train = np.concatenate(X_train, axis=1)
X_test = np.concatenate(X_test, axis=1)
X_train, y_train = shuffle(X_train, y_train)

input_tensor = Input(X_train.shape[1:])
x = Dropout(0.5)(input_tensor)
x = Dense(1, activation='sigmoid')(x)
model = Model(input_tensor, x)

model.compile(optimizer='adadelta',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=128, nb_epoch=8, validation_split=0.2)
y_pred = model.predict(X_test, verbose=1)
y_pred = y_pred.clip(min=0.005, max=0.995)

print('------------------------------')	#30個

#訓練結果分析


def plot_training(history):
    acc = history.history['acc']
    val_acc = history.history['val_acc']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'b')
    plt.plot(epochs, val_acc, 'r')
    plt.legend(["acc", "val_acc"], loc='best')
    plt.title('Training and validation accuracy')
    show()
    
loss = history.history['loss']
val_loss = history.history['val_loss']   
plt.plot(epochs, loss, 'b')
plt.plot(epochs, val_loss, 'r')
plt.legend(["loss", "val_loss"], loc='best')
plt.title('Training and validation loss')
show()

plot_training(history)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
