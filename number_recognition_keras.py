import time
from datetime import datetime

import keras
import matplotlib.pyplot as plt
import numpy as np
from keras.callbacks import ModelCheckpoint
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.datasets import mnist
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from keras.optimizers import Adam
from keras.utils import np_utils

# use_model = 'models/model_epoch_10_2020-08-01_19_32_44.h5'
use_model = None

enable_evaluation = not use_model


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


def model_1():
    # https://www.mdpi.com/1424-8220/20/12/3344/pdf
    # Four layers model case 5 with feature maps of 12-24-28-32, 99.76% accuracy
    #        k s d  p i/p o/p r  f
    # Layer1 5 1 2  2  28 28 9  12
    # Layer2 5 2 1  2  28 14 13 24
    # Layer3 3 2 1  1  14 7  17 28
    # Layer4 3 2 1  1  7  4  27 32

    model = Sequential()
    model.add(Conv2D(
        input_shape=(28, 28, 1),
        filters=12,
        kernel_size=5,
        strides=1,
        dilation_rate=2,
        padding='same',
        activation='relu'
    ))
    model.add(Conv2D(24, 5, strides=2, padding='same', activation='relu'))
    model.add(Conv2D(28, 3, strides=2, padding='same', activation='relu'))
    model.add(Conv2D(32, 3, strides=2, padding='same', activation='relu'))
    model.add(Flatten())
    model.add(Dropout(0.1))
    model.add(Dense(10, activation='softmax'))

    adam = Adam(lr=1e-3)

    model.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])

    return model


def model_2():
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
    return model


def train_model(model):
    time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = "logs/fit/" + time_str
    tensorboard_callback = keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

    weight_save_callback = ModelCheckpoint('models/model_{epoch:02d}-{val_loss:.2f}-%s.hdf5' % time_str,
                                           monitor='val_loss',
                                           verbose=0, save_best_only=False, mode='auto')

    x_train, y_train, x_test, y_test = dataset()
    model.fit(x_train, y_train, batch_size=32, epochs=15,
              callbacks=[tensorboard_callback, weight_save_callback],
              validation_split=0.15)
    return model


if use_model:
    print("using model", use_model)
    model = load_model(use_model)
else:
    print("training new model")
    model = train_model(model_2())

if enable_evaluation:
    x_train, y_train, x_test, y_test = dataset()
    loss, accuracy = model.evaluate(x_test, y_test)
    print("loss: ", loss, "acc: ", accuracy)


def predict(img):
    img = np.array(img).reshape((-1, 28, 28, 1))
    return model.predict(img)


if __name__ == '__main__':
    pass
