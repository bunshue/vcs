"""
import seaborn as sns       #海生, 自動把圖畫得比較好看

"""

import sys
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns       #海生, 自動把圖畫得比較好看

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

#Python繪圖的方法-使用 seaborn

#匯入必要模組
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#匯入data
fmri = sns.load_dataset("fmri")#觀察fmri的資料型態是pandas
print(type(fmri))
#觀察欄位
print(fmri.head())

ax = sns.lineplot(x="timepoint", y="signal", data=fmri,err_style=None)
plt.show()

ax = sns.lineplot(x="timepoint", y="signal", data=fmri,err_style='band')
plt.show()

ax = sns.lineplot(x="timepoint", y="signal", data=fmri,err_style='bars')
plt.show()

fig,axs=plt.subplots(1,2,figsize=(10,8),sharey=True)
sns.lineplot(x="timepoint", y="signal", hue="event",data=fmri,ax=axs[0])
sns.lineplot(x="timepoint", y="signal", data=fmri,err_style='bars',ax=axs[1])
#設定hue="event"會畫出，不同的event對應的signal數值vs.timepoint
plt.show()


flights = sns.load_dataset("flights")
flights.head()
flights_wide = flights.pivot("year", "month", "passengers")
flights_wide.head()#畫出不同月份乘客人數和年份的關係
sns.lineplot(data=flights_wide)
plt.show()


#和上例是等效的，但是每組以不同“顏色”線分開
sns.lineplot(data=flights, x="year", y="passengers", hue="month")
plt.show()

#和上例是等效的，但是每組以不同“破折號”種類分開
sns.lineplot(data=flights, x="year", y="passengers", style="month")
plt.show()

#和上例是等效的，但是每組以不同“粗細的線”分開
sns.lineplot(data=flights, x="year", y="passengers", size="month")
plt.show()

#replot

#畫出不同region和event組合下不同的subject的signal vs. timepoint
sns.relplot(x="timepoint", y="signal", hue="subject", col="region", 
            row="event", height=3, kind="line", estimator=None, data=fmri);
plt.show()

print(fmri.query("region == 'frontal'"))
#大量水平變量狀況下，若展開多個圖，可以用col_wrap來指定圖片數目達到多少時換行，此利用以5為例
g=sns.relplot(x="timepoint", y="signal", hue="event", style="event",
            col="subject", col_wrap=5,
            height=2, aspect=1, linewidth=1.5,
            kind="line", data=fmri.query("region == 'frontal'"));
#height:圖片高
#aspect:圖片寬
#linewidth:線寬
#kind:指定繪圖方式
g.fig.suptitle('suptitle',x=0.5,y=1.1)
plt.subplots_adjust(wspace=0.1,hspace=0.5)
plt.show()

#pairplot

iris=sns.load_dataset('iris')
iris.head()
sns.pairplot(data=iris,hue="species")

plt.show()

#barplot

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
fig,axs=plt.subplots(1,2,figsize=(20,8))
data=sns.load_dataset('tips')
print(data)
##默認分組取平均值，capsize是設置誤差帽條(可和ci混用，用ci設置信心水準，用capsize設定帽蓋長度)
sns.barplot(x='day',y='total_bill',hue='sex',data=data,ax=axs[0],capsize=0.1)
sns.barplot(x='tip',y='day',data=data,ci=95,ax=axs[1])#ci表示信心水準(可設置float,sd,None)axs[0].set_title('Plot1')
axs[1].set_title('Plot2')
axs[0].set_ylim(0,30)
# axs[1].set_xlim(0,4)axs[0].legend(loc=2)
plt.subplots_adjust(wspace=0.2)
##若分組想要取其他種類的統計量，要透過estimator
fig.ax=plt.subplots()
#palette是著色表，可以參考以下網址
#https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette
sns.barplot(x='day',y='total_bill',hue='sex',ci=None,data=data,estimator=np.max,palette="Set2")

plt.show()

#histplot

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as snsdata=sns.load_dataset("penguins")
print(data)

fig,axs=plt.subplots(1,2,figsize=(20,8))
sns.histplot(data=data, x="flipper_length_mm",ax=axs[0],kde=True)
sns.histplot(data=data, y="flipper_length_mm",ax=axs[1],bins=15)
axs[0].set_title('Histplot1')
axs[1].set_title('Histplot2')

plt.show()

fig,axs=plt.subplots(3,2,figsize=(20,20))
sns.histplot(data=data, x="flipper_length_mm", hue="species",ax=axs[0][0])
sns.histplot(data=data, x="flipper_length_mm", hue="species",ax=axs[0][1],multiple="stack")
sns.histplot(data=data, x="flipper_length_mm", hue="species",ax=axs[1][0], element="step")
sns.histplot(data=data, x="flipper_length_mm", hue="species",ax=axs[1][1], element="poly")

axs[0][0].set_title('Add hue')
axs[0][1].set_title('Add hue+ stack')
axs[1][0].set_title('set element=step')
axs[1][1].set_title('set element=poly')

sns.histplot(data=data, x="flipper_length_mm",ax=axs[2][0],bins=20,stat='density')
sns.histplot(data=data, x="flipper_length_mm",ax=axs[2][1],bins=20,stat='probability',fill=False)
axs[2][0].set_title('stat=density')
axs[2][1].set_title('stat=probability, fill=False')

