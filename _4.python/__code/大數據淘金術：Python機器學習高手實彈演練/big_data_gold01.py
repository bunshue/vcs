"""
pandas一大堆



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
'''
# 索引
df = pd.DataFrame({"a":[1,3], "b":[2,4]}, index=['line1', 'line2'])
print(df.index) # 顯示行索引
print(df.columns) # 顯示列索引

print('------------------------------------------------------------')	#60個

# 多重索引
df = pd.read_excel('data/test.xlsx', header=[0,1]) # 指定前兩行爲列索引
print(df)
print(df.columns.values) # 查看列索引內容

df.columns = ['_'.join(col).strip() for col in df.columns.values] # 重置字段名
print(df)

print('------------------------------------------------------------')	#60個

# Python日期時間處理
# 時間點

from datetime import datetime

d1 = datetime.now() # 獲取當前時間
print(d1)
print(d1.year, d1.month, d1.day, d1.hour, d1.minute, d1.second)
d2 = datetime(2019, 3, 27) # 通過指定日期構造datetime
print(d2)

# 時間段
from datetime import timedelta

delta = d2-d1 # 通過時間日期相減獲取
print(type(delta))
print(delta)
delta = timedelta(days=3) # 通過指定時定差獲取
print(d1+delta)# 利用時間段計算新日期時間

# 時間戳

import time
print(time.time())

d = datetime.now()
t = time.mktime(d.timetuple()) # 從datetime格式轉換
print(t)
print(time.mktime(time.strptime("2019-03-27", "%Y-%m-%d"))) # 從字符串轉換
print(datetime.fromtimestamp(t)) 
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)))


# 時間類型轉換
d = datetime.strptime('2019-03-27', '%Y-%m-%d')
print(d)

from dateutil.parser import parse
d = parse('2019/03/27')
print(d)
print(str(d))

print(d.strftime("%Y/%m/%d %H:%M:%S"))

print('------------------------------------------------------------')	#60個

# Pandas日期時間處理
# 時間點TimeStamp

t = pd.to_datetime('2019-03-01 00:00:00') # 從字符串轉換
print(type(t), t)
t = pd.to_datetime(datetime.now()) # 從datetime格式轉換
print(type(t), t)

# 時間間隔
t1 = pd.to_datetime('2019-03-01 00:00:00')
t2 = pd.to_datetime(datetime.now())
delta = t2-t1 # 通過TimeStamp相減獲取
print(type(delta), delta, delta.days, delta.seconds)

delta = pd.Timedelta(days=27) # 構造時間間隔爲27天
print(t2 + delta)

# 時間段Period
t = pd.to_datetime(datetime.now())
p = pd.Period(t, freq='H')
print(p, p.start_time, p.end_time) # 顯示時間段起止時間

# 批量轉換
arr = ['2019-03-01','2019-03-02','2019-03-03']
df = pd.DataFrame({'d':arr})
df['d'] = pd.to_datetime(df['d'])
print(df)

print('------------------------------------------------------------')	#60個

# 時間序列操作
# 時間日期類型索引
df.index = pd.to_datetime(df['d']) # 本例中使用了上例中構造的df[‘d’]
print(df.index)

df = pd.DataFrame()
df['date'] = pd.date_range(start='2017-12-30',end='2019-01-05',freq='d') # 創建時間數據
df['val'] = df['date'].apply(lambda x: x.weekday()) # 計算該日是星期幾
df.set_index('date', inplace = True) # 設置時間索引
print(df.head(3)) # 顯示前三條

# 時間段類型索引
df_period = df.to_period(freq='M') # 按月創建時間段
print(type(df_period.index)) # 查看類型
print(len(df_period)) # 查看記錄個數，與原記錄個數一致
print(df_period.head(3))

print(df_period.index[0].start_time, df_period.index[0].end_time)
print(df_period.index[1].start_time, df_period.index[1].end_time)
print(df.index.is_unique, df_period.index.is_unique)

df_dt = df_period.to_timestamp()
print(df_dt.head(3))
print(type(df_dt.index))

print('------------------------------------------------------------')	#60個

# 篩選和切分
print(df['2019'])  # 篩選2019全年數據
print(df['2019-01'])  #  篩選2019年一月全月數據
print(df['2018':'2019'].head()) # 篩選2018年初到2019年底的所有數據
print(df['2018-12-31':].head()) # 篩選2018-12-31及之後的數據

# 重採樣
tmp = df.resample('w').sum() # 使用疊加方式按周重採樣
print(tmp.head(3))

tmp = df.resample('M').ohlc() # 使用用ohlc方式按月降採樣
print(tmp.head(3))

tmp = df.resample('M').sum().to_period('M') # 按月降採樣，同時將時間變爲時間段
print(tmp.head(3))

df1 = pd.DataFrame({'val':[8,7,6]})
df1.index = pd.to_datetime(['2019-03-01','2019-03-15','2019-03-31']) # 僅含三條數據
df2 = df1.resample('D').interpolate() # 用插值方式升採樣
print(len(df2))
print(df2.head(3))

df3 = df1.asfreq('D')
print(df3.head(3))

# 偏移
df['prev'] = df['val'].shift() # 取前一條數據的val值作爲當前記錄中prev字段的值
print(df.head(3))

# 計算滑動窗口
df['sw'] = df['val'].rolling(window=3).mean() # 計算窗口中數據的均值
print(df.head(3))

df['emw_3'] = df['val'].ewm(span=3).mean()
df['emw_7'] = df['val'].ewm(span=7).mean()
df['rolling'] = df['val'].rolling(7).mean()

print('------------------------------------------------------------')	#60個

# 時區轉換

import pytz
print('時區個數 :', len(pytz.common_timezones))
print('前3個 :', pytz.common_timezones[:3])

import datetime
t = datetime.datetime.now()
print(t)

utc_dt = pytz.utc.localize(t)
print(utc_dt)

from pytz import timezone
tz = timezone('Asia/Shanghai') # 將時區設爲上海
print(utc_dt.astimezone(tz)) # 轉換時區

df = pd.DataFrame()
df['date'] = pd.date_range(start='2018-12-31',end='2019-01-01',freq='d')
df.set_index('date', inplace=True) # 設置時間索引
print(df.index)

df.index = df.index.tz_localize('UTC')
print(df.index.values, df.index)

df.index = df.index.tz_convert('Asia/Shanghai')
print(df.index.values)
print(df.index)

print('------------------------------------------------------------')	#60個

# 數據重排
# 數據錶轉置
df = pd.DataFrame({"a":[1,2],"b":[3,4]}, index=['l1','l2'])
print(df)
print(df.T)

# 行轉列和列轉行
df1 = df.stack() # 列轉行
print(df1)

print(df1.unstack()) # 將內層行索引轉爲列索引
print(df1.unstack(level=0)) # 將外層行索引轉爲列索引

# 透視轉換
df = pd.DataFrame({"時間":['期中','期末','期中','期末'],
                   "學科":['語文','語文','數學','數學'],
                   "分數":[89,75,90,95]})
df1 = df.pivot(index='時間', columns='學科', values='分數')
print(df, df1)

print("------------------------------------------------------------")  # 60個

""" fail
# 4.2.5 多圖組合
# jointplot兩變量圖

