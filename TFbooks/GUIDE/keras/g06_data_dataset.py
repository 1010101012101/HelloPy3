import tensorflow as tf
from tensorflow.keras import layers
import numpy as np

model = tf.keras.Sequential([
# Adds a densely-connected layer with 64 units to the model:
layers.Dense(64, activation='relu'),

# Add another:
layers.Dense(64, activation='relu'),
# Add a softmax layer with 10 output units:
layers.Dense(10, activation='softmax')])

model.compile(optimizer=tf.train.AdamOptimizer(0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

data = np.random.random((1024, 32))
labels = np.random.random((1024, 10))

dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32)
dataset = dataset.repeat()

val_data = np.random.random((100, 32))
val_labels = np.random.random((100, 10))

dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32).repeat()

val_dataset = tf.data.Dataset.from_tensor_slices((val_data, val_labels))
val_dataset = val_dataset.batch(32).repeat()

model.fit(dataset, batch_size=32, epochs=10, steps_per_epoch=30,
          validation_data=val_dataset,
          validation_steps=3)

#model.fit(data, labels, epochs=10, batch_size=32,
#          validation_data=(val_data, val_labels))

# Don't forget to specify `steps_per_epoch` when calling `fit` on a datasets.
#model.fit(datasets, epochs=10, steps_per_epoch=30)
