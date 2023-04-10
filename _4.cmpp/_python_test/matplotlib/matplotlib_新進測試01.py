'''
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

cyl = [6 ,6 ,4 ,6 ,8 ,6 ,8 ,4 ,4 ,6 ,6 ,8 ,8 ,8 ,8 ,8 ,8 ,4 ,4 ,4 ,4 ,8 ,8 ,8 ,8 ,4 ,4 ,4 ,8 ,6 ,8 ,4]

labels, values = zip(*Counter(cyl).items())
indexes = np.arange(len(values))

plt.bar(indexes, values, width = 0.5)
plt.xticks(indexes, labels)
plt.show()


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

'''

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

'''
