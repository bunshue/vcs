import sys

import pandas as pd

print('------------------------------------------------------------')	#60個

# SnowNLP用法

from snownlp import SnowNLP

s = SnowNLP("跟框架學代碼設計，跟應用學功能設計")
print(s.words) # 分詞
print(s.sentiments) # 消極or積極，結果在0-1之間
print(s.tags) # 詞性標註
print(s.keywords(3)) #　關鍵詞
print(s.summary(3)) # 摘要
print(s.tf) # tf
print(s.idf) # idf

print('------------------------------------------------------------')	#60個


# 引入頭文件
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings 
import re
import tools # 工具實現在tools.py文件中

warnings.filterwarnings("ignore")

# 讀訓練數據
data = pd.read_csv('data/weibo_train_data.txt',sep='\t',header=None)
data = tools.prepare(data)
data = tools.add_features(data)

# 切分訓練集和驗證集
train,val = train_test_split(data, test_size=0.2, random_state=0)
val = val.reset_index(drop=True)

# 按用戶分組
if True:
    grp = train.groupby('uid')
    user_data = pd.DataFrame()
    user_data['f'] = grp['f'].mean()
    user_data['c'] = grp['c'].mean()
    user_data['l'] = grp['l'].mean()
else:
    user_data = pd.read_csv("train_user.csv")
user_data_2 = user_data.rename(columns={'l':'avg_l','c':'avg_c','f':'avg_f'})
print(user_data.head())

print('------------------------------------------------------------')	#60個


# 模型訓練
import xgboost as xgb

def testme_f(preds,dtrain):
    labels=pd.Series(dtrain.get_label())
    tmp = pd.DataFrame()
    d = ((preds - labels)/(labels + 5.0)).apply(lambda x: abs(x))
    count_i = labels
    precision = 1 - d
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 50] = 50
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return 'testme', 1 - count_1/count_2

def testme_lc(preds,dtrain):
    labels=pd.Series(dtrain.get_label())
    tmp = pd.DataFrame()
    d = ((preds - labels)/(labels + 3.0)).apply(lambda x: abs(x))
    count_i = labels
    precision = 1 - d
    sign = np.sign(precision - 0.8).apply(lambda x: 0 if x == -1 else 1)
    count_i[count_i > 25] = 25
    count_1 = sum((count_i + 1) * sign)
    count_2 = sum(count_i + 1)
    return 'testme', 1 - count_1/count_2

def calc(grp1, grp2, features, key, params, feval):
    train_X = grp1[features]
    train_Y = grp1[key]
    val_X = grp2[features]
    val_Y = grp2[key]
    dtrain = xgb.DMatrix(train_X, train_Y)
    dval = xgb.DMatrix(val_X, val_Y)
    watchlist  = [(dtrain,'train'),(dval,'val')]
    model = xgb.train(params,dtrain, evals=watchlist, feval=feval, 
                      num_boost_round=200, early_stopping_rounds=10)
    model.save_model('model_'+key)
    dic = model.get_fscore()
    dic2= sorted(dic.items(), key=lambda d:d[1], reverse = True)
    print("feature importance", dic2)
    return model

params={
    'max_depth':7,
    'subsample':0.7,
    'eta': 0.05,
    'seed':5,
    'objective':'reg:linear'
}




print('------------------------------------------------------------')	#60個

# 提取關鍵詞
import jieba

# tmp=data.sample(n = 100000) # adjust
tmp = data.sample(n = 1000)
arr = tmp['content'].unique()
print(len(arr))
arr_all = []
for i in arr:
    arr = jieba.cut(i, cut_all=True)
    arr_zh = [i for i in arr if len(re.findall(r"^[#\+a-z0-9A-Z\\-_]+$",i,re.M)) == 0 and len(i) > 1]
    arr_all.extend(arr_zh)
print(len(arr_all))

result = pd.value_counts(arr_all)
arr_word = []
for key,value in result.items():
    if value > 5:
        arr_word.append(key)
print(arr_word)

print('------------------------------------------------------------')	#60個

# 從文字中提取特徵
from scipy import stats

