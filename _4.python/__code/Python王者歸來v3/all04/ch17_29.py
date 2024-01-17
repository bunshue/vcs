# ch17_29.py
from PIL import Image
import os

def batch_convert_images(directory, target_format='.jpg'):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            img = Image.open(path)
            rgb_im = img.convert('RGB')  # 轉換為RGB模式以便保存為JPEG
            rgb_im.save(path.replace('.png', target_format), quality=95)

# 呼叫批次更改函數
batch_convert_images('images_directory')


