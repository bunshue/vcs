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

# # 一、使用sndHsPr

import matplotlib

#get_ipython().magic('matplotlib inline')

snd = pd.read_csv("sndHsPr.csv")

snd["all_pr2"]=snd[["price","AREA"]].apply(lambda x:x[0]*x[1], axis = 1 )
snd.head()

# ## 1、把dist變量重新編碼為中文，比如chaoyang改為朝陽區。1）先作頻次統計，然后繪制柱形圖圖展現每個區樣本的數量；

# ###  把dist變量重新編碼為中文，比如chaoyang改為朝陽區。  

district = {'fengtai':'豐臺區','haidian':'海淀區','chaoyang':'朝陽區','dongcheng':'東城區','xicheng':'西城區','shijingshan':'石景山區'}
snd['district'] = snd.dist.map(district)
# snd_new = snd.drop('dist',axis = 1)
snd.head()

#4.1 描述性統計與探索型數據分析
# ### 1單因子頻數:描述名義變量的分布

#snd.dist.value_counts()
snd.district.value_counts()
#type(snd.district.value_counts())
#snd.district.value_counts()/snd.district.count()

snd.district.value_counts().plot(kind = 'bar')
#snd.district.value_counts().plot(kind = 'pie')  

# ### 2 單變量描述:描述連續變量的分布

snd.price.mean()

snd.price.median()

snd.price.std()

snd.price.skew()

snd.price.agg(['mean','median','sum','std','skew'])

snd.price.quantile([0.01,0.5,0.99])

snd.price.hist(bins=40)

#4.2 描述統計方法大全
# ### 1.1表分析

sub_sch = pd.crosstab(snd.district,snd.school)
sub_sch

pd.crosstab(snd.dist,snd.subway).plot(kind="bar")

#pd.crosstab(snd.district,snd.school).plot(kind = 'bar')
t1=pd.crosstab(snd.district,snd.school)
t1.plot(kind = 'bar',stacked= True)
type(t1)

sub_sch = pd.crosstab(snd.district,snd.school)
sub_sch["sum1"]=sub_sch.sum(1)
sub_sch.head()

sub_sch = sub_sch.div(sub_sch.sum1,axis = 0)
sub_sch

sub_sch[[0,1]].plot(kind = 'bar',stacked= True)

from stack2dim import *

stack2dim(snd, i="district", j="school")

from pyecharts import Map
#from echarts-china-cities-pypkg import *
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
snd_price = list(zip(snd.price.groupby(snd.district).mean().index,
                  snd.price.groupby(snd.district).mean().values))
attr, value = Map.cast(snd_price)
min_ = snd.price.groupby(snd.dist).mean().min()
max_ = snd.price.groupby(snd.dist).mean().max()

map = Map('北京各區房價', width = 1200, height = 600)
map.add('', attr, value, maptype = '北京', is_visualmap = True, visual_range=[min_, max_], 
        visual_text_color = '#000', is_label_show =True)
map.render()

# ![北京房價](北京各區房價.png)

# ### 1.2 分類匯總
snd.price.groupby(snd.district).mean().plot(kind="bar")

snd.price.groupby(snd.district).mean().sort_values(ascending= True).plot(kind = 'barh')

sns.boxplot(x = 'district', y = 'price', data = snd)

# ### 1.3 匯總表

snd.pivot_table(values='price', index='district', columns='school', aggfunc=np.mean)

snd.pivot_table(values='price', index='district', columns='school', aggfunc=np.mean).plot(kind = 'bar')

# ### 1.4、兩個連續變量---使用area和price做散點圖，分析area是否影響單位面積房價

snd.plot.scatter(x = 'AREA', y = 'price')

# ### 1.5 雙軸圖 需要導入GDP數據

# - 按年度匯總GDP，并計算GDP增長率。繪制雙軸圖。GDP為柱子，GDP增長率為線。

gdp = pd.read_csv('gdp_gdpcr.csv',encoding = 'gbk')
gdp.head()

x = list(gdp.year)
GDP = list(gdp.GDP)
GDPCR = list(gdp.GDPCR)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.bar(x,GDP)
ax1.set_ylabel('GDP')
ax1.set_title("GDP of China(2000-2017)")
ax1.set_xlim(2000,2018)

ax2 = ax1.twinx()
ax2.plot(x,GDPCR,'r')
ax2.set_ylabel('Increase Ratio')
ax2.set_xlabel('Year')

######################################################################################################################################
#以下內容為第8章內容
# ### 3、對age按照5歲間隔分段，命名為age_group，用loss_flag對age_group作logit圖。
# ### 1）手工計算Logit,即WOE

auto = pd.read_csv('auto_ins.csv',encoding = 'gbk')

auto.Loss = auto.Loss.map(lambda x: 1 if x >0 else 0)

bins = [21,26,31,36,41,46,51,56,61,67]
labels = [1,2,3,4,5,6,7,8,9]
auto['age_group'] = pd.cut(auto.Age, bins, labels = labels, right =False)

log_tab = pd.crosstab(auto.age_group,auto.Loss)
log_tab

log_tab[['p0','p1']] = log_tab[[0,1]].apply(lambda x: x/sum(x))
log_tab['log'] = log_tab[['p1','p0']].apply(lambda x: np.log(x[0]/x[-1]),axis = 1)
log_tab

log_tab.log.plot()

from woe import WoE

woe = WoE(v_type='d')
woe.fit(auto.age_group,auto.Loss)
fig = woe.plot([8,5])
plt.show(fig)

