# matplotlib_新進測試13_pie

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

import os
import time
import random

print("------------------------------------------------------------")  # 60個

""" OK 但搬遷有問題
# 饼图的绘制

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']
# 绘制饼图
plt.pie(x = edu, # 绘图数据
labels = labels, # 添加教育水平标签
autopct = '%.1f%%' # 设置百分比的格式，这里保留一位小数
)
# 添加图标题
plt.title('失信用户的教育水平分布')

plt.show()

print("------------------------------------------------------------")  # 60個

# 构造数据
edu = [0.2515,0.3724,0.3336,0.0368,0.0057]
labels = ['中专','大专','本科','硕士','其他']
# 添加修饰的饼图
explode = [0,0.1,0,0,0] # 生成数据，用于突出显示大专学历人群
colors = ['#9999ff','#ff9999','#7777aa','#2442aa','#dd5555'] # 自定义颜色
# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
# 将横、纵坐标轴标准化处理，确保饼图是一个正圆，否则为椭圆
plt.axes(aspect = 'equal')
# 绘制饼图
plt.pie(x = edu, # 绘图数据
explode = explode, # 突出显示大专人群
labels = labels, # 添加教育水平标签
colors = colors, # 设置饼图的自定义填充色
autopct = '%.1f%%', # 设置百分比的格式，这里保留一位小数
pctdistance = 0.8, # 设置百分比标签与圆心的距离
labeldistance = 1.1, # 设置教育水平标签与圆心的距离
startangle = 180, # 设置饼图的初始角度
radius = 1.2, # 设置饼图的半径
counterclock = False, # 是否逆时针，这里设置为顺时针方向
wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'},# 设置饼图内外边界的属性值
textprops = {'fontsize':10, 'color':'black'}, # 设置文本标签的属性值
)
# 添加图标题
plt.title('失信用户的受教育水平分布')

plt.show()

print("------------------------------------------------------------")  # 60個

# 构建序列
data1 = pd.Series({'中专':0.2515,'大专':0.3724,'本科':0.3336,'硕士':0.0368,'其他':0.0057})
print(data1)
data1.name = ''
# 控制饼图为正圆
plt.axes(aspect = 'equal')
# plot方法对序列进行绘图
data1.plot(kind = 'pie', # 选择图形类型
autopct = '%.1f%%', # 饼图中添加数值标签
radius = 1, # 设置饼图的半径
startangle = 180, # 设置饼图的初始角度
counterclock = False, # 将饼图的顺序设置为顺时针方向
title = '失信用户的受教育水平分布', # 为饼图添加标题
wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'}, # 设置饼图内外边界的属性值
textprops = {'fontsize':10, 'color':'black'} # 设置文本标签的属性值
)

plt.show()
"""
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


