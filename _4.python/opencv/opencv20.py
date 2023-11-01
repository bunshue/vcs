import sys
import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

print('用np建立一個影像陣列')
img=np.ones([2,4,3],dtype=np.uint8)
size=img.shape[:2]
rst=cv2.resize(img,size)
print("img.shape=\n",img.shape)
print("img=\n",img)
print("rst.shape=\n",rst.shape)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/test.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
size=(int(cols*0.9),int(rows*0.5))
rst=cv2.resize(img,size)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/test.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rst=cv2.resize(img,None,fx=2,fy=0.5)
print("img.shape=",img.shape)
print("rst.shape=",rst.shape)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

x=cv2.flip(img,0)
y=cv2.flip(img,1)
xy=cv2.flip(img,-1)
cv2.imshow("img",img)
cv2.imshow("x",x)
cv2.imshow("y",y)
cv2.imshow("xy",xy)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

height,width=img.shape[:2]
x=100
y=200
M = np.float32([[1, 0, x], [0, 1, y]])
move=cv2.warpAffine(img,M,(width,height))
cv2.imshow("original",img)
cv2.imshow("move",move)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

height,width=img.shape[:2]
M=cv2.getRotationMatrix2D((width/2,height/2),45,0.6)
rotate=cv2.warpAffine(img,M,(width,height))
cv2.imshow("original",img)
cv2.imshow("rotation",rotate)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols,ch=img.shape
p1=np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2=np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
M=cv2.getAffineTransform(p1,p2)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("origianl",img)
cv2.imshow("result",dst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/demo.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
print(rows,cols)
pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(cols,rows))
cv2.imshow("img",img)
cv2.imshow("dst",dst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols=img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
print("img=\n",img)
print("mapx=\n",mapx)
print("mapy=\n",mapy)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols=img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
print("img=\n",img)
print("mapx=\n",mapx)
print("mapy=\n",mapy)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols=img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
print("img=\n",img)
print("mapx=\n",mapx)
print("mapy=\n",mapy)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        mapx.itemset((i,j),j)
        mapy.itemset((i,j),rows-1-i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols=img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
            mapx.itemset((i,j),cols-1-j)
            mapy.itemset((i,j),i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
print("img=\n",img)
print("mapx=\n",mapx)
print("mapy=\n",mapy)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
            mapx.itemset((i,j),cols-1-j)
            mapy.itemset((i,j),i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
img=np.random.randint(0,256,size=[4,5],dtype=np.uint8)

rows,cols=img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
            mapx.itemset((i,j),cols-1-j)
            mapy.itemset((i,j),rows-1-i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
print("img=\n",img)
print("mapx=\n",mapx)
print("mapy=\n",mapy)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
            mapx.itemset((i,j),cols-1-j)
            mapy.itemset((i,j),rows-1-i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

print('用np建立一個隨機影像陣列')
img=np.random.randint(0,256,size=[4,6],dtype=np.uint8)

rows,cols=img.shape
mapx = np.zeros(img.shape,np.float32)
mapy = np.zeros(img.shape,np.float32)
for i in range(rows):
    for j in range(cols):
            mapx.itemset((i,j),i)
            mapy.itemset((i,j),j)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
print("img=\n",img)
print("mapx=\n",mapx)
print("mapy=\n",mapy)
print("rst=\n",rst)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
            mapx.itemset((i,j),cols-1-j)
            mapy.itemset((i,j),rows-1-i)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
print('讀取圖檔 :', filename)
img=cv2.imread(filename)

rows,cols=img.shape[:2]
mapx = np.zeros(img.shape[:2],np.float32)
mapy = np.zeros(img.shape[:2],np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols< i <0.75*cols and 0.25*rows< j <0.75*rows:
                mapx.itemset((i,j),2*( j - cols*0.25 ) + 0.5)
                mapy.itemset((i,j),2*( i - rows*0.25 ) + 0.5)
        else:     
                mapx.itemset((i,j),0)
                mapy.itemset((i,j),0)
rst=cv2.remap(img,mapx,mapy,cv2.INTER_LINEAR)
cv2.imshow("original",img)
cv2.imshow("result",rst)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


