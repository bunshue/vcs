'''
import matplotlib.pyplot as plt
import matplotlib.image as img
from PIL import Image, ImageEnhance

filename = 'C:/______test_files/_emgu/lena.jpg'

plt.figure(figsize=(10,10))    # 改變圖表尺寸 單位是英吋

image1 = Image.open(filename)              # 開啟圖片
enhancer = ImageEnhance.Brightness(image1)   # 建立調整亮度的方法

# 顯示原圖
plt.subplot(221)                   # 建立 2x2 子圖表的左上方圖表
plt.imshow(image1)                  # 在子圖表中繪製圖片

# 顯示亮度 x0.5 的圖片
image2 = enhancer.enhance(0.5)  # 顯示亮度 x0.5 的圖片
plt.subplot(222)                   # 建立 2x2 子圖表的右上方圖表
plt.imshow(image2)                  # 在子圖表中繪製圖片

plt.subplot(223)                   # 建立 2x2 子圖表的左下方圖表
image3 = enhancer.enhance(1.5)  # 顯示亮度 x1.5 的圖片
plt.imshow(image3)                  # 在子圖表中繪製圖片

plt.subplot(224)                   # 建立 2x2 子圖表的右下方圖表
image4 = enhancer.enhance(3)    # 顯示亮度 x3 的圖片
plt.imshow(image4)                  # 在子圖表中繪製圖片

plt.show()


'''


import tkinter as tk

root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

#像是richTextBox
text = tk.Text(root)  # 放入多行輸入框
text.pack()

root.mainloop()
