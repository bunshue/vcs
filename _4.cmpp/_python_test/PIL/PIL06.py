import numpy as np
import torchvision.transforms as transforms
from PIL import Image

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample.jpg'

'''
image = Image.open(filename)    #讀取的是RGB格式的圖片

# 輸出維度
print("RGB圖像的維度：", np.array(image).shape)
image.show()    # 顯示原圖

# RGB轉換成灰階圖像
image_transforms = transforms.Compose([
transforms.Grayscale(1)
])

image = image_transforms(image)
# 輸出灰度圖像的維度
print("灰度圖像維度： ", np.array(image).shape)
# 顯示灰度圖像
image.show()
'''

#filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample.jpg'
filename = 'C:/______test_files/bug.bmp'
image = Image.open(filename)    #讀取的是RGB格式的圖片
image_dim_len = len(np.array(image).shape)
#image.show()
print("The dim of Image: ", image_dim_len)

print("RGB圖像的維度：", np.array(image).shape)

print('OK')