import statsmodels.api as sm
import seaborn as sns

sns.set(style="darkgrid")
data = sm.datasets.ccard.load_pandas().data
g = sns.jointplot('AVGEXP', 'AGE', data=data, kind="reg",
                 xlim=(0, 1000), ylim=(0, 50), color="m")
plt.show()

print('------------------------------------------------------------')	#60個

"""

import statsmodels.api as sm

# pairplot多變量圖
data = sm.datasets.ccard.load_pandas().data
sns.pairplot(data, vars=['AGE','INCOME', 'INCOMESQ','OWNRENT'])

plt.show()


print('------------------------------------------------------------')	#60個

""" fail
# factorplot兩變量關係圖
data = sm.datasets.fair.load_pandas().data
sns.factorplot(x='occupation', y='affairs', hue='religious', data=data)

plt.show()
"""

print('------------------------------------------------------------')	#60個

""" fail

# 準備工作

import pyecharts

attr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

# 4.3.3 繪製交互圖
# 柱圖
bar = pyecharts.Bar("Title1", "Title2")
bar.add("v1", attr, v1, mark_line=["average"], mark_point=["max", "min"])
bar.add("v2", attr, v2, mark_line=["average"], mark_point=["max", "min"])
bar.render('test.html')
bar

"""

print('------------------------------------------------------------')	#60個

print('讀寫XML文件')

from xml.dom import minidom

dom=minidom.Document()
root_node=dom.createElement('root') # 創建根節點
dom.appendChild(root_node) # 添加根節點

book_node=dom.createElement('blog') # 創建第一個子節點
book_node.setAttribute('level','3') # 添加屬性
root_node.appendChild(book_node) # 爲root添加子節點

name_node=dom.createElement('addr') # 創建第二個子節點
name_text=dom.createTextNode('https://blog.csdn.net/xieyan0811') # 添加文字
name_node.appendChild(name_text)
root_node.appendChild(name_node)

# toxml() 轉換成字符串, toprettyxml()轉換成樹形縮進版式
print(dom.toprettyxml())
with open('test_dom.xml','w') as fh:
    dom.writexml(fh, indent='',addindent='\t', newl='\n', encoding='UTF-8')

print('------------------------------------------------------------')	#60個


from xml.dom import minidom
with open('test_dom.xml','r') as fh:
    dom = minidom.parse(fh) # 獲取dom對象
    root = dom.documentElement # 獲取根節點
    print("node name", root.nodeName) # 顯示節點名: root
    print("node type", root.nodeType) # 顯示節點類型
    print("child nodes", root.childNodes) # 列出所有子節點
    blog = root.getElementsByTagName('blog')[0] # 根據標籤名獲取元素列表
    print(blog.getAttribute('level')) # 獲取屬性值
    addr = root.getElementsByTagName('addr')[0]
    print("addr's child nodes", addr.childNodes)
    text_node = addr.childNodes[0] # 獲取文本節點內容
    print("text data", text_node.data)
    print("parent", addr.parentNode.nodeName) # 顯示name的父節點名稱

print('------------------------------------------------------------')	#60個

print('抓取網站數據')

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

print('------------------------------------------------------------')	#60個

print('基本類型轉換')

dic = {
     'string': ['dog', 'snake', 'cat', 'dog', 'monkey', 'elephant'],
     'integer': [2000, 2000, 2001, 2002, 2003, np.nan],
     'float': [1.5, 1.5, 1.7, np.nan, np.nan, 8.3],
     'dtime': ['2018-01-01', '2018/01/02', '2018-01-03', '2018-01-04', '2018-01-05', np.nan],
     'mix': [1, 1, 0, '+', 0, 1],
     'classify': ['A', 'B', 'A', 'B', 'A', 'A']
                }
data = pd.DataFrame(dic)
print(data.dtypes)

data['dtime'] = pd.to_datetime(data['dtime'], infer_datetime_format=True)
data['mix']=pd.to_numeric(data['mix'],errors='coerce')
data['classify']=pd.Categorical(data['classify'])
data['float']=data['float'].astype(np.float32)
print(data.dtypes)

print('------------------------------------------------------------')	#60個

print('缺失值處理')

dic = {   
     'state': ['Ohio', 'Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
     'year': [2000, 2000, 2001, 2002, 2003, 3456],
     'score': [1.5, 1.5, 1.7, np.nan, np.nan, 8.3],
     'desc': [np.nan, np.nan, np.nan, np.nan, np.nan, 3],
     'val1': [1, 1, 0, '+', 0, 1],
}
data = pd.DataFrame(dic)

print(data['desc'].nunique()) # 不同取值個數
print(data['desc'].unique()) # 不同取值列表
print(data['year'].value_counts()) # 不同取值出現次數

print(data['desc'].isnull()) # 是否缺失
print(data['desc'].isnull().any()) # 是否含有任意缺失
print(data['desc'].isnull().all()) # 是否全部缺失
print(data['desc'].isnull().sum(), len(data)) # 空值個數與記錄個數
print(data.dropna(axis=1, how='all'))
print(data['score'].fillna(data['score'].mean()))
print(data['score'].fillna(method='ffill', limit=1))

print(data.interpolate(mdthod='polynomial', order=2)) # 二次多項式插值
print(data.interpolate(mdthod='spline', order=3)) # 三次樣條插值

print('------------------------------------------------------------')	#60個

print('異常值處理')

print(data.query('year<2050'))
print(data[data['year']<2050])

data['val1'] = data['val1'].apply(lambda x: 1 if x == '+' else x)


print('去重處理')

print(data.drop_duplicates(keep='last'))
print(data.drop_duplicates(keep='last', subset='year'))



print('------------------------------------------------------------')	#60個

print('簡單隨機抽樣')

import statsmodels.api as sm

data = sm.datasets.anes96.load_pandas().data
df = data.sample(50)
print(df.head())

print('系統抽樣')

index_list = [i for i in range(len(data)) if i % 10 == 0]
df = data.iloc[index_list]
print(df.head())

print('分層抽樣')

def typicalSampling(grp, typicalFracDict):
    name = grp.name
    frac = typicalFracDict[name]
    return grp.sample(frac=frac)

typicalFracDict = {
    0.0: 0.35,  
    1.0: 0.5,  
}
df = data.groupby('vote').apply(typicalSampling, typicalFracDict)
print(df.head())

print('整羣抽樣')
unique = np.unique(data['income'])
sample = random.sample(list(unique),2)
df = pd.DataFrame()
for label in sample:
    tmp = data[data['income']==label]  
    df = pd.concat([df, tmp])
print(df.head())

print('------------------------------------------------------------')	#60個

print('merge方法')

df1 = pd.DataFrame({'id': [1, 2, 3], 'val1': [2, 4, 6]})
df2 = pd.DataFrame({'id': [3, 2, 2], 'val2': [9, 6, 5]})
print(pd.merge(df1, df2, how='left'))

print('------------------------------------------------------------')	#60個

print('concat方法')

df1 = pd.DataFrame({'id': [1, 2, 3], 'val1': [2, 4, 6]})
df2 = pd.DataFrame({'id': [3, 2, 2], 'val2': [9, 6, 5]})
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))

print('------------------------------------------------------------')	#60個

print('數值型特徵')

dic = {'height': [1.6, 1.7, 1.8],
      'weight': [60, 70, 90]}
data = pd.DataFrame(dic)
data['bmi'] = data['weight'] / (data['height'] **2)
print(data)
data['overweight'] = data['bmi'] > 25
print(data)
data['overweight'] = data['overweight'].map({True:'Yes', False:'No'})
print(data)

print('------------------------------------------------------------')	#60個

print('類型特徵')

dic = {'string': ['第一組', '第二組', '第二組']}
data = pd.DataFrame(dic)
print(pd.factorize(data.string)) # 轉換成數值型編碼

data['num'] = pd.factorize(data['string'])[0]
df = pd.get_dummies(data['string'], prefix='組別')  # 轉換成onehot類型編碼
new_data = pd.concat([data, df], axis=1)
print(new_data)
'''
print('------------------------------------------------------------')	#60個

"""

