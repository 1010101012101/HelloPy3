import tensorflow as tf

a = tf.constant([1, 2], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = a + b
print(result)

'''
输出：
ValueError: Tensor conversion requested dtype int32 for Tensor with dtype float32: 'Tensor("b:0", shape=(2,), dtype=float32)'

>>强调张量的type属性
'''