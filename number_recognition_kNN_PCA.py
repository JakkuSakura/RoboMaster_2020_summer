import struct
import time

import numpy as np

from PCA import PCA

use_values = True
n_components = 100
knn_samples = 3


def read_image_data(image_path, label_path):
    image_file = open(image_path, 'rb')
    label_file = open(label_path, 'rb')

    image_raw_data = image_file.read()
    label_raw_data = label_file.read()

    image_file.close()
    label_file.close()

    image_index = 0
    label_index = 0

    image_magic_num, image_len, image_rows, image_cols = struct.unpack_from('>IIII', image_raw_data, image_index)
    label_magic_num, label_len = struct.unpack_from('>II', label_raw_data, label_index)

    image_index += struct.calcsize('>IIII')
    label_index += struct.calcsize('>II')

    if image_magic_num != 2051 or label_magic_num != 2049:
        return None

    if image_len != label_len:
        return None

    image_list = []
    label_list = []

    for i in range(0, image_len):
        im = struct.unpack_from('>784B', image_raw_data, image_index)
        image_index += struct.calcsize('>784B')

        im = np.array(im, dtype='uint8')
        im = im.reshape(image_cols, image_rows)

        label = struct.unpack_from('>B', label_raw_data, label_index)[0]
        label_index += struct.calcsize('>B')

        image_list.append(im)
        label_list.append(label)

    return image_list, label_list


train_data_ori, train_label = read_image_data('official/mnist_data/train-images.idx3-ubyte',
                                              'official/mnist_data/train-labels.idx1-ubyte')
test_data_ori, test_label = read_image_data('official/mnist_data/t10k-images.idx3-ubyte',
                                            'official/mnist_data/t10k-labels.idx1-ubyte')
train_data_ori = np.array(train_data_ori)
test_data_ori = np.array(test_data_ori)

test_data_ori = test_data_ori[:100]
test_label = test_label[:100]

print("original training data shape:", train_data_ori.shape)
print("original testing data shape:", test_data_ori.shape)

train_data = train_data_ori.reshape(-1, 784)
test_data = test_data_ori.reshape(-1, 784)


def KNN(test_data1, train_data_pca, train_label, k, p):
    subMat = train_data_pca - np.tile(test_data1, (len(train_data_pca), 1))
    subMat = np.abs(subMat)
    distance = subMat ** p
    distance = np.sum(distance, axis=1)
    distance = distance ** (1.0 / p)
    distanceIndex = np.argsort(distance)
    classCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(k):
        label = train_label[distanceIndex[i]]
        classCount[label] = classCount[label] + 1
    return np.argmax(classCount)


pca_h = PCA(n_components=100)
if use_values:
    pca_h.load('model.npy')
else:
    pca_h.fit(train_data)  # fit PCA with training data instead of the whole dataset
    pca_h.save('model.npy')
train_data_pca = pca_h.transform(train_data)
test_data_pca = pca_h.transform(test_data)
print("PCA completed with", pca_h.n_components, "components")
print("training data shape after PCA:", train_data_pca.shape)
print("testing data shape after PCA:", test_data_pca.shape)


def predict(img_list):
    img_list = np.array(img_list).reshape((-1, 28 * 28))
    pca_list = pca_h.transform(img_list)
    return np.array([KNN(x, pca_h.train_compacted, train_label, knn_samples, 2) for x in pca_list])


if __name__ == '__main__':
    print('evaluating')
    m, n = np.shape(test_data_pca)
    count = 0

    M = np.zeros((10, 10), int)
    results = predict(test_data)
    for i in range(m):
        M[test_label[i], results[i]] += 1
        if test_label[i] == results[i]:
            count += 1

    print('accuracy on test data:', count / len(test_data))
    print("Confusion matrix:\n", M)
