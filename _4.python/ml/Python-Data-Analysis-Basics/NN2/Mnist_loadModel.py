from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import load_model

def show_images_labels_predictions(images,labels,predictions,start_id,num=10):
    plt.gcf().set_size_inches(12, 14)
    if num>25: num=25 
    for i in range(0, num):
        ax=plt.subplot(5,5, i+1)
        ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
        if( len(predictions) > 0 ) :  #有傳入預測資料
            title = 'ai = ' + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += (' (o)' if predictions[start_id]==labels[start_id] else ' (x)') 
            title += '\nlabel = ' + str(labels[start_id])
        else :  #沒有傳入預測資料
            title = 'label = ' + str(labels[start_id])
        ax.set_title(title,fontsize=12)  #X,Y軸不顯示刻度
        ax.set_xticks([]);ax.set_yticks([])        
        start_id+=1 
    plt.show()

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()
test_feature_vector = test_feature.reshape(len( test_feature), 784).astype('float32')
test_feature_normalize = test_feature_vector/255
model = load_model('Mnist_mlp_model.h5')

prediction=model.predict_classes(test_feature_normalize)  #預測
show_images_labels_predictions(test_feature,test_label,prediction,0)
