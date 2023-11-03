
# coding: utf-8

# # 一、使用sndHsPr

# In[44]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os
#get_ipython().magic('matplotlib inline')


# In[47]:
os.chdir(r'D:\Python_book\4Describe')
snd = pd.read_csv("sndHsPr.csv")


# In[54]:

snd["all_pr2"]=snd[["price","AREA"]].apply(lambda x:x[0]*x[1], axis = 1 )
snd.head()


# ## 1、把dist变量重新编码为中文，比如chaoyang改为朝阳区。1）先作频次统计，然后绘制柱形图图展现每个区样本的数量；

# ###  把dist变量重新编码为中文，比如chaoyang改为朝阳区。  

# In[21]:

district = {'fengtai':'丰台区','haidian':'海淀区','chaoyang':'朝阳区','dongcheng':'东城区','xicheng':'西城区','shijingshan':'石景山区'}
snd['district'] = snd.dist.map(district)
# snd_new = snd.drop('dist',axis = 1)
snd.head()

#4.1 描述性统计与探索型数据分析
# ### 1单因子频数:描述名义变量的分布

# In[22]:

#snd.dist.value_counts()
snd.district.value_counts()
#type(snd.district.value_counts())
#snd.district.value_counts()/snd.district.count()


# In[30]:

#如遇中文显示问题可加入以下代码
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
snd.district.value_counts().plot(kind = 'bar')
#snd.district.value_counts().plot(kind = 'pie')  

# ### 2 单变量描述:描述连续变量的分布

# In[48]:

snd.price.mean()


# In[4]:

snd.price.median()


# In[5]:

snd.price.std()


# In[6]:

snd.price.skew()


# In[16]:
snd.price.agg(['mean','median','sum','std','skew'])


# In[17]:

snd.price.quantile([0.01,0.5,0.99])


# In[15]:

snd.price.hist(bins=40)
#%%
#4.2 描述统计方法大全
# ### 1.1表分析

# In[27]:

sub_sch = pd.crosstab(snd.district,snd.school)
sub_sch


# In[24]:

pd.crosstab(snd.dist,snd.subway).plot(kind="bar")


# In[22]:

#pd.crosstab(snd.district,snd.school).plot(kind = 'bar')
t1=pd.crosstab(snd.district,snd.school)
t1.plot(kind = 'bar',stacked= True)
type(t1)


# In[38]:

sub_sch = pd.crosstab(snd.district,snd.school)
sub_sch["sum1"]=sub_sch.sum(1)
sub_sch.head()


# In[29]:

sub_sch = sub_sch.div(sub_sch.sum1,axis = 0)
sub_sch


# In[30]:

sub_sch[[0,1]].plot(kind = 'bar',stacked= True)


#%%
from stack2dim import *

stack2dim(snd, i="district", j="school")

#%%
from pyecharts import Map
#from echarts-china-cities-pypkg import *
"""
官网给的解释如下：

自从 0.3.2 开始，为了缩减项目本身的体积以及维持 pyecharts 项目的轻量化运行，pyecharts 将不再自带地图 js 文件。如用户需要用到地图图表，可自行安装对应的地图文件包。下面介绍如何安装。

全球国家地图: echarts-countries-pypkg (1.9MB): 世界地图和 213 个国家，包括中国地图
中国省级地图: echarts-china-provinces-pypkg (730KB)：23 个省，5 个自治区
中国市级地图: echarts-china-cities-pypkg (3.8MB)：370 个中国城市:https://github.com/echarts-maps/echarts-china-cities-js
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
别注明，中国地图在 echarts-countries-pypkg 里。
"""
#%%
snd_price = list(zip(snd.price.groupby(snd.district).mean().index,
                  snd.price.groupby(snd.district).mean().values))
attr, value = Map.cast(snd_price)
min_ = snd.price.groupby(snd.dist).mean().min()
max_ = snd.price.groupby(snd.dist).mean().max()

map = Map('北京各区房价', width = 1200, height = 600)
map.add('', attr, value, maptype = '北京', is_visualmap = True, visual_range=[min_, max_], 
        visual_text_color = '#000', is_label_show =True)
map.render()


# ![北京房价](北京各区房价.png)
#%%


# ### 1.2 分类汇总

# In[31]:

snd.price.groupby(snd.district).mean().plot(kind="bar")


# In[34]:

snd.price.groupby(snd.district).mean().sort_values(ascending= True).plot(kind = 'barh')


# In[37]:

sns.boxplot(x = 'district', y = 'price', data = snd)


# ### 1.3 汇总表

# In[38]:

snd.pivot_table(values='price', index='district', columns='school', aggfunc=np.mean)


# In[39]:

snd.pivot_table(values='price', index='district', columns='school', aggfunc=np.mean).plot(kind = 'bar')


# ### 1.4、两个连续变量---使用area和price做散点图，分析area是否影响单位面积房价

# In[ ]:

snd.plot.scatter(x = 'AREA', y = 'price')


# ### 1.5 双轴图 需要导入GDP数据

# - 按年度汇总GDP，并计算GDP增长率。绘制双轴图。GDP为柱子，GDP增长率为线。

# In[40]:

gdp = pd.read_csv('gdp_gdpcr.csv',encoding = 'gbk')
gdp.head()
# In[45]:

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
#以下内容为第8章内容
# In[ ]:
# ### 3、对age按照5岁间隔分段，命名为age_group，用loss_flag对age_group作logit图。

# ### 1）手工计算Logit,即WOE

# In[136]:
auto = pd.read_csv('auto_ins.csv',encoding = 'gbk')
# In[134]:


auto.Loss = auto.Loss.map(lambda x: 1 if x >0 else 0)


bins = [21,26,31,36,41,46,51,56,61,67]
labels = [1,2,3,4,5,6,7,8,9]
auto['age_group'] = pd.cut(auto.Age, bins, labels = labels, right =False)


# In[138]:


log_tab = pd.crosstab(auto.age_group,auto.Loss)
log_tab


# In[124]:
log_tab[['p0','p1']] = log_tab[[0,1]].apply(lambda x: x/sum(x))
log_tab['log'] = log_tab[['p1','p0']].apply(lambda x: np.log(x[0]/x[-1]),axis = 1)
log_tab


# In[125]:


log_tab.log.plot()
# In[124]:
from woe import WoE
woe = WoE(v_type='d')
woe.fit(auto.age_group,auto.Loss)
fig = woe.plot([8,5])
plt.show(fig)
# In[124]:


