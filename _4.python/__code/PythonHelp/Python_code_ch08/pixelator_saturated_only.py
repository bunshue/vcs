import cv2
from matplotlib import pyplot as plt

files = ['earth_west.png', 'earth_east.png']

def analyze_picture(filename):
    # 載入、縮放、顯示影像
    img_ini = cv2.imread(filename)
    pixelated = cv2.resize(img_ini, (3, 3), interpolation=cv2.INTER_AREA)
    img = cv2.resize(pixelated, (300, 300), interpolation=cv2.INTER_NEAREST)
    cv2.imshow('Pixelated {}'.format(filename), img)
    cv2.waitKey(2000)

    color_values = pixelated[1, 1]  # 選擇中央的像素塊
    print(color_values)

    # 製作圓餅圖
    labels = 'Blue', 'Green', 'Red'
    colors = ['blue', 'green', 'red']    
    fig, ax = plt.subplots(figsize=(3.5, 3.3))  # 尺寸單位為英吋
    _, _, autotexts = ax.pie(color_values,
                             labels=labels,
                             autopct='%1.1f%%',
                             colors=colors)
    for autotext in autotexts:
        autotext.set_color('white')
    plt.title('{} Saturated Center Pixel \n'.format(filename))
    plt.show()

filename = 'earth_west.png'
filename = 'C:/_git/vcs/_4.python/_data/ims01.bmp'

analyze_picture(filename)


