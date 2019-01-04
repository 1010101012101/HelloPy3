from keras.models import Sequential
from keras.layers import Conv2D,Flatten


model = Sequential()
model.add(Conv2D(64, (3, 3), input_shape=(3, 32, 32), padding='same',))
# now: model.output_shape == (None, 64, 32, 32)

model.add(Flatten())
# now: model.output_shape == (None, 65536)

model.summary()
