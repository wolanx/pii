import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt


class Model(object):
    def __init__(self):
        self.a3 = tf.Variable(tf.random.uniform([1]))
        self.a2 = tf.Variable(tf.random.uniform([1]))
        self.a1 = tf.Variable(tf.random.uniform([1]))
        self.a0 = tf.Variable(tf.random.uniform([1]))

    def __call__(self, x):
        # return self.a1 * x + self.a0  # w*x + b
        # return self.a3 * x ** 3 + self.a2 * x ** 2 + self.a1 * x + self.a0
        return self.a3 * np.sinc(x) ** 2 + self.a2 * np.sinc(x) + self.a1 * x + self.a0


def loss_fn(model, x, y):
    return tf.reduce_mean(tf.square(model(x) - y))


def run(dataXY, iterNum=10000, rate=0.001, debug=False):
    (dataX, dataY) = dataXY
    model = Model()

    for epoch in range(iterNum):
        with tf.GradientTape() as tape:
            loss = loss_fn(model, dataX, dataY)

        a3, a2, a1, a0 = tape.gradient(loss, [model.a3, model.a2, model.a1, model.a0])
        (a3, a2, a1, a0), _ = tf.clip_by_global_norm((a3, a2, a1, a0), 15)

        model.a3.assign_sub(rate * a3)
        model.a2.assign_sub(rate * a2)
        model.a1.assign_sub(rate * a1)
        model.a0.assign_sub(rate * a0)

        if debug and epoch % 100 == 0:
            print(
                "Epoch [{}/{}], loss [{:.3f}], a/b/c/d [{:.3f}/{:.3f}/{:.3f}/{:.3f}]".format(
                    epoch,
                    iterNum,
                    loss,
                    float(model.a3.numpy()),
                    float(model.a2.numpy()),
                    float(model.a1.numpy()),
                    float(model.a0.numpy()),
                )
            )
            plt.cla()
            plt.scatter(dataX, dataY)
            plt.plot(dataX, model(dataX), c="r")
            plt.pause(0.05)

    print(
        "Epoch [{}/{}], loss [{:.3f}], a/b/c/d [{:.3f}/{:.3f}/{:.3f}/{:.3f}]".format(
            iterNum,
            iterNum,
            loss,
            float(model.a3.numpy()),
            float(model.a2.numpy()),
            float(model.a1.numpy()),
            float(model.a0.numpy()),
        )
    )

    return model, loss
