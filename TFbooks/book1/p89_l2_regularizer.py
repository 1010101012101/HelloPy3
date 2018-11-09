import tensorflow as tf

"""
batch_size = 8

x = tf.placeholder(tf.float32, shape=(batch_size, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(batch_size, 1), name='y-input')

w = tf.Variable(tf.random_normal([2, 1], stddev=1, seed=1))
y = tf.matmul(x, w)

loss = tf.reduce_mean(tf.square(y_ - y) + tf.contrib.layers.l2_regularizer(lambda )(w)
"""

weights = tf.constant([[1.0, -2.0], [-3.0, 4.0]])
with tf.Session() as sess:
    # 输出(|1|+|-2|+|-3|+|4|)x0.5=5.其中0.5为正则化项的权重
    print(sess.run(tf.contrib.layers.l1_regularizer(0.5)(weights)))
    # 输出为(1^2 + (-2)^2 + (-3)^2 + 4^2)/2x0.5=7.5
    print(sess.run(tf.contrib.layers.l2_regularizer(0.5)(weights)))