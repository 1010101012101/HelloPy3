import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2, 3], stddev=1), name='w1')
w2 = tf.Variable(tf.random_normal([2, 2], stddev=1), name='w2')
tf.assign(w1, w2)
'''
将报错：
ValueError: Dimension 1 in both shapes must be equal, but are 3 and 2. Shapes are [2,3] and [2,2]. for 'Assign' (op: 'Assign') with input shapes: [2,3], [2,2].
'''
tf.assign(w1, w2, validate_shape=False)
'''
可执行成功
'''