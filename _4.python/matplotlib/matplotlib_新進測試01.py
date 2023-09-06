import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

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

N = 10

x2 = np.arange(N)
#y2 = x2 * np.random.randn(N)
y2 = np.random.randn(N)
y2 = x2

plt.scatter(x2, y2)
#plt.show()

plt.bar(x2, y2)
#plt.show()


plt.plot(x2, y2)
plt.show()


#箱形圖  便於確認資料分布的視覺化方法
plt.boxplot(y2)

plt.show()




print('------------------------------------------------------------')	#60個

'''
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
'''



print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個




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


print('------------------------------------------------------------')	#60個

plt.plot(x, y, marker='o')
plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)

plt.show()

'''
print('------------------------------------------------------------')	#60個


