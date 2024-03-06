'''

PIL 圖片相關的處理

各種convert


'''

import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image
from matplotlib import patches
import matplotlib.pyplot as plt

#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'


image1 = Image.open(filename)
  
image = Image.open(filename)
image_1 = image.convert('1')	#轉換成二值化圖像

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image_1)

plt.show()

print('------------------------------------------------------------')	#60個

img = Image.open("data/img01.jpg")
imggray = img.convert('L') #轉換為灰階

print("------------------------------------------------------------")  # 60個

img = Image.open("data/img01.jpg")
w,h=img.size #320 240
img = img.convert('L')  #先轉換為灰階

for i in range(w):  #i為每一列
    for j in range(h):  #j為每一行
        if img.getpixel((i,j)) <100:  
            img.putpixel((i,j),(0))   #設為黑色
        else:
            img.putpixel((i,j),(255)) #設為白色

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個





