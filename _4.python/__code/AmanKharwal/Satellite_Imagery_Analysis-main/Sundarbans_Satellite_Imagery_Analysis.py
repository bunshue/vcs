"""




"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個


#Sundarbans Satellite Imagery Analysis using Python
"""
pip install earthpy
pip install gdal

"""

from glob import glob

import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

import rasterio as rio
from rasterio.plot import plotting_extent
from rasterio.plot import show
from rasterio.plot import reshape_as_raster, reshape_as_image

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

import plotly.graph_objects as go

np.seterr(divide='ignore', invalid='ignore')


print("------------------------------------------------------------")  # 60個

S_sentinel_bands = glob("Data/sundarbans_data/*B?*.tiff")
S_sentinel_bands.sort()
print(S_sentinel_bands)




l = []
for i in S_sentinel_bands:
  with rio.open(i, 'r') as f:
    l.append(f.read(1))

     

arr_st = np.stack(l)
     

print(arr_st.shape)
     

#(12, 954, 298)


ep.plot_bands(arr_st, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)
plt.show()
     

print("------------------------------------------------------------")  # 60個
rgb = ep.plot_rgb(arr_st, 
                  rgb=(3,2,1), 
                  figsize=(10, 16), 
                  # title='RGB Composite Image'
                  )

plt.show()



print("------------------------------------------------------------")  # 60個
ep.plot_rgb(
    arr_st,
    rgb=(3, 2, 1),
    stretch=True,
    str_clip=0.2,
    figsize=(10, 16),
    # title="RGB Composite Image with Stretch Applied",
)

plt.show()

print("------------------------------------------------------------")  # 60個

colors = ['tomato', 'navy', 'MediumSpringGreen', 'lightblue', 'orange', 'blue',
          'maroon', 'purple', 'yellow', 'olive', 'brown', 'cyan']

ep.hist(arr_st, 
         colors = colors,
        title=[f'Band-{i}' for i in range(1, 13)], 
        cols=3, 
        alpha=0.5, 
        figsize = (12, 10)
        )

plt.show()

print("------------------------------------------------------------")  # 60個

"""
Vegetation and soils indices
Normalized Difference Vegetation Index (NDVI)

NDVI = ((NIR - Red)/(NIR + Red))

    NIR = pixel values from the near-infrared band
    Red = pixel values from the red band
"""

ndvi = es.normalized_diff(arr_st[7], arr_st[3])

ep.plot_bands(ndvi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     

"""
Soil-Adjusted Vegetation Index (SAVI)

SAVI = ((NIR - Red) / (NIR + Red + L)) x (1 + L)

    NIR = pixel values from the near infrared band
    Red = pixel values from the near red band
    L = amount of green vegetation cover
"""

L = 0.5

savi = ((arr_st[7] - arr_st[3]) / (arr_st[7] + arr_st[3] + L)) * (1 + L)
     

ep.plot_bands(savi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     

"""
Visible Atmospherically Resistant Index (VARI)

VARI = (Green - Red)/ (Green + Red - Blue)

    Green = pixel values from the green band
    Red= pixel values from the red band
    Blue = pixel values from the blue band
"""

vari = (arr_st[2] - arr_st[3])/ (arr_st[2] + arr_st[3] - arr_st[1])

ep.plot_bands(vari, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     

#Distribution of NDVI, SAVI, and VARI pixel values

ep.hist(np.stack([ndvi, savi, vari]), 
        alpha=0.5,
        cols=3, 
        figsize=(20, 5),
        title = ['NDVI', 'SAVI', 'VARI'],
        colors = ['mediumspringgreen', 'tomato', 'navy'])
plt.show()
     


print("------------------------------------------------------------")  # 60個

"""
Water Indices
Modified Normalized Difference Water Index (MNDWI)

MNDWI = (Green - SWIR) / (Green + SWIR)

    Green = pixel values from the green band
    SWIR = pixel values from the short-wave infrared band
"""

mndwi = es.normalized_diff(arr_st[2], arr_st[10])
     
ep.plot_bands(mndwi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     
print("------------------------------------------------------------")  # 60個
"""
Normalized Difference Moisture Index (NDMI)

NDMI = (NIR - SWIR1)/(NIR + SWIR1)

    NIR = pixel values from the near infrared band
    SWIR1 = pixel values from the short-wave infrared 1 band

"""

ndmi = es.normalized_diff(arr_st[7], arr_st[10])

ep.plot_bands(ndmi, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     

print("------------------------------------------------------------")  # 60個

"""
Geology Indices
Clay Minerals

Clay Minerals Ratio = SWIR1 / SWIR2

    SWIR1 = pixel values from the short-wave infrared 1 band
    SWIR2 = pixel values from the short-wave infrared 2 band
"""

cmr = np.divide(arr_st[10], arr_st[11])
     

ep.plot_bands(cmr, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     



print("------------------------------------------------------------")  # 60個


"""
Ferrous Minerals

Ferrous Minerals Ratio = SWIR / NIR

    SWIR= pixel values from the short-wave infrared band
    NIR = pixel values from the near infrared band

"""

fmr = np.divide(arr_st[10], arr_st[7])
     

ep.plot_bands(fmr, cmap="RdYlGn", cols=1, vmin=-1, vmax=1, figsize=(10, 14))

plt.show()
     


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

