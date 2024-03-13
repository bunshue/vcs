"""
PIL 新進

"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

print('PIL模糊處理 GaussianBlur')
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'

guido_img = Image.open(open(filename, 'rb'))
guido2_img = guido_img.filter(ImageFilter.GaussianBlur)
guido2_img.save(open('tmp_elephant_blur.jpg', 'wb'))


print('二值化')
img1 = Image.open(open(filename, 'rb'))
img2 = img1.point(lambda x: 0 if x < 128 else 255)

img2.save(open('tmp_elephant_binary.png', 'wb'))



print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