sys.exit()

"""

#sklearn


print('------------------------------------------------------------')	#60個

print('線性迴歸')

def train(xArr,yArr):  # 訓練模型
    m,n = np.shape(xArr)
    xMat = np.mat(np.ones((m, n+1))) # 加第一列設爲1，用於計算截距
    x = np.mat(xArr)
    xMat[:,1:n+1] = x[:,0:n]
    yMat = np.mat(yArr).T  
    xTx = xMat.T*xMat
    if np.linalg.det(xTx) == 0.0:  #行列式的值爲0，無逆矩陣
        print("This matrix is sigular, cannot do inverse") 
        return None
    ws = xTx.I*(xMat.T*yMat)  
    return ws  

def predict(xArr, ws): # 預測
    m,n = np.shape(xArr)
    xMat = np.mat(np.ones((m, n+1))) # 加第一列設爲1, 爲計算截距
    x = np.mat(xArr)
    xMat[:,1:n+1] = x[:,0:n];
    return xMat*ws

if __name__ == '__main__':
    x = [[1], [2], [3], [4]]
    y = [4.1, 5.9, 8.1, 10.1]
    ws = train(x,y)
    if isinstance(ws, np.ndarray):
        print(ws)  # 返回結果：[[2.  ] [2.02]]
        print(predict([[5]], ws)) # 返回結果：[[12.1]]
        plt.scatter(x, y, s=20) # 繪圖
        yHat = predict(x, ws)
        plt.plot(x, yHat, linewidth=2.0) 
        plt.show()

print('------------------------------------------------------------')	#60個

print('邏輯迴歸')

def sigmoid(x): # S函數實現
    return 1.0 / (1.0 + np.exp(-x))
x = np.arange(-10,10,0.2) # 生成從-10, 10， 間隔爲0.2的數組
y = [sigmoid(i) for i in x]
plt.grid(True) # 顯示網格
plt.plot(x,y)

plt.show()


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('信息量和熵')

import math
def entropy(*c):
    if(len(c)<=0):
        return -1
    result = 0
    for x in c:
        result+=(-x)*math.log(x,2)
    return result;
print(entropy(0.99,0.01))
print(entropy(0.5,0.5))
print(entropy(0.333,0.333,0.333))

print('------------------------------------------------------------')	#60個

print('Apriori關聯規則')

from numpy import *

def load1(): 
    return [['香蕉','蘋果','梨','葡萄','櫻桃','西瓜','芒果','枇杷'],
            ['蘋果','菠蘿' ,'梨','香蕉','荔枝','芒果','橙子'],
            ['菠蘿','香蕉','桔子','橙子'],
            ['菠蘿','梨','枇杷'],
            ['蘋果','香蕉' ,'梨','荔枝','枇杷','芒果','香瓜']]

# 建立所有物品集合
def create_collection_1(data):
    c = []
    for item in data:
        for g in item:
            if not [g] in c:
                c.append([g])                
    c.sort()
    return list(map(frozenset, c))

def check_support(d_list, c_list, min_support):
    # d_list是購物數據，c_list是物品集合，support是支持度
    c_dic = {} # 組合計數
    for d in d_list: # 每次購物
        for c in c_list: # 每個組
            if c.issubset(d):
                if c in c_dic: 
                    c_dic[c]+=1 # 組合計數加1
                else: 
                    c_dic[c]=1 # 將組合加入字典
    d_count = float(len(d_list)) # 購物次數
    ret = []
    support_dic = {}
    for key in c_dic:
        support = c_dic[key]/d_count
        if support >= min_support: # 判斷支持度
            ret.append(key)
        support_dic[key] = support # 記錄支持度
    return ret, support_dic # 返回滿足支持率的組和支持度字典

def create_collection_n(lk, k):
    ret = []
    for i in range(len(lk)):
        for j in range(i+1, len(lk)): 
            l1 = list(lk[i])[:k-2];
            l1.sort()
            l2 = list(lk[j])[:k-2]
            l2.sort()
            if l1==l2:
                ret.append(lk[i] | lk[j])
    return ret

def apriori(data, min_support = 0.5):
    c1 = create_collection_1(data)
    d_list = list(map(set, data)) # 將購物列表轉換成集合列表
    l1, support_dic = check_support(d_list, c1, min_support)
    l = [l1]
    k = 2
    while (len(l[k-2]) > 0):
        ck = create_collection_n(l[k-2], k) # 建立新組合
        lk, support = check_support(d_list, ck, min_support) # 判斷新組是否適合支持率
        support_dic.update(support)
        l.append(lk) # 將本次結果加入整體
        k += 1
    return l, support_dic

data = load1()
l,support_dic = apriori(data)
print(l)
print()
print(support_dic)

print('------------------------------------------------------------')	#60個

print('樸素貝葉斯')

import jieba

def load2():
    arr = ['不知道該說什麼, 這麼爛的抄襲片也能上映, 我感到很尷尬',
       '天吶。一個大寫的滑稽。',
       '劇情太狗血，演技太浮誇，結局太無語。總體太渣了。這一個半小時廢了。',
       '畫面很美，音樂很好聽，主角演的很到位，很值得一看的電影，男主角很帥很帥，贊贊贊',
       '超級喜歡的一部愛情影片',
       '故事情節吸引人，演員演的也很好，電影裏的歌也好聽，總之值得一看，看了之後也會很感動的。']
    ret = []
    for i in arr:
        words = jieba.cut(i) # 將句子切分成詞
        ret.append(words)
    return ret,[0,0,0,1,1,1]

def create_vocab(data):
    vocab_set = set([])# 使用set集合操作去掉重複出現的詞彙
    for document in data:
        vocab_set = vocab_set | set(document) 
    return list(vocab_set)

def words_to_vec(vocab_list, vocab_set):  # 將句轉換成詞表格式
    ret = np.zeros(len(vocab_list)) # 創建數據表中的一行，並置初值爲0（不存在）
    for word in vocab_set:
        if word in vocab_list:
            ret[vocab_list.index(word)] = 1  # 若該詞在本句中出現，則設置爲1
    return ret

def train(X, y):
    rows = X.shape[0]
    cols = X.shape[1]
    percent = sum(y)/float(rows) # 正例佔比
    p0_arr = np.ones(cols) # 設置初值爲1，後作爲分子
    p1_arr = np.ones(cols)
    p0_count = 2.0 # 設初值爲2，後作爲分母
    p1_count = 2.0
    for i in range(rows): # 按每句遍歷
        if y[i] == 1:
            p1_arr += X[i] # 數組按每個值相加
            p1_count += sum(X[i]) # 句子所有詞個數相加(只計詞彙表中詞)
        else:
            p0_arr += X[i]
            p0_count += sum(X[i])
    p1_vec = np.log(p1_arr/p1_count) # 正例時，每個詞出現概率
    p0_vec = np.log(p0_arr/p0_count)
    return p0_vec, p1_vec, percent

def predict(X, p0_vec, p1_vec, percent):
    p1 = sum(X * p1_vec) + np.log(percent) # 爲1的概率
    p0 = sum(X * p0_vec) + np.log(1.0 - percent) #爲0的概率
    if p1 > p0:
        return 1
    else:
        return 0

sentences,y = load2()
vocab_list = create_vocab(sentences)
X=[]
for sentence in sentences:
    X.append(words_to_vec(vocab_list, sentence))
p0_vec, p1_vec, percent = train(np.array(X), np.array(y))
test = jieba.cut('抄襲得那麼明顯也是醉了！')
print(test)
test_X = np.array(words_to_vec(vocab_list, test))
print(test_X)
print(test,'分類',predict(test_X, p0_vec, p1_vec, percent))

print('------------------------------------------------------------')	#60個

""" some fail
from hmmlearn import hmm

