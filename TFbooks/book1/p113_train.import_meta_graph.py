import tensorflow as tf

saver = tf.train.import_meta_graph("data/mode/model.ckpt/model.ckpt.meta")

with tf.Session() as sess:
    saver.restore(sess, "data/model/model.ckpt")
    print(sess.run(tf.get_default_graph().get_tensor_by_name("add:0")))
