from number_recognition_kNN_PCA import pca_h, train_data_pca, train_label, test_data_pca, test_label, test_data
import numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from joblib import dump, load
from correction import to_one_hot

use_values = True

if not use_values:
    svm = SVC(decision_function_shape="ovr")
    svm.fit(train_data_pca, train_label)
    dump(svm, 'svm.joblib')
else:
    svm = load('svm.joblib')


def predict(img_list):
    img_list = np.array(img_list).reshape((-1, 28 * 28))
    pca_list = pca_h.transform(img_list)
    res = svm.predict(pca_list)
    return res


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
