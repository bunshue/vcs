import numpy as np
import matplotlib.pyplot as plt



print('------------------------------------------------------------')	#60個


img = np.array([[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9 , 10, 11],
                [12, 13, 14, 15]])
                
plt.imshow(img, cmap='Blues')
plt.colorbar()
plt.show()


print('------------------------------------------------------------')	#60個

import matplotlib.image as img

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
pict = img.imread(filename)
plt.axis('off')
plt.title('牡丹亭', fontsize=24)
plt.imshow(pict)

plt.show()

print('------------------------------------------------------------')	#60個


import matplotlib.image as img

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

pict = img.imread(filename)
h, w, c = pict.shape
print(f"圖檔高度   = {h}")
print(f"圖檔寬度   = {w}")
print(f"圖檔通道数 = {c}")
plt.axis('off')
plt.title('牡丹亭', fontsize=24)
plt.imshow(pict)

plt.show()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


