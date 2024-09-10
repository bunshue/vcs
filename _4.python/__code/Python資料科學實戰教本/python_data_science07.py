"""
Python資料科學實戰教本



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

a = np.array([1, 2, 3, 4, 5]) 
b = np.array((1, 2, 3, 4, 5)) 
print(type(a), type(b))  
print("---------------------------")        
print(a[0], a[1], a[2], a[3], a[4])
print("---------------------------")
b[0] = 5    
print(b)
print("---------------------------")
b[4] = 0
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6]])
print(a[0, 0], a[0, 1], a[0, 2])
print(a[1, 0], a[1, 1], a[1, 2])
print("---------------------------")
a[0, 0] = 6
a[1, 2] = 1
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5], int) 
b = np.array((1, 2, 3, 4, 5), dtype=float) 
print(a)
print("---------------------------")
print(b)    

print("------------------------------------------------------------")  # 60個

a = np.arange(5)
print(a)
print("---------------------------")
b = np.arange(1, 6, 2)
print(b) 
print("===========================")
c = np.zeros(2) 
print(c)
print("---------------------------")
d = np.zeros((2,2)) 
print(d)           
print("===========================")
e = np.ones(2) 
print(e)
print("---------------------------")
f = np.ones((2,2)) 
print(f)         
print("===========================")
g = np.full(2, 7)
print(g)
print("---------------------------")
h = np.full((2,2), 7)
print(h)  

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6]])
b = np.zeros_like(a)
print(b)
print("===========================")
c = np.ones_like(a)
print(c)
print("===========================")
d = np.eye(3)  
print(d)
print("---------------------------")
e = np.eye(3, k=1)
print(e)
print("===========================")    
f = np.random.rand(3)
print(f)
print("---------------------------")
g = np.random.rand(3,3)
print(g)   

print("------------------------------------------------------------")  # 60個

a = np.arange(16)
print(a)
print("---------------------------")
b = a.reshape((4, 4))
print(b)
print("===========================")
c = np.array(range(10), float)
print(c)
print("---------------------------")
d = c.reshape((5, 2))
print(d)

print("------------------------------------------------------------")  # 60個

a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])
 
print(type(a))
print(a.dtype)
print(a.size)
print(a.shape)
print(a.itemsize)
print(a.ndim)
print(a.nbytes)  

print("------------------------------------------------------------")  # 60個

a = np.array([[1, 2], [3, 4], [5, 6]])
for ele in a:
    print(ele)

print("---------------------------")
for ele in a:
    for item in ele:
        print(str(item) + " ", end="")

print("------------------------------------------------------------")  # 60個

a = np.arange(10)
outputfile = "Example.npy"
with open(outputfile, 'wb') as fp:
    np.save(fp, a)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6]])
outputfile = "Example.out"
np.savetxt(outputfile, a, delimiter=',')

print("------------------------------------------------------------")  # 60個

outputfile = "Example.npy"
with open(outputfile, 'rb') as fp:
    a = np.load(fp)
print(a)

print("------------------------------------------------------------")  # 60個

outputfile = "Example.out"
a = np.loadtxt(outputfile, delimiter=',')
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3]) 
print("a=" + str(a))
s = 5 
print("s=" + str(s))
b = a + s       
print("a+s=" + str(b))    
b = a - s       
print("a-s=" + str(b))   
b = a * s       
print("a*s=" + str(b))  
b = a / s       
print("a/s=" + str(b))  

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3]) 
print("a=" + str(a))
s = 5 
print("s=" + str(s))
b = np.add(a, s)       
print("np.add(a,s)=" + str(b))    
b = np.subtract(a, s)       
print("np.subtract(a,s)=" + str(b))   
b = np.multiply(a, s)       
print("np.multiply(a,s)=" + str(b))  
b = np.divide(a, s)       
print("np.divide(a,s)=" + str(b))  

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3]) 
print("a=" + str(a))
s = np.array([4, 5, 6])  
print("s=" + str(s))
b = a + s       
print("a+s=" + str(b))    
b = a - s       
print("a-s=" + str(b))   
b = a * s       
print("a*s=" + str(b))  
b = a / s       
print("a/s=" + str(b))  

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3]) 
print("c=" + str(a))
s = np.array([4, 5, 6])  
print("s=" + str(s))
b = np.add(a, s)       
print("np.add(a,s)=" + str(b))    
b = np.subtract(a, s)       
print("np.subtract(a,s)=" + str(b))   
b = np.multiply(a, s)       
print("np.multiply(a,s)=" + str(b))  
b = np.divide(a, s)       
print("np.divide(a,s)=" + str(b))  

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3]) 
print("a=" + str(a))
s = np.array([4, 5, 6])  
print("s=" + str(s))
b = a.dot(s)       
print("a.dot(s)=" + str(b))    

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("a=" + str(a))

b = a[1:3]     # 索引 1,2
print("a[1:3]=" + str(b))
b = a[:4]      # 索引 0,1,2,3
print("a[:4]=" + str(b))
b = a[3:]      # 索引 3,4,5,6,7,8
print("a[3:]=" + str(b))
b = a[2:9:3]   # 索引 2,5,8
print("a[2:9:3]=" + str(b))
b = a[::2]     # 索引 0,2,4,6,8
print("a[::2]=" + str(b))
b = a[::-1]    # 索引 8,7,6,5,4,3,2,1,0
print("a[::-1]=" + str(b))
b = a[2:-2]    # 索引 8,7,6,5,4,3,2,1,0
print("a[2:-2]=" + str(b))

print("------------------------------------------------------------")  # 60個

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("a=" + str(a))

print(a[0], a[2], a[-1])  # 索引 0,2,最後1個 
b = a[[1, 3, 5, 7]]       # 索引 1,3,5,7
print("a[[1,3,5,7]]=" + str(b))
b = a[range(6)]           # 索引 0,1,2,3,4,5
print("a[range(6)]=" + str(b))
a[[2, 6]] = 10            # 同時更改多個索引值
print("a[[2,6]]=10->" + str(a))

print("------------------------------------------------------------")  # 60個

a = np.array([14,8,10,11,6,3,18,13,12,9])
print("a=" + str(a))
mask = (a % 3 == 0)        # 建立布林值陣列
print("mask=" + str(mask))
b = a[mask]                # 使用布林值陣列取出值
print("a[mask]=" + str(b))
a[a % 3 == 0] = -1         # 同時更改多個True索引
print("a[a%3==0]=-1->" + str(a))

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6]])
print("a=")
print(a)
s = 5 
print("s=" + str(s))
b = a + s       
print("a+s=")
print(b)    
b = a - s       
print("a-s=")
print(b)   
b = a * s       
print("a*s=")
print(b)  
b = a / s       
print("a/s=")
print(b)  

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6]])
print("a=")
print(a)
s = 5 
print("s=" + str(s))
b = np.add(a, s)       
print("np.add(a,s)=")
print(b)    
b = np.subtract(a, s)       
print("np.subtract(a,s)=")
print(b)   
b = np.multiply(a, s)       
print("np.multiply(a,s)=")
print(b)  
b = np.divide(a, s)       
print("np.divide(a,s)=")
print(b)  

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2],[3,4]])
print("a=")
print(a)
s = np.array([[5,6],[7,8]])
print("s=")
print(s)
b = a + s       
print("a+s=")
print(b)    
b = a - s       
print("a-s=")
print(b)   
b = a * s       
print("a*s=")
print(b)  
b = a / s       
print("a/s=")
print(b)  

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2],[3,4]])
print("a=")
print(a)
s = np.array([[5,6],[7,8]])
print("s=")
print(s)
b = np.add(a, s)       
print("np.add(a,s)=")
print(b)    
b = np.subtract(a, s)       
print("np.subtract(a,s)=")
print(b)   
b = np.multiply(a, s)       
print("np.multiply(a,s)=")
print(b)  
b = np.divide(a, s)       
print("np.divide(a,s)=")
print(b)  

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2],[3,4]])
print("a=")
print(a)
s = np.array([[5,6],[7,8]])
print("s=")
print(s)
b = a.dot(s)       
print("a.dot(s)=")
print(b)    

print("------------------------------------------------------------")  # 60個

a = np.arange(11,36)
a = a.reshape(5,5)
print("a=")
print(a)

b = a[0, 1:4]     # 索引 [0,1~3]
print("a[0,1:4]=")
print(b)
b = a[1:4, 0]     # 索引 [1~3,0]
print("a[1:4,0]=")
print(b)
b = a[:2, 1:3]    # 索引 [0~1,1~2]
print("a[:2,1:3]=")
print(b)
b = a[:,1]        # 索引 [0~4,1]
print("a[:,1]=")
print(b)
b = a[::2, ::2]   # 索引 [0~2~4,0~2~4]
print("a[::2,::2]=")
print(b)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("a=")
print(a)

b = a[[0,1,2],[0,1,0]]   # 索引 [0,0][1,1][2,0]
print("a[[0,1,2],[0,1,0]]=")
print(b)
b = np.array([a[0,0],a[1,1],a[2,0]])  # 索引 [0,0][1,1][2,0]
print("np.array([a[0,0],a[1,1],a[2,0]])")
print(b)

idx = np.array([0, 2, 0, 1])
print("idx=" + str(idx))
b = a[np.arange(4), idx]     # 索引 [0,0][1,2][2,0][3,1]
print("a[np.arange(4),idx]=")
print(b)
a[np.arange(4), idx] += 10
print("a[np.arange(4), idx] += 10->")
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2],[3,4],[5,6]])
print("a=")
print(a)

mask = (a > 2)
print("mask=")
print(mask)
b = a[mask]           # 使用布林值陣列取出值
print("a[mask]=" + str(b))
a[a > 2] = -1         # 同時更改多個True索引
print("a[a>2]=-1->")
print(a)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print("a=")
print(a)
print("a 形狀: " + str(a.shape))
b = np.array([1,0,1])
print("b=" + str(b))
print("b 形狀: " + str(b.shape))

c = a + b
print(c)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3],[4,5,6]])
print("a=")
print(a)

b = a.ravel()
print("a.ravel()=" + str(b))
c = a.flatten()
print("a.flatten()=" + str(c))
d = np.ravel(a)
print("np.ravel(a)=" + str(d))

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3,4,5,6])
print("a=" + str(a))

b = np.reshape(a,(3,2))
print("b=np.reshape(a,(3,2))->")
print(b)
c = b.T
print("c=b.T->")
print(c)
c = b.transpose()
print("c=b.transpose()->")
print(c)
c = np.transpose(b)
print("c=np.transpose(b)->")
print(c)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3])
print("a=" + str(a))

b = a[:, np.newaxis]
print("b=a[:,np.newaxis]->")
print(b)
print(b.shape)
b = a[np.newaxis, :]
print("b=a[np.newaxis,:]->")
print(b)
print(b.shape)

print("------------------------------------------------------------")  # 60個

a = np.array([1,2,3])
print("a=" + str(a))

b = a.copy()
print("b=a.copy()->" + str(b))
b.fill(4)
print("b.fill(0)=" + str(b))
c = np.concatenate((a,b))
print("c=np.concatenate((a,b))->" + str(c))

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c = np.concatenate((a,b))
print("c=np.concatenate((a,b))->")
print(c)
c = np.concatenate((a,b), axis=0)
print("c=np.concatenate((a,b), axis=0)->")
print(c)
c = np.concatenate((a,b), axis=1)
print("c=np.concatenate((a,b), axis=1)->")
print(c)

print("------------------------------------------------------------")  # 60個

a = np.array([[1,2,3,4,5,6,7,8]])
b = a.reshape(2, 4)
print(b.shape)
print("---------------------------")
c = np.expand_dims(b, axis=0)
d = np.expand_dims(b, axis=1)
print(c.shape, d.shape)
print("---------------------------")
e = np.squeeze(c)
f = np.squeeze(d)
print(e.shape, f.shape)

print("------------------------------------------------------------")  # 60個

a = np.array([[11,22,13,74,35,6,27,18]])

min_value = np.min(a)
max_value = np.max(a)
print("最小值: " + str(min_value))
print("最大值: " + str(max_value))

min_idx = np.argmin(a)
max_idx = np.argmax(a)
print("最小值索引: " + str(min_idx))
print("最大值索引: " + str(max_idx))

print("------------------------------------------------------------")  # 60個

v1 = np.random.random()
v2 = np.random.random()
print(v1, v2)
v3 = np.random.randint(5, 10)
v4 = np.random.randint(1, 101)
print(v3, v4)

print("------------------------------------------------------------")  # 60個

a = np.random.rand(5)
print("np.random.rand(5)=")
print(a)
b = np.random.rand(3, 2)  
print("np.random.rand(3,2)=")
print(b)
c = np.random.randint(5, 10, size=5)
print("np.random.randint(5,10,size=5)")
print(c)
d = np.random.randint(5, 10, size=(2,3))
print("np.random.randint(5,10,size=(2,3))")
print(d)

print("------------------------------------------------------------")  # 60個

a = np.array([30,45,60]) 

print(np.sin(a*np.pi/180)) 
print(np.cos(a*np.pi/180)) 
print(np.tan(a*np.pi/180)) 

print("------------------------------------------------------------")  # 60個

a = np.array([1.0,5.55, 123, 0.567, 25.532]) 
print("a=" + str(a))

print(np.around(a))
print(np.around(a, decimals = 1))
print(np.around(a, decimals = -1))

a = np.array([-1.7, 1.5, -0.2, 0.6, 10]) 
print("a=" + str(a))

b = np.floor(a)
print("floor()=" + str(b))
b = np.ceil(a)
print("ceil()=" + str(b))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



