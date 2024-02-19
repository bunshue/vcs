import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

#折線圖
def lineChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.plot(x, s, marker='.')

#長條圖
def barChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.bar(x, s)

#橫條圖
def barhChart(s,x):
    plt.barh(x, s)

#圓餅圖
def pieChart(s,x):	 
    plt.pie(s,labels=x, autopct='%.2f%%')

#要繪圖的數據
x = ['第一季', '第二季', '第三季', '第四季']
s = [13.2, 20.1, 11.9, 14.2]

#定義子圖
plt.figure(1, figsize=(8, 6),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(2,2,1)
pieChart(s,x)

x = ['程式設計概論', '多媒體概論', '計算機概論', '網路概論']
s = [3560, 4000, 4356, 1800]
plt.subplot(2,2,2)
barhChart(s,x)

x = ['新北市', '台北市', '高雄市', '台南市','桃園市','台中市']
s = [0.2, 0.3, 0.15, 0.23,0.19, 0.27]
plt.subplot(223)
lineChart(s,x)

plt.subplot(224)
barChart(s,x)

plt.show()

print("------------------------------------------------------------")  # 60個



import matplotlib.pyplot as plt

data1 = [1, 2, 3, 4, 5, 6, 7, 8]                # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]           # data2線條
data3 = [1, 3, 6, 10, 15, 21, 28, 36]           # data3線條
data4 = [1, 7, 15, 26, 40, 57, 77, 100]         # data4線條

seq = [1, 2, 3, 4, 5, 6, 7, 8]

plt.subplot(2, 2, 1)
plt.plot(seq, data1, '-*')

plt.subplot(2, 2, 2)
plt.plot(seq, data2, '-o')

plt.subplot(2, 2, 3)
plt.plot(seq, data3, '-^')

plt.subplot(2, 2, 4)
plt.plot(seq, data4, '-s')

plt.show()


print("------------------------------------------------------------")  # 60個

# 建立衰減數列.
x1 = np.linspace(0.0, 5.0, 50)
y1 = np.cos(3 * np.pi * x1) * np.exp(-x1)
# 建立非衰減數列
x2 = np.linspace(0.0, 2.0, 50)
y2 = np.cos(3 * np.pi * x2)

plt.subplot(2,1,1)
plt.title('衰減數列')
plt.plot(x1, y1, 'go-')
plt.ylabel('衰減值')

plt.subplot(2,1,2)
plt.plot(x2, y2, 'm.-')
plt.xlabel('時間(秒)')
plt.ylabel('非衰減值')

plt.show()

print("------------------------------------------------------------")  # 60個

data1 = [1, 2, 3, 4, 5, 6, 7, 8]        # data1線條
data2 = [1, 4, 9, 16, 25, 36, 49, 64]   # data2線條
seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.subplot(1, 2, 1)                    # 子圖1
plt.plot(seq, data1, '-*')
plt.subplot(1, 2, 2)                    # 子圖2
plt.plot(seq, data2, 'm-o')                      

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

x = np.linspace(0.0, np.pi, 100)
plt.subplot(2,2,1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(2,2,2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(2,2,3)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

x = np.linspace(0.0, np.pi, 100)
plt.subplot(221)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(222)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(223)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()

print("------------------------------------------------------------")  # 60個

def f(t):
    return np.exp(-t) * np.sin(2*np.pi*t)

x = np.linspace(0.0, np.pi, 100)
plt.subplot(2,2,1)          # 子圖 1
plt.plot(x, f(x))
plt.title('子圖 1')
plt.subplot(2,2,2)          # 子圖 2
plt.plot(x, f(x))
plt.title('子圖 2')
plt.subplot(2,1,2)          # 子圖 3
plt.plot(x, f(x))
plt.title('子圖 3')

plt.show()

print("------------------------------------------------------------")  # 60個

plt.subplot(1,2,1)      # 建立子圖表 1,2,1
plt.text(0.15,0.5,'subplot(1,2,1)',fontsize='16',c='b')
plt.subplot(2,2,2)      # 建立子圖表 2,2,2
plt.text(0.15,0.5,'subplot(2,2,2)',fontsize='16',c='m')
plt.subplot(2,2,4)      # 建立子圖表 2,2,4
plt.text(0.15,0.5,'subplot(2,2,4)',fontsize='16',c='m')

plt.show()

print("------------------------------------------------------------")  # 60個


N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                          # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2*np.pi, N)            # 建立 50 個點
y = np.sin(x)
fig = plt.figure()                          # 建立畫布物件
ax = fig.add_subplot()                      # 建立子圖(或稱軸物件)ax
ax.scatter(x, y, c=colors, marker='*')      # 繪製 sin
ax.set_title("建立畫布與軸物件,使用OO API繪圖", fontsize=16)

plt.show()

print("------------------------------------------------------------")  # 60個

fig, ax = plt.subplots(2, 2)            # 建立4個子圖
x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x**2)
ax[0, 0].plot(x, y,'b')                 # 子圖索引 0,0
ax[0, 0].set_title('子圖[0, 0]')
ax[0, 1].plot(x, y,'g')                 # 子圖索引 0,1
ax[0, 1].set_title('子圖[0, 1]')
ax[1, 0].plot(x, y,'m')                 # 子圖索引 1,0
ax[1, 0].set_title('子圖[1, 0]')
ax[1, 1].plot(x, y,'r')                 # 子圖索引 1,1
ax[1, 1].set_title('子圖[1, 1]') 
fig.suptitle("4個子圖的實作",fontsize=16) # 圖表主標題
plt.tight_layout()                      # 緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect('equal', 'box')
ax[1, 1].set_title('設定寬高比相同')
fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

# 繪製半徑 5 的圓
angle = np.linspace(0, 2*np.pi, 100)
fig, ax = plt.subplots(2, 2)    # 建立 2 x 2 子圖

ax[0, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 0].set_title('繪圓形, 看起來像橢圓')
ax[0, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[0, 1].axis('equal')
ax[0, 1].set_title('寬高比相同, 是圓形')
ax[1, 0].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 0].axis('equal')
ax[1, 0].set(xlim=(-5, 5), ylim=(-5, 5))
ax[1, 0].set_title('設定寬和高相同區間')
ax[1, 1].plot(5 * np.cos(angle), 5 * np.sin(angle))
ax[1, 1].set_aspect(2)
ax[1, 1].set_title('設定寬高比是2')
fig.tight_layout()

plt.show()

print("------------------------------------------------------------")  # 60個

ax = plt.subplot(projection='polar')
r = np.arange(0, 1, 0.001)
theta = 2 * 2*np.pi * r
ax.plot(theta, r, 'm', lw=3)
plt.title("極座標圖表",fontsize=16)
plt.tight_layout()      # 圖表標題可以緊縮佈局

plt.show()

print("------------------------------------------------------------")  # 60個

def f(x, y):
    return (1.2-x**2+y**5)*np.exp(-x**2-y**2)

x = np.linspace(-3.0, 3.0, 100)
y = np.linspace(-3.0, 3.0, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# 建立 2 個子圖
fig, ax = plt.subplots(1,2, figsize=(8,4))
# 繪製左圖 level 是預設
con = ax[0].contourf(X,Y,Z,cmap='Greens') # 填充輪廓圖
plt.colorbar(con,ax=ax[0])
oval = ax[0].contour(X,Y,Z,colors='b')    # 輪廓圖
ax[0].clabel(oval,colors='b')             # 增加高度標記
ax[0].set_title('指數函數等高圖level是預設',fontsize=16,color='b')
# 繪製右圖 level=12
ax[1].contourf(X,Y,Z,12,cmap='Greens')    # 填充輪廓圖
oval = ax[1].contour(X,Y,Z,12,colors='b') # 輪廓圖
ax[1].clabel(oval,colors='b')             # 增加高度標記
ax[1].set_title('指數函數等高圖level=12',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import axes3d

# 取得測試資料
X, Y, Z = axes3d.get_test_data(0.05)
# 建立 2 個子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
# 繪製曲線表面圖
ax[0].plot_surface(X, Y, Z, cmap="bwr")
ax[0].set_title('繪製曲線表面圖',fontsize=16,color='b')

# 繪製曲線框面圖
#ax = fig.add_subplot(111, projection='3d')
ax[1].plot_wireframe(X, Y, Z, color='g')
ax[1].set_title('繪製曲線框線圖',fontsize=16,color='b')

plt.show()

print("------------------------------------------------------------")  # 60個

z = np.linspace(0,1,300)        # z 軸值
x = z * np.sin(30*z)            # x 軸值
y = z * np.cos(30*z)            # y 軸值
colors = x + y                  # 色彩是沿 x + y 累增

# 建立 2 個子圖
fig,ax = plt.subplots(1,2,figsize=(8,4),subplot_kw={'projection':'3d'})
ax[0].scatter(x, y, z, c = colors)                  # 繪製左子圖
ax[1].scatter(x, y, z, c = colors, cmap='hsv')      # 繪製右子圖
ax[1].set_axis_off()            # 關閉軸

plt.show()

print("------------------------------------------------------------")  # 60個

def f1(x, y):                                # 左邊曲面函數
    return np.exp(-(0.5*X**2+0.5*Y**2))
def f2(x, y):                                # 右邊曲面函數
    return np.exp(-(0.1*X**2+0.1*Y**2))

N = 50
x = np.linspace(-5, 5, N)
y = np.linspace(-5, 5, N)
X, Y = np.meshgrid(x, y)            # 建立 X 和 Y 資料
np.random.seed(10)
c = np.random.rand(N, N)            # 取隨機色彩值
# 建立子圖
fig,ax = plt.subplots(1,3,figsize=(8,4),subplot_kw={'projection':'3d'})
# 左邊子圖乎叫 f1
sc = ax[0].scatter(X, Y, f1(X,Y), c=c, marker='o', cmap='hsv')
# 中間子圖乎叫 f2
sc = ax[1].scatter(X, Y, f2(X,Y), c=c, marker='o', cmap='hsv')
ax[1].set_axis_off()
# 右邊子圖乎叫 f2, 但是用不同的仰角和方位角
sc = ax[2].scatter(X, Y, f2(X,Y), c=c, marker='o', cmap='hsv')
ax[2].set_axis_off()
ax[2].view_init(60,-30)
ax[2].set_title(f"仰角={ax[2].elev},方位角={ax[2].azim}",color='b')

plt.show()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