plt.show()


#X 和 Y都指定的histplot

plt.subplots(figsize=(10,5))
data1=data
sns.histplot(data=data1, x="bill_depth_mm", y="body_mass_g", hue="species",cbar=True, cbar_kws=dict(shrink=.75))

plt.subplots(figsize=(10,5))
data2=sns.load_dataset('planets')
print(data2)
#discrtete的tuple個對應到x軸和y軸，log_scale同理
sns.histplot(data=data2, x="year", y="distance",bins=30, discrete=(True,False),cbar=True,log_scale=(False, True))

plt.show()

#scatterplot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
fig,axs=plt.subplots(2,1,figsize=(10,20))
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="day", style="time",ax=axs[0])
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="size",size="size",sizes=(20, 80), legend="full")
axs[0].legend(loc=1)

plt.show()

#boxplot

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fig,axs=plt.subplots(2,1,figsize=(10,15))
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="smoker",data=tips,linewidth=1.5,hue_order=['No','Yes'],ax=axs[0])
sns.boxplot(x="day", y="total_bill",data=tips,ax=axs[1])
sns.swarmplot(x="day", y="total_bill",data=tips, color=".25",ax=axs[1])

plt.show()

#violinplot

fig,axs=plt.subplots(1,2,figsize=(20,10))
iris = sns.load_dataset("iris")
sns.violinplot(x="species", y="sepal_length", data=iris,ax=axs[0])
sns.violinplot(x=iris.species, y=iris.sepal_length,ax=axs[1])

plt.show()

#catplot

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#分類散點圖
#stript plot
sns.load_dataset("tips")
sns.catplot(x="day", y="total_bill", data=tips);
#stript plot + jitter
sns.catplot(x="day", y="total_bill", jitter=False, data=tips);
#swarm plot
sns.catplot(x="day", y="total_bill", hue="sex", kind="swarm", data=tips);

plt.show()


#分類分布圖
##boxplot
sns.catplot(x="day", y="total_bill", kind="box", data=tips);
sns.catplot(x="day", y="total_bill", hue="smoker", kind="box", data=tips);
plt.show()

#小提琴圖(violin plot)
sns.catplot(x="total_bill", y="day", hue="time", kind="violin", data=tips);
sns.catplot(x="day", y="total_bill", hue="sex", kind="violin", split=True, data=tips);
g=sns.catplot(x="day", y="total_bill", kind="violin", data=tips);
sns.swarmplot(x="day", y="total_bill", color="k", size=3, data=tips, ax=g.ax);
plt.show()

#分類統計估計圖#barplot
titanic = sns.load_dataset("titanic")
g1=sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic,ci=None);
g2=sns.catplot(x="survived", hue="class", kind="count", palette="pastel", edgecolor=".6", data=titanic);
#catplot本身是個FacetGrid
g1.ax.set_title('Survived vs. sex between differenrt class')
plt.show()

#點圖(point plot)
sns.catplot(x="class", y="survived", hue="sex", palette={"male": "g", "female": "m"}, markers=["^", "o"], linestyles=["-", "--"], kind="point", data=titanic);
plt.show()

#使用子圖展示多重關係
tips=sns.load_dataset('tips')
sns.catplot(x="day", y="total_bill", hue="smoker", col="time", aspect=0.7, kind="swarm", data=tips,sharey=False);
plt.subplots_adjust(wspace=0.2)

plt.show()

#jointplot

penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", hue="species")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="reg")

plt.show()

g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm")
g.plot_joint(sns.kdeplot, color="r", zorder=0, levels=6)
# g.plot_marginals(sns.rugplot, color="r", height=-.15, clip_on=False)

plt.show()


g.plot_marginals(sns.rugplot, color="r", height=-.15, clip_on=False)

plt.show()

#FacetGrid

#以上兩種搭配一起用

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
## g.map內的plotting function可以是任何matplotlib, sns繪圖方法
tips=sns.load_dataset('tips')
g1 = sns.FacetGrid(tips, col="sex", hue="smoker")
g1.map(plt.scatter, "total_bill", "tip", alpha=.7)
g1.add_legend();g2 = sns.FacetGrid(tips, col="sex", hue="smoker")
g2.map(sns.scatterplot, "total_bill", "tip", alpha=.7)
g2.add_legend();

plt.show()

#heatmap

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")
print(flights)

ax = sns.heatmap(flights)

plt.show()

ax=sns.heatmap(flights, annot=True, fmt="d")

plt.show()

#用mask來只畫出部分熱力圖
random_data=np.random.randn(10, 200)
corr = np.corrcoef(random_data)
mask = np.zeros_like(corr)
print(mask)
mask[np.triu_indices_from(mask)] = True
print(mask)
fig,ax=plt.subplots(figsize=(6,6))
sns.heatmap(corr, ax=ax, mask=mask, vmax=.3, square=True)

plt.show()

grid_kws = {"height_ratios": (.95, .05), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2,figsize=(6,6) ,gridspec_kw=grid_kws)
ax = sns.heatmap(flights, ax=ax,cbar_ax=cbar_ax,cbar_kws={"orientation": "horizontal"})

plt.show()


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





