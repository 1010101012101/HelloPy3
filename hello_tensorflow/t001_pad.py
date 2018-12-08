import tensorflow as tf



t = tf.constant([[1, 2, 3], [4, 5, 6]])
paddings = tf.constant([[1, 1,], [2, 2]])
A = tf.pad(t, paddings, "CONSTANT")
R = tf.pad(t, paddings, "REFLECT")
S = tf.pad(t, paddings, "SYMMETRIC")
print(t)
print(A)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print("t:\n", sess.run(t))
    print("A:\n",sess.run(A))
    print("R:\n",sess.run(R))
    print("S:\n",sess.run(S))