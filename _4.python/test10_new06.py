import numpy as np
import matplotlib.pyplot as plt


print('------------------------------------------------------------')	#60個

N = 500

plt.show()

#randn 由標準常態分布隨機取值
#還可以取好高級的亂數, 從平均數 0, 標準差 1 的常態分佈中取出 n 個數字。

x = np.random.randn(N)
y = np.random.randn(N)
print('max :', x.max())
print('min :', x.mean())
print('avg :', x.min())
print('std :', x.std())

plt.scatter(x, y, s=50, color='r')#s是大小

#rand 隨機取值
x = np.random.rand(N)
y = np.random.rand(N)
print('max :', x.max())
print('min :', x.mean())
print('avg :', x.min())
print('std :', x.std())

plt.scatter(x, y, s=50, color='g')#s是大小
plt.scatter(x, y, s=50, color=(0, 1, 0))  #s是大小 # 綠色

plt.show()

print('------------------------------------------------------------')	#60個


plt.scatter(np.random.randn(100), np.random.randn(100))

plt.show()


print('------------------------------------------------------------')	#60個


'''
xpt = list(range(1,11))        # 建立1-100序列x座標點

plt.plot(squares, lw=10)       # 串列squares數據是y軸的值, 線條寬度是10
plt.tick_params(axis='both', labelsize=12, color='red')

plt.plot(seq, data1, 'g--', seq, data2, 'r-.', seq, data3, 'y:', seq, data4, 'k.')   
plt.plot(seq, data1, '-*', seq, data2, '-o', seq, data3, '-^', seq, data4, '-s')   
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

'''

'''
print('------------------------------------------------------------')	#60個
seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度
plt.plot(seq, Benz, '-*', label='Benz')
plt.plot(seq, BMW, '-o', label='BMW')
plt.plot(seq, Lexus, '-^', label='Lexus')


plt.title("Sales Report", fontsize=24)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Number of Sales", fontsize=14)


seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度




print('------------------------------------------------------------')	#60個
plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')


plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)
'''

print('------------------------------------------------------------')	#60個

'''
plt.plot(x, np.sin(x), c='#e63946', lw=3)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)
plt.scatter(x, np.random.randn(100), c='#daa73e', s=50, alpha=0.5)
plt.bar(range(10), np.random.randint(1,30,10), fc='#e55934')

plt.plot(x,y,'r-.')
'''


print('------------------------------------------------------------')	#60個
plt.plot(x, y, marker='o')
plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)
plt.show()

print('------------------------------------------------------------')	#60個

xpt = np.linspace(0, 5, 50)                            # 建立含500個元素的陣列
ypt = 1 - 0.5*np.abs(xpt-2)                             # y陣列的變化
  
plt.scatter(xpt, ypt, s=50, c=ypt, cmap='hsv')          # 色彩隨y軸值變化
plt.show()


print('------------------------------------------------------------')	#60個

xpt = np.linspace(0, 5, 500)                            # 建立含500個元素的陣列
ypt = 1 - 0.5*np.abs(xpt-2)                             # y陣列的變化
 
plt.scatter(xpt, ypt, s=50, c=xpt, cmap='hsv')          # 色彩隨x軸值變化
plt.show()

print('------------------------------------------------------------')	#60個

x = np.arange(50)
y = x
t = x
plt.scatter(x, y, c=t, cmap='rainbow')
plt.show()

print('------------------------------------------------------------')	#60個



