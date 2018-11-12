import tensorflow as tf


with tf.variable_scope("foo"):
    v = tf.get_variable("v", [1], initializer=tf.constant_initializer(1.0))


# 因为在命名空间foo中已经存在名字为v的变量，所以以下代码 将会报错：
#with tf.variable_scope("foo"):
#    v = tf.get_variable("v", [1])
"""
输出：
ValueError: Variable foo/v already exists, disallowed. Did you mean to set reuse=True or reuse=tf.AUTO_REUSE in VarScope? Originally defined at:
"""

with tf.variable_scope("foo", reuse=True):
    v1 = tf.get_variable("v")
    print(v == v1)


#
#with tf.variable_scope("bar", reuse=True):
#    v = tf.get_variable("v", [1])
"""
输出：
ValueError: Variable bar/v does not exist, or was not created with tf.get_variable(). Did you mean to set reuse=tf.AUTO_REUSE in VarScope?
"""