'''
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
myapp = App(root)
myapp.mainloop()
'''

'''
import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

filename = 'C:/______test_files/_emgu/lena.jpg'
face_cascade = cv2.CascadeClassifier('/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_default.xml')
img = cv2.imread(filename)	#讀取本機圖片
cv2.imshow('Original Picture', img) #顯示圖片

#灰階
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階

#人臉辨識
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.08,
    minNeighbors=6,
    minSize=(10, 10))
    
# 繪製人臉部份的方框（能不能不要方匡啊，要輪廓就好）
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# 顯示成果
#cv2.imshow(img)
cv2.imshow('New Picture', img) #顯示圖片


'''

'''
import cv2
import numpy as np

filename = 'C:/______test_files/_emgu/lena.jpg'

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format


#== Processing =======================================================================

#-- Read image -----------------------------------------------------------------------
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('原圖灰階', gray)
cv2.waitKey()

#-- Edge detection -------------------------------------------------------------------

edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
cv2.imshow('Canny 處理', edges)
cv2.waitKey()
edges = cv2.dilate(edges, None)
cv2.imshow('Dilate 處理', edges)
cv2.waitKey()
edges = cv2.erode(edges, None)
cv2.imshow('Erode 處理', edges)
cv2.waitKey()

#cv2.imwrite('C:/Temp/person-masked.jpg', masked)           # Save
'''

'''
import cv2
import numpy as np

filename = 'C:/______test_files/_emgu/lena.jpg'

img = cv2.imread(filename)

# split image into channels
c_red, c_green, c_blue = cv2.split(img)

# merge with mask got on one of a previous steps
#img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

cv2.imshow('R', c_red)
cv2.waitKey()

cv2.imshow('G', c_green)
cv2.waitKey()

cv2.imshow('B', c_blue)
cv2.waitKey()
'''

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'C:/______test_files/_emgu/lena.jpg'

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format


#== Processing =======================================================================

#-- Read image -----------------------------------------------------------------------
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#-- Edge detection -------------------------------------------------------------------
edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

# split image into channels
c_red, c_green, c_blue = cv2.split(img)

# merge with mask got on one of a previous steps
img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

# show on screen (optional in jupiter)
#%matplotlib inline
plt.imshow(img_a)
plt.show()

# save to disk
cv2.imwrite('img/girl_1.png', img_a*255)

# or the same using plt
plt.imsave('img/girl_2.png', img_a)

cv2.imshow('img', masked)                                   # Displays red, saves blue

cv2.waitKey()
'''





