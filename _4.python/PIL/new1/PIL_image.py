from PIL import Image
from pylab import *

#plt.rcParams['font.sans-serif'] =['SimHei']  #显示中文标签
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

figure()
pil_im = Image.open('house.jpg')
gray()
subplot(121)
title(u'原图')
axis('off')
imshow(pil_im)
pil_im = Image.open('house.jpg').convert('L')
subplot(122)
title(u'灰度图')
axis('off')
imshow(pil_im)

show()
