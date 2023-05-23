foldername = 'C:/_git/vcs/_1.data/______test_files1/__pic/imagedata/'

import matplotlib.pyplot as plt
import glob,cv2

def show_images_labels_predictions(images,labels,start_id,num=10):
    plt.gcf().set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, i+1)
        ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
        title = 'label = ' + str(labels[start_id])
        ax.set_title(title,fontsize=12)  #X,Y軸不顯示刻度
        ax.set_xticks([]);ax.set_yticks([])        
        start_id+=1 
    plt.show()
    
files = glob.glob(foldername+'*.jpg')  #建立測試資料
test_feature=[]
test_label=[]
for file in files:
    img=cv2.imread(file)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)
    label=file[54:55]  #"imagedata\1.jpg"第10個字元1為label
    test_label.append(int(label))
   
show_images_labels_predictions(test_feature,test_label,0,len(test_feature))

