
from sklearn.naive_bayes import GaussianNB
import numpy as np



X=np.array([[9,9],[9.2,9.2],[9.6,9.2],[9.2,9.2],[6.7,7.1],[7,7.4],[7.6,7.5],
   [7.2,10.3], [7.3,10.5], [7.2,9.2], [7.3,10.2], [7.2,9.7], [7.3,10.1], [7.3,10.1]])
Y=np.array([1,1,1,1,1,1,1,
   2,2,2,2,2,2,2])


model = GaussianNB()
model.fit(X,Y)
print(model.class_prior_ )
print(model.get_params() )



#Predict Output
x_test=np.array([[8,8],[8.3,8.3]])
predicted= model.predict(x_test)
print(predicted)
print(model.predict_proba(x_test))

t1=np.array([[1, 2],[3, 4]])
print(t1.ravel())      # 轉成一維 輸出為[1, 2, 3, 4]
t2=np.linspace(0, 10, 3)
print(t2)  #輸出為[ 0.  5. 10.]
t3=np.linspace(0, 10, 2)
print(t3)  #輸出為[ 0. 10.]
t4,t5 = np.meshgrid(t2,t3)
print(t4)  #輸出為[[ 0.  5. 10.][ 0.  5. 10.]]
print(t5)  #輸出為[[ 0.  0.  0.] [10. 10. 10.]]
t4,t5 = np.meshgrid(t3,t2)
print(t4) #輸出為[[ 0. 10.][ 0. 10.][ 0. 10.]]
print(t5) #輸出為[[ 0.  0.][ 5.  5.][10. 10.]]


import matplotlib.pyplot as plt
#繪圖
plt.plot(X[:7,0], X[:7,1], 'yx' )
plt.plot(X[7:,0], X[7:,1], 'g.' )
plt.plot(x_test[:,0],x_test[:,1], 'r^' )                                                                                       #綠色點
plt.ylabel('W')
plt.xlabel('H')
plt.legend(('Citrus','Lemon'),  loc='upper left')

x_min= X[:, 0].min() - .5
x_max= X[:, 0].max() + .5
y_min= X[:, 1].min() - .5
y_max= X[:, 1].max() + .5

xx, yy = np.meshgrid(np.linspace(x_min, x_max, 30),
                     np.linspace(y_min, y_max, 30))
Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])
Z1 = Z[:, 1].reshape(xx.shape)
plt.contour(xx, yy, -Z1, [-0.5], colors='k')

plt.savefig('myBayes.png', bbox_inches='tight')

plt.show()

