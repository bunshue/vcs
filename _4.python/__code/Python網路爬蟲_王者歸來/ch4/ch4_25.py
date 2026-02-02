# ch4_25.py
import pandas as pd
import matplotlib.pyplot as plt

colName = ['sepal_len','sepal_wd','petal_len','petal_wd','species']
iris = pd.read_csv('iris.csv', names = colName)

plt.plot(iris['sepal_len'],iris['sepal_wd'],'*',color='g')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Sepal length and width anslysis')
plt.show()











