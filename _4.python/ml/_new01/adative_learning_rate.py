import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def _height(x, y):
    # z = np.sqrt(x**2 + y**2)
    z = 0.5 * (x**2) + 0.8 * (y**2)
    return z


def main():
    x = tf.Variable(-8.00000)
    y = tf.Variable(4.00000)
    a = tf.constant(0.1000)
    b = tf.constant(1.0000)
    mul1 = tf.multiply(a, tf.square(x))
    mul2 = tf.multiply(b, tf.square(y))
    output = tf.add(mul1, mul2)

    gradient_op = tf.train.GradientDescentOptimizer(
        learning_rate=0.4).minimize(output)

    momentum_op = tf.train.MomentumOptimizer(
        learning_rate=0.035, momentum=0.9).minimize(output)

    adagrad_op = tf.train.AdagradOptimizer(learning_rate=2).minimize(output)

    rms_op = tf.train.RMSPropOptimizer(learning_rate=0.5).minimize(output)

    adam_op = tf.train.AdamOptimizer(learning_rate=0.35).minimize(output)

    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        epochs = 30
        start_x = [-8.0]
        start_y = [4.0]

        for epoch in range(epochs):
            print("epoch of triaining", epoch)
            sess.run(rms_op)
            array_x = sess.run(x)
            array_y = sess.run(y)
            start_x.append(array_x)
            start_y.append(array_y)

        print(epoch)
        print(start_x)
        print(start_y)

        x = np.arange(-10.0, 10.0, 2)
        y = np.arange(-10.0, 10.0, 2)
        X, Y = np.meshgrid(x, y)
        Z = _height(X, Y)

        plt.figure(figsize=(8, 4))
        cs = plt.contourf(X, Y, Z, 15, alpha=0.75, cmap='rainbow')
        # cs = plt.contour(X, Y, Z, 15, cmap='rainbow')
        plt.plot(start_x, start_y, c='b')
        plt.title('rms')
        for xt, yt in zip(start_x, start_y):
            plt.scatter(xt, yt, c='b')
        plt.show()


if __name__ == '__main__':
    main()