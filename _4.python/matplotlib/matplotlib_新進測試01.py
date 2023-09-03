import sys

import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個


#foldername = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
foldername = 'C:/_git/vcs/_1.data/______test_files1'


'''
import glob,cv2

files = glob.glob(foldername + "/*.jpg")  #建立測試資料
test_feature=[]
for file in files:
    print(file)
    img = cv2.imread(file)	#讀取本機圖片
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)

print(test_feature)

print('畫多張圖')


plt.gcf().set_size_inches(12, 14)

num=25

if num>25: num=25
for i in range(num):
    ax=plt.subplot(5,5, i+1)
    #ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
    title = 'label = ' + str(i)
    ax.set_title(title,fontsize=12)  # X,Y軸不顯示刻度
    ax.set_xticks([]);ax.set_yticks([])        
plt.show()


'''

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


N = 10

x2 = np.arange(N)
#y2 = x2 * np.random.randn(N)
y2 = np.random.randn(N)
y2 = x2

plt.scatter(x2, y2)
plt.show()

plt.bar(x2, y2)
plt.show()


plt.plot(x2, y2)
plt.show()


#箱形圖  便於確認資料分布的視覺化方法
plt.boxplot(y2)
plt.show()

import sys
sys.exit()


'''
print('------------------------------------------------------------')	#60個
                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()
'''

print('------------------------------------------------------------')	#60個



'''
X = np.random.randn(300)
Y = np.random.randn(300)
plt.scatter(X, Y)
'''


plt.plot(np.random.randn(20))
plt.plot(range(20), np.random.randn(20))

plt.show()




print('------------------------------------------------------------')	#60個

'''
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
'''

print('------------------------------------------------------------')	#60個



x = np.linspace(-5, 5, 1000)
y = np.sin(x) / (x**2+1)

plt.plot(x,y,lw=5)
plt.plot(x,np.cos(x))
#plt.xticks(np.arange(-5,6))



#把這個函數大於 0 的地方標示出來。
y = np.sinc(x)
plt.plot(x,y)
plt.plot(x[y>0], y[y>0], 'o')




print('------------------------------------------------------------')	#60個




'''
print('------------------------------------------------------------')	#60個
                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()
'''

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個