states = ["A", "B", "C"] # 定義隱藏狀態
n_states = len(states)

observations = ["down","up"] # 定義觀測狀態
n_observations = len(observations)

p = np.array([0.7, 0.2, 0.1]) # 設置初始值概率pi
a = np.array([  # 設置狀態轉移矩陣A
   [0.5, 0.2, 0.3],
   [0.3, 0.5, 0.2],
   [0.2, 0.3, 0.5]
])
b = np.array([  # 設置狀態對觀測的生成矩陣B
  [0.6, 0.2],
  [0.3, 0.3],
  [0.1, 0.5]
])
o = np.array([[1, 0, 1, 1, 1]]).T # 設置觀測狀態

model = hmm.MultinomialHMM(n_components=n_states)
model.startprob_= p
model.transmat_= a
model.emissionprob_= b

logprob, h = model.decode(o, algorithm="viterbi")
print("The hidden h", ", ".join(map(lambda x: states[x], h))) # 顯示隱藏狀態

"""


print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('Hyperopt')

# pip install hyperopt
from hyperopt import fmin, tpe, hp, Trials

trials = Trials()
best = fmin(
    fn=lambda x: (x-1)**2, # 最小化目標，如誤差函數
    space=hp.uniform('x', -10, 10), # 定義搜索空間, 名稱爲x，範圍-10~10
    algo=tpe.suggest, # 指定搜索算法
    trials=trials, # 保存每次迭代的具體信息
    max_evals=50) # 評估次數
print(best) # 返回結果：{'x': 0.980859461591201}
for t in trials.trials:
    print(t['result'])

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


