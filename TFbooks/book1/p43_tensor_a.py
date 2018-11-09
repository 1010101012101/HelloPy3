import tensorflow as tf

a = tf.constant([1.0, 2.0], name='a')
b = tf.constant([2.0, 3.0], name='b')
result = tf.add(a, b, name='add')
print(result)

'''
输出：
Tensor("add:0", shape=(2,), dtype=float32)

>>add:0说明result这个张量是计算节点add输出的第一个结果（编号从0开始）
'''