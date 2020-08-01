import time

import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Conv2D, Convolution2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import Adam
from keras.utils import np_utils

# 载入数据
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# (60000,28,28)->(60000,28,28,1)
x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
# 换one hot格式
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)


def new_model():
    # 定义顺序模型
    model = Sequential()

    # 第一个卷积层
    # input_shape 输入平面
    # filters 卷积核/滤波器个数
    # kernel_size 卷积窗口大小
    # strides 步长
    # padding padding方式 same/valid
    # activation 激活函数
    model.add(Conv2D(
        input_shape=(28, 28, 1),
        filters=32,
        kernel_size=5,
        strides=1,
        padding='same',
        activation='relu'
    ))
    # 第一个池化层
    model.add(MaxPooling2D(
        pool_size=2,
        strides=2,
        padding='same',
    ))
    # 第二个卷积层
    model.add(Conv2D(64, 5, strides=1, padding='same', activation='relu'))
    # 第二个池化层
    model.add(MaxPooling2D(2, 2, 'same'))
    # 把第二个池化层的输出扁平化为1维
    model.add(Flatten())
    # 第一个全连接层
    model.add(Dense(1024, activation='relu'))
    # Dropout
    model.add(Dropout(0.5))
    # 第二个全连接层
    model.add(Dense(10, activation='softmax'))

    # 定义优化器
    adam = Adam(lr=1e-4)

    # 定义优化器，loss function，训练过程中计算准确率
    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
    for i in range(5):
        # 训练模型
        model.fit(x_train, y_train, batch_size=32, epochs=2)
        model.save('models/model_epoch_%d_%s.h5' % ((i + 1) * 2, str(time.time())))
    return model


model = new_model()
# model = load_model('model.h5')

# 评估模型
loss, accuracy = model.evaluate(x_test, y_test)

print('test loss', loss)
print('test accuracy', accuracy)

if __name__ == '__main__':
    pass
