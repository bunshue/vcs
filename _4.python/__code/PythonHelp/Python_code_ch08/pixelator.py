import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

files = ['earth_west.png', 'earth_east.png']

for file in files:
    # 載入、縮放、顯示影像
    img_ini = cv.imread(file)
    pixelated = cv.resize(img_ini, (3, 3), interpolation=cv.INTER_AREA)
    img = cv.resize(pixelated, (300, 300), interpolation=cv.INTER_NEAREST)
    cv.imshow('Pixelated {}'.format(file), img)
    cv.waitKey(2000)

    # 取出各顏色 channel，並計算其平均
    b, g, r = cv.split(pixelated)
    color_aves = []
    for array in (b, g, r):
        color_aves.append(np.average(array))

    # 製作圓餅圖
    labels = 'Blue', 'Green', 'Red'
    colors = ['blue', 'green', 'red']    
    fig, ax = plt.subplots(figsize=(3.5, 3.3))  # 尺寸單位為英吋
    _, _, autotexts = ax.pie(color_aves,
                             labels=labels,
                             autopct='%1.1f%%',
                             colors=colors)
    for autotext in autotexts:
        autotext.set_color('white')
    plt.title('{}\n'.format(file))
    
plt.show()
