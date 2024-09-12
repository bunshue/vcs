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


#Unsupervised Learning in Satellite Imagery using Python
# 非監督的



print("------------------------------------------------------------")  # 60個

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
     

print(f'Height: {arr_st.shape[1]}\nWidth: {arr_st.shape[2]}\nBands: {arr_st.shape[0]}')
     

#Visualize Data
#Bands

ep.plot_bands(arr_st, cmap = 'gist_earth', figsize = (20, 12), cols = 6, cbar = False)
plt.show()
    


print("------------------------------------------------------------")  # 60個


#RGB Composite Image

rgb = ep.plot_rgb(arr_st, 
                  rgb=(3,2,1), 
                  figsize=(8, 10), 
                  # title='RGB Composite Image'
                  )

plt.show()
     


print("------------------------------------------------------------")  # 60個

ep.plot_rgb(
    arr_st,
    rgb=(3, 2, 1),
    stretch=True,
    str_clip=0.2,
    figsize=(8, 10),
    # title="RGB Composite Image with Stretch Applied",
)

plt.show()

print("------------------------------------------------------------")  # 60個

#Data Distribution of Bands

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


#Preprocessing

x = np.moveaxis(arr_st, 0, -1)
print(x.shape)
     
#(954, 298, 12)


x.reshape(-1, 12).shape, 954*298

#((284292, 12), 284292)

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

X_data = x.reshape(-1, 12)

scaler = StandardScaler().fit(X_data)

X_scaled = scaler.transform(X_data)

print(X_scaled.shape)

#(284292, 12)

print("------------------------------------------------------------")  # 60個

#Principal Component Analysis (PCA)

pca = PCA(n_components = 4)

pca.fit(X_scaled)

data = pca.transform(X_scaled)
     

print(data.shape)
     
#(284292, 4)

print(pca.explained_variance_ratio_)
     
#array([0.55778198, 0.37521242, 0.0484222 , 0.00637526])

print(np.sum(pca.explained_variance_ratio_))
     
#0.9877918653349008

print("------------------------------------------------------------")  # 60個

#Visualize Bands after PCA

ep.plot_bands(np.moveaxis(data.reshape((954, 298, data.shape[1])), -1, 0),
              cmap = 'gist_earth',
              cols = 4,
              title = [f'PC-{i}' for i in range(1,5)])

plt.show()
     
print("------------------------------------------------------------")  # 60個

#k - Means

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters = 6, random_state = 11)

kmeans.fit(data)

     
""" out
KMeans(algorithm='auto', copy_x=True, init='k-means++', max_iter=300,
       n_clusters=6, n_init=10, n_jobs=None, precompute_distances='auto',
       random_state=11, tol=0.0001, verbose=0)
"""

labels = kmeans.predict(data)
     

np.unique(labels)
     

#array([0, 1, 2, 3, 4, 5], dtype=int32)

print("------------------------------------------------------------")  # 60個

#Visualize Clusters

ep.plot_bands(labels.reshape(954, 298), cmap=ListedColormap(['darkgreen', 'green', 'black', '#CA6F1E', 'navy', 'forestgreen']))
plt.show()
     
print("------------------------------------------------------------")  # 60個

#Interactive plot using Plotly

import plotly.express as px

fig = px.imshow(labels.reshape(954, 298), 
          color_continuous_scale = ['darkgreen', 'green', 'black', '#CA6F1E', 'navy', 'forestgreen'])

fig.update_xaxes(showticklabels=False)

fig.update_yaxes(showticklabels=False)

fig.update_layout(
    autosize=False,
    width=500,
    height=1000,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    ),
    # paper_bgcolor="LightSteelBlue",
)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

