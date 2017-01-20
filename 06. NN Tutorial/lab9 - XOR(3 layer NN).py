# three layer neural network

import tensorflow as tf
import numpy as np

xy = np.loadtxt('train.txt', unpack=True)
x_data = np.transpose(xy[0:-1])
y_data = np.reshape(xy[-1], (4,1))

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_uniform([2, 5], -1.0, 1.0))
W2 = tf.Variable(tf.random_uniform([5, 3], -1.0, 1.0))
W3 = tf.Variable(tf.random_uniform([3, 1], -1.0, 1.0))

b1 = tf.Variable(tf.zeros([5]), name="Bias1")
b2 = tf.Variable(tf.zeros([3]), name="Bias2")
b3 = tf.Variable(tf.zeros([1]), name="Bias3")

L2 = tf.sigmoid(tf.matmul(X, W1)+b1)
L3 = tf.sigmoid(tf.matmul(L2, W2)+b2)
hypothesis = tf.sigmoid(tf.matmul(L3, W3)+b3)

cost = tf.reduce_mean(-Y*tf.log(hypothesis)-(1-Y)*tf.log(1-hypothesis))
optimizer = tf.train.GradientDescentOptimizer(0.3).minimize(cost)

init = tf.initialize_all_variables()

with tf.Session() as session:
    session.run(init)

    for step in xrange(2001):
        session.run(optimizer, feed_dict={X:x_data, Y:y_data})
        if step % 500 == 0:
            print session.run(cost, feed_dict={X:x_data, Y:y_data})


    answer = tf.equal(tf.floor(hypothesis+0.5), Y)
    accuracy = tf.reduce_mean(tf.cast(answer, "float"))
    print session.run([hypothesis], feed_dict={X:x_data, Y:y_data})
    print "Accuracy : ", accuracy.eval({X:x_data, Y:y_data})*100, "%"




