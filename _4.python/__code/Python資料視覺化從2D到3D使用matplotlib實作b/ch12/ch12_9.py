# ch12_9.py
import matplotlib.pyplot as plt
import matplotlib.image as img

macau = img.imread('macau.jpg')             # 讀取原始圖像
plt.figure()
for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2*(i-1)                       # 調整色彩明暗參數
    plt.axis('off')                         # 關閉顯示軸刻度
    plt.title(f'x = {x:2.1f}',color='b')    # 藍色浮動值標題    
    src = macau * x                         # 處理像素值
    intmacau = src.astype(int)              # 將元素值轉成整數
    plt.imshow(intmacau)                    # 顯示圖像
plt.show()


