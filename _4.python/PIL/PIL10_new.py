'''
PIL 新進

'''

import numpy as np
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

'''
from PIL import Image,ImageDraw
image = Image.open("captcha.png").convert("L")	#轉換成灰階圖像
'''


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


#PIL之基本設定


''' not ready
from PIL import Image, ImageDraw, ImageFont

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

im = Image.open(filename1)
im.save(filename1 + '.png', 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename1 + '.png')



filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'
image3 = image1.resize((100, 500), Image.ANTIALIAS)
image3.save(filename2)


im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename3)


#im.show()  #顯示圖片



image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#image.show()


print('使用plt顯示圖片')
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()


#PIL保存圖片的方式，調用方法 Image.save() 即可
print('影像存圖')
print('將二值畫圖像存圖')
image_1.save('image_1.png')


#儲存過濾過的圖形到新檔案
im_sharp.save(filename2, 'JPEG')
print("儲存過濾過的圖形, 檔案 : ", filename2);



#im.show()  #顯示圖片
im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：' + filename)

#im.show()

filename = 'C:/_git/vcs/_1.data/______test_files2/tmppic_new'
im.save(filename+'.png', 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')





#im.show()  #顯示圖片

im.save(filename2, 'PNG')
print('新檔存圖, 已寫入檔案：' + filename2)

#im.show()  #顯示圖片

im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename3)


filename = 'C:/_git/vcs/_1.data/______test_files2/pil_test01.png'
img.save(filename)
print('已寫入檔案：' + filename)



im.save(filename2, 'PNG')
print('舊檔存圖, 已寫入檔案：' + filename2)

im.save(filename2, 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename2)

'''

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
from PIL import Image
im = Image.open(filename)
print(im.format, im.size, im.mode)
im.close()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image
im = Image.open(filename)
smaller = im.resize((640,480))
smaller.show()
smaller.save("new_pic.jpg")
im.close()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('完成')
