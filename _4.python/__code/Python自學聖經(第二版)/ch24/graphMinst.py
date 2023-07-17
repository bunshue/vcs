import matplotlib.pyplot as plt
from keras.datasets import mnist
(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

def show_images_labels_predictions(images,labels,start_id,num=10):
    plt.gcf().set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(num):
        ax=plt.subplot(5,5, i+1)
        ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
        title = 'label = ' + str(labels[start_id])
        ax.set_title(title,fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([]);ax.set_yticks([])        
        start_id+=1 
    plt.show()

show_images_labels_predictions(train_feature,train_label,0,10)
