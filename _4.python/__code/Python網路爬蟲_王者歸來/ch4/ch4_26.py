# ch4_26.py
import pandas as pd
import matplotlib.pyplot as plt

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)

# 擷取不同品種的鳶尾花
iris_setosa = iris[iris['species'] == 'Iris-setosa']
iris_versicolor = iris[iris['species'] == 'Iris-versicolor']
iris_virginica = iris[iris['species'] == 'Iris-virginica']
# 繪製散點圖
plt.plot(iris_setosa['sepal_len'],iris_setosa['sepal_wd'],
         '*',color='g',label='setosa')
plt.plot(iris_versicolor['sepal_len'],iris_versicolor['sepal_wd'],
         'x',color='b',label='versicolor')
plt.plot(iris_virginica['sepal_len'],iris_virginica['sepal_wd'],
         '.',color='r',label='virginica')
# 標註軸和標題
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Sepal length and width anslysis')
plt.legend()
plt.show()











