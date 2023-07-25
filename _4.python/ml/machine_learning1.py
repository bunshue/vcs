import keras
import numpy as np

model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

#xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
#ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

# y = x ^ 2
xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
ys = np.array([0.0, 1.0, 4.0, 9.0, 16.0, 25.0], dtype = float)


model.fit(xs, ys, epochs = 500)

print('keras 預測')

print(model.predict([2.5]))     #[[9.230829]]
print(model.predict([4.5]))     #[[19.108438]]
print(model.predict([6.0]))     #[[26.516644]]
print(model.predict([10.0]))    #[[46.271862]]