def get_dic(arr_word, dst, count, data):
    print(len(arr_word))
    dic_key = {}
    for idx,i in enumerate(arr_word):
        df1 = data[data['content'].str.contains(i)==False]
        df2 = data[data['content'].str.contains(i)==True]
        ret2 = stats.levene(df1[dst], df2[dst])
        if ret2[1] < 0.05:
            dic_key[i] = [ret2[1], df2[dst].mean(), len(df2)]
            print(idx, i, dic_key[i], len(dic_key))
            if len(dic_key) > count:
                break
    return dic_key

dic_key_f = get_dic(arr_word, 'f', 100, data[:100000])
dic_key_c = get_dic(arr_word, 'c', 50, data[:100000])
dic_key_l = get_dic(arr_word, 'l', 100, data[:100000])

print('------------------------------------------------------------')	#60個

val = pd.merge(val, user_data_2, on='uid', how='left')
train = pd.merge(train, user_data_2, on='uid', how='left')

# 生成新模型
def calc_dic(train, val, dst, dic):
    train_new = train.copy()
    for key in dic.keys():
        #print(key)
        train_new[key] = train['content'].str.contains(key).apply(lambda x: 1 if x else 0)
    val_new = val.copy()
    for key in dic.keys():
        val_new[key] = val['content'].str.contains(key).apply(lambda x: 1 if x else 0)
    features = ['weekday', 'hour',
           'c_has_link', 'c_has_at', 'c_has_ex', 'c_has_video', 'c_has_ads',
           'c_has_share', 'c_has_it', 'avg_l', 'avg_c', 'avg_f', 'c_has_topic']
    features_new = features + list(dic.keys())
    model = calc(train_new, val_new, features_new, dst, params, testme_f)
    return model

model_f = calc_dic(train, val, 'f', dic_key_f)
model_c = calc_dic(train, val, 'c', dic_key_c)
model_l = calc_dic(train, val, 'l', dic_key_l)


print('------------------------------------------------------------')	#60個

# 保存模型
dic = {}
dic['model_f'] = model_f
dic['model_c'] = model_c
dic['model_l'] = model_l
dic['dic_key_f'] = dic_key_f
dic['dic_key_c'] = dic_key_c
dic['dic_key_l'] = dic_key_l
dic['user_data_2'] = user_data_2

""" import fail
from sklearn.externals import joblib
joblib.dump(dic, 'model.pkl')
"""

print('------------------------------------------------------------')	#60個

def do_pred(model, val, dic):
    val_new = val.copy()
    for key in dic.keys():
        val_new[key] = val['content'].str.contains(key).apply(lambda x: 1 if x else 0)
    features = ['weekday', 'hour',
           'c_has_link', 'c_has_at', 'c_has_ex', 'c_has_video', 'c_has_ads',
           'c_has_share', 'c_has_it', 'avg_l', 'avg_c', 'avg_f', 'c_has_topic']
    features_new = features + list(dic.keys())
    tmp = val_new[features_new]
    dtest = xgb.DMatrix(tmp)
    out = model.predict(dtest)
    out = pd.Series(out).apply(lambda x:int(x))
    return out

def do_pred_all(df):
    out = df.copy()
    out['f'] = do_pred(model_f, df, dic_key_f)
    out['l'] = do_pred(model_l, df, dic_key_l)
    out['c'] = do_pred(model_c, df, dic_key_c)
    return out

# 對驗證集預測
out = do_pred_all(val)
print(tools.do_score(val, out))

# 預測並生成提交數據
test = pd.read_csv('data/weibo_predict_data.txt',sep='\t',header=None)
test = tools.prepare(test)
test = tools.add_features(test)
test = pd.merge(test, user_data_2, on='uid', how='left')
test = test.fillna(0)
out = do_pred_all(test)
out['ss'] = out['f'].astype(str) + "," + out['c'].astype(str) + ',' + out['l'].astype(str)
out = out[['uid','mid','ss']]
print(out.shape)
print(out.head())
out.to_csv("result_190624.txt", index=False, header=None, sep='\t')

print('------------------------------------------------------------')	#60個


""" some fail
import pandas as pd

df = pd.read_csv('data/weibo_train_data.txt',sep='\t',header=None)
df = df.rename(columns={0:'uid',1:'m',2:'datetime',3:'f',4:'c',5:'l'})
print(df.shape)


print(df[5:10])
df[6:10].to_csv('weibo.csv',index=False, encoding='gbk',header=None)

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt

counts = df[3].value_counts()
print(type(counts))
plt.plot(counts)

plt.show()


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

print('------------------------------------------------------------')	#60個


