import tensorflow as tf


global_step = tf.Variable(0)

# 通过exponential_decay函数生成学习率
learning_rate = tf.train.exponential_decay(0.1, global_step, 100, 0.96, staircase=True)

# 使用指数衰减的学习率，在minimize函数中传入global_step将自动更新
# global_step参数，从而使得学习得到相应更新。
learning_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(...my loss..., global_step=global_step)