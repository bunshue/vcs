# plot 集合

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_1.py

# ch20_1.py
import matplotlib.pyplot as plt

y = [1, 3, 5, 7, 6, 4, 2]
plt.stem(y)
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_2.py

# ch20_2.py
import matplotlib.pyplot as plt
import numpy as np

pts = 15
x = np.linspace(1, 2*np.pi, pts)
y = np.random.randn(pts)
plt.stem(x,y)
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_3.py

# ch20_3.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,linefmt='--')
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_4.py

# ch20_4.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,linefmt='C2-.')
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_5.py

# ch20_5.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,linefmt='m',markerfmt='gD')
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_6.py

# ch20_6.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,linefmt='m',markerfmt='gD',basefmt='b-')
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_7.py

# ch20_7.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,linefmt='m',markerfmt='gD',basefmt='b-',label='stem()')
plt.legend()
plt.show()


      

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料視覺化從2D到3D使用matplotlib實作a\ch20\ch20_8.py

# ch20_8.py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
pts = 30
x = np.linspace(1, 2*np.pi, pts)
y = np.exp(np.sin(x))
plt.stem(x,y,markerfmt='g*',basefmt='b-',label='stem()',bottom=1.2)
plt.legend()
plt.show()


      

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


