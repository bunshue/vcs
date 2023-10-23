# 等高線圖 Contour Chart 集合

"""
將資料繪製成等高線圖 ( Contour Chart )
並進一步介紹 contour() 的相關用法
以及使用 contourf() 將等高線圖變成等高線面積圖。

pyplot.contour() 參數
參數 	說明
x 	必填，等高線圖的中心點 x 座標，使用串列格式。
y 	必填，等高線圖的中心點 y 座標，使用串列格式。
z 	必填，等高線圖的高度，使用串列格式。
levels 	等高線的數量。
colors 	等高線顏色，使用串列格式，若不足 levels 的數量，則會自動重複，不能和 map 同時使用。
cmap 	等高線顏色，使用 colormaps，不能和 colors 同時使用。
vmin, vmax 	等高線顏色的最小值與最大值。
linewidths 	等高線的粗細。
"""

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

'''

N = 5
x1, x2 = np.meshgrid(np.arange(-N, (N + 1), 1), np.arange(-N, (N + 1), 1))

print(x1)
print(x2)
print(x1 * x2)
print(x1 * x1 + x2 * x2)

z = x1 * x1 + x2 * x2

plt.contourf(x1, x2, z, alpha = 0.3)
plt.grid()
plt.show()
'''
print('------------------------------------------------------------')	#60個

#下方的程式碼，執行後會先使用 x 和 y 畫出一個二維的直角座標系統，
#接著 z 使用二維陣列，標記每個位置的高度，最後就會根據數據資料畫出等高線圖。

x = range(5)
y = range(5)
z = [[0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,2,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]]
plt.contour(x,y,z,levels=5)
plt.show()


print('------------------------------------------------------------')	#60個


#繪製更精緻的等高線圖
#參考 matplotlib 官方網站的運算式，搭配 numpy 的 linspace 方法，就能做出更細緻的等高線圖。

x = np.linspace(-3, 3, 200)    # 產生從 -3～3 共 200 的數值的 x
y = np.linspace(-3, 3, 200)    # 產生從 -3～3 共 200 的數值的 y
z = [[(1 - x[i]/2 + x[i]*3 + y[j]*5) * math.exp(-x[i]**2 - y[j]**2) for i in range(200)] for j in range(200)]
# 根據 x 和 y 計算出 z
lv = np.linspace(np.min(z), np.max(z), 20)  # 根據 z 的最大值和最小值，定義 level 區間
plt.figure(figsize=(8,6))
plt.contour(x,y,z,levels=lv)
plt.show()

print('------------------------------------------------------------')	#60個

#使用 contourf() 繪製等高線面積圖

#如果將 contour() 換成 contourf()，繪製的圖形就會變成「等高線面積圖」，
#下方的程式碼執行後，會畫出等高線面積圖和等高線結合的圖表。

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
z = [[(1 - x[i]/2 + x[i]*3 + y[j]*5) * math.exp(-x[i]**2 - y[j]**2) for i in range(200)] for j in range(200)]
lv = np.linspace(np.min(z), np.max(z), 10)
plt.figure(figsize=(8,6))
plt.contourf(x,y,z,levels=lv,cmap='Reds')           # 等高線面積圖
plt.contour(x,y,z,levels=lv,colors=['#000','#000']) # 等高線圖
plt.show()

print('------------------------------------------------------------')	#60個

x = np.arange(1, 10)
y = x.reshape(-1, 1)
h = x * y

cs = plt.contourf(h, levels=[10, 30, 50],
    colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
cs.cmap.set_over('red')
cs.cmap.set_under('blue')
cs.changed()
plt.show()

print('------------------------------------------------------------')	#60個

x = np.arange(1, 10)
y = x.reshape(-1, 1)
h = x * y

cs = plt.contourf(h, levels=[10, 30, 50],
    colors=['#808080', '#A0A0A0', '#C0C0C0'], extend='both')
cs.cmap.set_over('red')
cs.cmap.set_under('blue')
cs.changed()

plt.show()

print('------------------------------------------------------------')	#60個

np.random.seed(19680801)
Z = np.random.rand(6, 10)
x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7

fig, ax = plt.subplots()
ax.pcolormesh(x, y, Z)

plt.show()

print('------------------------------------------------------------')	#60個


x = np.arange(-0.5, 10, 1)  # len = 11
y = np.arange(4.5, 11, 1)  # len = 7
X, Y = np.meshgrid(x, y)
X = X + 0.2 * Y  # tilt the coordinates.
Y = Y + 0.3 * X

fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z)

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


