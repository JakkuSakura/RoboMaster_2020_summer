import numpy as np


class PCA:
    def __init__(self, n_components):
        self.n_components = n_components
        self.mean = None
        self.eigenvalues = None
        self.eigenvectors = None
        self.train_compacted = None

    def fit(self, data_ori):
        data = np.array(data_ori).reshape((len(data_ori), -1))
        self.mean = data.mean(axis=0)
        data = data - self.mean
        cov = np.cov(data.T) / data.shape[0]  # Get covariance matrix
        v, w = np.linalg.eig(cov)

        idx = v.argsort()[::-1]  # Sort descending and get sorted indices
        self.eigenvalues = v[idx]

        self.eigenvectors = w[:, idx]
        self.train_compacted = self.transform(data_ori)

    def transform(self, data):
        data = np.array(data)
        if len(data.shape) == 1:
            data = data.reshape((1, -1))
        data = data - self.mean
        return data.dot(self.eigenvectors[:, :self.n_components])

    def save(self, filename):
        with open(filename, 'wb') as f:
            np.save(f, self.mean)
            np.save(f, self.eigenvalues)
            np.save(f, self.eigenvectors)
            np.save(f, self.train_compacted)

    def load(self, filename):
        with open(filename, 'rb') as f:
            self.mean = np.load(f)
            self.eigenvalues = np.load(f)
            self.eigenvectors = np.load(f)
            self.train_compacted = np.load(f)
