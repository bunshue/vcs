import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image

plt.figure('影像處理1', figsize = (10, 6))

pil_im = Image.open('house.jpg')
plt.gray()

plt.subplot(121)
plt.title(u'原图')
plt.axis('off')
plt.imshow(pil_im)

pil_im = Image.open('house.jpg').convert('L')

plt.subplot(122)
plt.title(u'灰度图')
plt.axis('off')
plt.imshow(pil_im)

plt.show()


