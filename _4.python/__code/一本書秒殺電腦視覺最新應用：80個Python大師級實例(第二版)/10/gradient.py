import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,color,data,filter

image =color.rgb2gray(data.camera())

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

denoised = filter.rank.median(image, morphology.disk(2)) #过滤噪声
#将梯度值低于10的作为开始标记点
markers = filter.rank.gradient(denoised, morphology.disk(5))<10
markers = ndi.label(markers)[0]
gradient = filter.rank.gradient(denoised, morphology.disk(2)) #计算梯度
labels =morphology.watershed(gradient, markers, mask=image) #基于梯度的分水岭算法
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes
ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("原始图像")
ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
ax1.set_title("梯度")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("标记")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("分割")
for ax in axes:
    ax.axis('off')
fig.tight_layout()
plt.show()
