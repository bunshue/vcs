# ch17_28.py
from PIL import Image
import os

def batch_resize_images(input_folder, output_folder, size=(300, 300)):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷輸入資料夾中的所有影像檔案
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png')):
            # 打開影像
            img = Image.open(os.path.join(input_folder, filename))
            # 調整影像尺寸
            img = img.resize(size, Image.ANTIALIAS)
            # 保存調整尺寸後的影像到輸出資料夾
            img.save(os.path.join(output_folder, filename))

# 假設有一個包含原始圖片的資料夾 'input_images' 和
# 一個用於存放調整後圖片的資料夾 'output_images'
input_folder = 'input_images'
output_folder = 'output_images'

# 呼叫函數，將所有圖片調整為300x300大小
batch_resize_images(input_folder, output_folder)


