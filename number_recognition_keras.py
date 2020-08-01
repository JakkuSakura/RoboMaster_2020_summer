import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import Adam
from keras.utils import np_utils

existing_model_path = 'models/model_epoch_10_2020-08-01_19_32_44.h5'
enable_evaluation = False


def dataset():
    # 载入数据
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # (60000,28,28)->(60000,28,28,1)
    x_train = x_train.reshape(-1, 28, 28, 1) / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1) / 255.0
    # 换one hot格式
    y_train = np_utils.to_categorical(y_train, num_classes=10)
    y_test = np_utils.to_categorical(y_test, num_classes=10)

    return x_train, y_train, x_test, y_test


def new_model():
    model = Sequential()
    model.add(Conv2D(
        input_shape=(28, 28, 1),
        filters=32,
        kernel_size=5,
        strides=1,
        padding='same',
        activation='relu'
    ))
    model.add(MaxPooling2D(
        pool_size=2,
        strides=2,
        padding='same',
    ))
    model.add(Conv2D(64, 5, strides=1, padding='same', activation='relu'))
    model.add(MaxPooling2D(2, 2, 'same'))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(10, activation='softmax'))

    adam = Adam(lr=1e-3)

    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

    x_train, y_train, x_test, y_test = dataset()
    for i in range(5):
        # 训练模型
        model.fit(x_train, y_train, batch_size=32, epochs=2)
        model.save('models/model_epoch_%d_%s.h5' % ((i + 1) * 2, datetime.now().strftime('%Y-%m-%d_%H_%M_%S')))
    return model


if existing_model_path:
    print("using model", existing_model_path)
    model = load_model(existing_model_path)
else:
    print("training new model")
    model = new_model()

if enable_evaluation:
    x_train, y_train, x_test, y_test = dataset()
    loss, accuracy = model.evaluate(x_test, y_test)
    print("loss: ", loss, "acc: ", accuracy)


def predict(img):
    img = np.array(img).reshape((-1, 28, 28, 1))
    return model.predict(img)
