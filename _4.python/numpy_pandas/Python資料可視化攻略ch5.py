import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei

#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

# 定義資料 
sales_dep = pd.DataFrame({
    "label": ["第1業務部", "第2業務部", "第3業務部",
              "網路事業部1", "網路事業部2"],
    "value": [500, 130, 200, 75, 20]})

print('繪製預設的派圖')
plt.pie(sales_dep["value"], labels=sales_dep["label"],
        autopct="%1.1f%%")

plt.show()

print('從12點鐘方向開始繪製的派圖')

# 排序（這次一開始就先排序資料） 
sales_dep = sales_dep.sort_values("value", ascending=False) 
plt.pie(sales_dep["value"], labels=sales_dep["label"],
        autopct="%1.1f%%", startangle=90, counterclock=False) 

plt.show()


print('只變更要強調的扇形的顏色')

# 要強調的扇形的標籤 
point_label = "第3業務部" 
# 重點色 
point_color = "#CC0000" 
# 調整特定標籤的顏色
palette = sns.color_palette("binary", len(sales_dep)) 
for i in sales_dep[sales_dep.label == point_label].index.values:
    palette[i] = point_color 

plt.pie(sales_dep["value"], labels=sales_dep["label"],
        autopct="%1.1f%%", startangle=90, counterclock=False,
        colors=palette)

plt.show()

print('------------------------------------------------------------')	#60個

# 折線圖
# 日本各都市平均氣溫全年資料

filename = 'data/weather_sample.csv'
weather = pd.read_csv(filename, header=0, parse_dates=["年月"])

#折線圖的繪製範例
#sns.set(style="whitegrid", font="meiryo")

# 由於座標軸的最小值不能為0，所以指定y軸的值
plt.ylim([0, 30])

sns.lineplot(data=weather, x="年月", y="東京-平均氣溫(℃)")


#sns.set(style="whitegrid", font="meiryo")
plt.ylim([0, 30])
sns.lineplot(data=weather, x="年月", y="東京-平均氣溫(℃)")

# 讓年月轉成90度的直書格式，才更方便閱讀
plt.xticks(rotation=90)

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'data/weather_sample.csv'
weather_index = pd.read_csv(filename, header=0,
                             parse_dates=["年月"], index_col=0) 
tmp_ave = weather_index[["東京-平均氣溫(℃)", "大阪-平均氣溫(℃)",
                         "那霸-平均氣溫(℃)", "函館-平均氣溫(℃)"]] 
print(tmp_ave)

# 在單一圖表繪製多張折線圖的範例

# 繪製折線圖
#sns.set(style="white", font="meiryo")
ax = sns.lineplot(data=tmp_ave)

# 適度調整標籤與圖例
plt.xticks(rotation=90)
ax.legend(loc="lower left", bbox_to_anchor=(1, 0))

print('ddd')
plt.show()

print('------------------------------------------------------------')	#60個

#將多張折線圖的折線設定為同一種類的範例

# 調整資料的格式
#sns.set(style="white", font="meiryo") 
tmp_stack = tmp_ave.stack().rename_axis(["年月", "category"]).reset_index().rename(columns={0: "value"}) 
print(tmp_stack)

# 繪製折線圖
#sns.set(style="white", font="meiryo") 
ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category",
                  palette="pastel") 
# 適度調整標籤與圖例 
plt.xticks(rotation=90) 
ax.legend(loc="lower left", bbox_to_anchor=(1, 0))

print('eee')
plt.show()

print('------------------------------------------------------------')	#60個

#強調特定折線圖的範例
#sns.set(style="white", font="meiryo") 
tmp_stack = tmp_ave.stack().rename_axis(["年月", "category"]).reset_index().rename(columns={0: "value"}) 
print(tmp_stack)

# 計算分類數量 
num_category = len(tmp_stack["category"].unique()) 
# 設定顏色 
point_color = "#CC0000"

# 要變更的分類的編號 
point_number = 2

# 建立原始的調色盤
palette = sns.color_palette("gray_r", num_category)

# 變更調色盤的部分顏色
palette[point_number] = point_color 

# 繪製折線圖
ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category",
                  palette=palette) 
# 適度調整標籤與圖例 
plt.xticks(rotation=90) 
ax.legend(loc="lower left", bbox_to_anchor=(1, 0))

print('fff')
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('作業完成')

print('------------------------------------------------------------')	#60個




