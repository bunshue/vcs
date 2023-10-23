########################################################################
#                                                                      #
#        ȥ�Ķ��� �����������Ƶ����֡��Ƶ�ȼ� vs ·�߼۸� ��ģ        #
#                                                                      #
########################################################################
#%matplotlib inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


df = pd.read_csv("D:/qunar_routes.csv")
print (df.head())
print (df.info())

df["����"]=df.·����Ϣ.str.extract('(\d+)��\d+��').apply(lambda x: int(x))
df["�Ƶ�����"]=df.�Ƶ���Ϣ.str.extract('(\d\.\d)��').apply(lambda x: float(x))
df["�Ƶ�ȼ�"]=df.�Ƶ���Ϣ.str.extract('\n(.*)')
df["�۸�"]=df.·����Ϣ.str.extract('(\d+)��/��').apply(lambda x: int(x))
print (df.head())
print (df.info())

class_map = {"����":0,"������":1,"������":2,"�ߵ���":3,"������":4}
df["�Ƶ�ȼ�"]=df["�Ƶ�ȼ�"].map(class_map)

# �Ա�����ֱ��ͼ���鿴�Ƿ����쳣ֵ
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
df["�Ƶ�ȼ�"].plot(ax=axes[0], kind='hist', title="�Ƶ�ȼ�")
df["�Ƶ�����"].plot(ax=axes[1], kind='hist', title="�Ƶ�����")
df["�۸�"].plot(ax=axes[2], kind='hist', title="�۸�")

#��ȡ�Ա���X,�����y
X,y = df.ix[:,4:-1].values, df.ix[:,-1].values

# ���OLS���Իع�ģ�� 
ols = sm.OLS(y,X)
result = ols.fit()
print (result.summary())

y_pred = result.predict(X)
ratio = y_pred/y
df["�Լ۱�"] = ratio
print (df.sort_values("�Լ۱�", ascending=False))