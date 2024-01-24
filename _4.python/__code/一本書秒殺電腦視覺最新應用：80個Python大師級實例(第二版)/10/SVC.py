from sklearn import datasets,svm
import matplotlib.pyplot as plt
 
""" 识别手写体数字 """ 
svc=svm.SVC(gamma=0.001,C=100.)
digits=datasets.load_digits() # 导入Digits数据集
# print(digits.DESCR) # 查看数据集的说明信息 
def plts():
    ''' 显示要识别的数字图片 '''
    plt.subplot(321)
    plt.imshow(digits.images[1791],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.subplot(322)
    plt.imshow(digits.images[1792],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.subplot(323)
    plt.imshow(digits.images[1793],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.subplot(324)
    plt.imshow(digits.images[1794],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.subplot(325)
    plt.imshow(digits.images[1795],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.subplot(326)
    plt.imshow(digits.images[1796],cmap=plt.cm.gray_r,interpolation='nearest')
    plt.show()
  
def svms():
    ''' 学习并返回识别结果 '''
    svc.fit(digits.data[:1791],digits.target[:1791]) # 训练
    res=svc.predict(digits.data[1791:1797]) # 识别
    return list(res)
 
if __name__=='__main__':
    result=svms()
    duibi=digits.target[1791:1797]
    print('识别的数字: {}\n实际的结果: {}'.format(result,list(duibi)))
    plts()
