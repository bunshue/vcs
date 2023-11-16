import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

x_values =pd.DataFrame([1,2,3,4])
y_values =pd.DataFrame([0,0.3,0.6,0.9])
x_test =pd.DataFrame([1.5,3,5])

#train model on data
body_reg = linear_model.LinearRegression()
body_reg.fit(x_values, y_values)


y_test_predict= body_reg.predict(x_test)
print(" body_reg.predict(x_text)",y_test_predict)

#visualize results
plt.scatter(x_values, y_values)
plt.scatter(x_test, y_test_predict, color='red')
plt.plot(x_test,y_test_predict, color='blue')
plt.show()