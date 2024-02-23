# python 3+ 請複製以下在 terminal 中執行
# pip3 install matplotlib

# python 2+ 請複製以下在 terminal 中執行
# pip install matplotlib

import numpy as np
from matplotlib import pyplot as plt 
 
x = np.arange(1,11, dtype=int) 
y =  2 * x
plt.title("demo") 
plt.xlabel("x") 
plt.ylabel("y") 
plt.plot(x,y) 
plt.show()