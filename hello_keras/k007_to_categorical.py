from keras.utils.np_utils import *
#类别向量定义
b = [0,1,2,3,4,5,6,0,8]
#调用to_categorical将b按照9个类别来进行转换
b = to_categorical(b)
print(b)