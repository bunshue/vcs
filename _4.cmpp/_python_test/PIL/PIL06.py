import numpy as np
import torchvision.transforms as transforms
from PIL import Image

filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample.jpg'

'''
image = Image.open(filename)    #读取的是RGB格式的图片

# 输出维度
print("RGB图像的维度：", np.array(image).shape)
image.show()    # 显示原图

# RGB转换我灰度图像
image_transforms = transforms.Compose([
transforms.Grayscale(1)
])

image = image_transforms(image)
# 输出灰度图像的维度
print("灰度图像维度： ", np.array(image).shape)
# 显示灰度图像
image.show()
'''

#filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/sample.jpg'
filename = 'C:/______test_files/bug.bmp'
image = Image.open(filename)    #读取的是RGB格式的图片
image_dim_len = len(np.array(image).shape)
#image.show()
print("The dim of Image: ", image_dim_len)

print("RGB图像的维度：", np.array(image).shape)

print('OK')
