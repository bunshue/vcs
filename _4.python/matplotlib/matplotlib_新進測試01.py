
'''

#盒鬚圖（Box plot）
import numpy as np
import matplotlib.pyplot as plt

normal_samples = np.random.normal(size = 100000) # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數

plt.boxplot(normal_samples)
plt.show()





#存圖
import numpy as np
import matplotlib.pyplot as plt
normal_samples = np.random.normal(size = 100000) # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
plt.hist(normal_samples)
plt.savefig(fname = "my_hist.png", format = "png")



#plot + bar
import matplotlib.pyplot as plt
#import matplotlib.gridspec as gridspec
import numpy as np

x = np.linspace(0, 6.28, 10)
y = np.sin(x * 2)
y2 = np.sin(x * 2) * np.sin(x * 2) *10

fig = plt.figure(figsize=(12, 8))
#gs = gridspec.GridSpec(4, 1, figure=fig)
ax = fig.add_subplot()

ax.plot(x, y, marker="", alpha=0.8)

ax.grid(20)
axx = ax.twinx()
axx.bar(
	x, y2,
	alpha=0.2,
	label="hold_volume",
	color="pink",
)

plt.show()
'''


'''



import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['savefig.facecolor'] = "0.8"

arr = np.arange(100).reshape((10, 10))

plt.close('all')
fig = plt.figure(figsize=(5, 4))

ax = plt.subplot()
im = ax.imshow(arr, interpolation="none")

plt.tight_layout()

plt.show()



plt.close('all')
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

plt.colorbar(im)

plt.tight_layout()
plt.show()


from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.close('all')
arr = np.arange(100).reshape((10, 10))
fig = plt.figure(figsize=(4, 4))
im = plt.imshow(arr, interpolation="none")

divider = make_axes_locatable(plt.gca())
cax = divider.append_axes("right", "5%", pad="3%")
plt.colorbar(im, cax=cax)

plt.tight_layout()

plt.show()

#foldername = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
foldername = 'C:/_git/vcs/_1.data/______test_files1'

import numpy as np
import matplotlib.pyplot as plt
import glob,cv2

files = glob.glob(foldername + "/*.jpg")  #建立測試資料
test_feature=[]
for file in files:
    print(file)
    img=cv2.imread(file)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)

print(test_feature)

print('畫多張圖')
import matplotlib.pyplot as plt

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



