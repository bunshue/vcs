import keras
import numpy as np
import matplotlib.pyplot as plt

ITERATIONS = 500

'''
model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

#xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype = float)
#ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype = float)

# y = x ^ 2
xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
ys = np.array([0.0, 1.0, 4.0, 9.0, 16.0, 25.0], dtype = float)


model.fit(xs, ys, epochs = ITERATIONS)

print('keras 預測')

print(model.predict([2.5]))     #[[9.230829]]
print(model.predict([4.5]))     #[[19.108438]]
print(model.predict([6.0]))     #[[26.516644]]
print(model.predict([10.0]))    #[[46.271862]]

'''


model = keras.Sequential([keras.layers.Dense(units = 1, input_shape = [1])])
model.compile(optimizer = 'sgd', loss = 'mean_squared_error')

ST = 0
SP = 10
N = 51

# yy = xx ^ 2
xx = np.linspace(ST, SP, N, dtype = float)  # 建立一個array, 在 ST 與 SP 的範圍之間讓 N 個點等分
yy = xx ** 2

model.fit(xx, yy, epochs = ITERATIONS)

print('keras 預測')

def get_predict_value(x):
    y1 = x ** 2
    y2 = float(model.predict([x]))
    diff = y1 - y2
    print('x =', x, '\t真實值 :', y1, '\t預測值 :', y2, '\t差距 :', diff)
    return y1, y2, diff

x = 2.5
get_predict_value(x)

x = 4.5
get_predict_value(x)

x = 6.0
get_predict_value(x)

x = 10.0
get_predict_value(x)

px = list()
y1 = list()
y2 = list()
y3 = list()

for x in range(5, 110, 10):
    yy1 , yy2, yy3 = get_predict_value(x / 10)
    #print('get data', x, yy1, yy2, yy3)
    #print('get type', type(x), type(yy1), type(yy2), type(yy3))
    px.append(x / 10)
    y1.append(yy1)
    y2.append(yy2)
    y3.append(yy3)


print(px)
print(y1)
print(y2)
print(y3)

print(len(px))
print(len(y1))
print(len(y3))
print(len(y3))

plt.figure()

plt.plot(px, y1, 'r:o')
plt.plot(px, y2, 'g:o')
#plt.plot(px, y3, 'b:o')#diff

#plt.plot(xx, yy, c = 'r', label = '', linewidth = 1)
#plt.plot(x, y, c = 'g', label = 'sin(x)', linewidth = 1)

#plt.xlabel('x')
#plt.ylabel('sin(x)')
#plt.title('')
#plt.legend()


plt.xlim(-1, 12)
plt.ylim(-1, 120)

plt.show()


