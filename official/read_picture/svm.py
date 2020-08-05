import numpy as np
import numpy.random as npr

def svm(pts, labels):
    """
    Support Vector Machine using CVXOPT in Python. This example is
    mean to illustrate how SVMs work.
    """
    n = len(pts[0])

    # x is a column vector [w b]^T

    # set up P
    P = np.eye(n+1)

    # q^t x
    # set up q
    q = matrix(0.0, (n + 1, 1))
    q[-1] = 1.0

    m = len(pts)
    # set up h
    h = matrix(-1.0, (m, 1))

    # set up G
    G = matrix(0.0, (m, n + 1))
    for i in range(m):
        G[i, :n] = -labels[i] * pts[i]
        G[i, n] = -labels[i]

    x = solvers.qp(P, q, G, h)['x']

    return P, q, h, G, x


if __name__ == '__main__':

    def create_overlapping_classification_problem(n=100):
        import gmm

        n1 = gmm.Normal(2, mu=[0, 0], sigma=[[1, 0], [0, 1]])
        n2 = gmm.Normal(2, mu=[0, 3], sigma=[[1, 0], [0, 1]])
        class1 = n1.simulate(n / 2)
        class2 = n2.simulate(n / 2)

        samples = np.vstack([class1, class2])

        labels = np.zeros(n)
        labels[:n / 2] = -1
        labels[n / 2:] = 1

        return samples, labels


    def create_classification_problem(n=100):
        class1 = npr.rand(n / 2, 2)
        class2 = npr.rand(n / 2, 2) + np.array([1.3, 0.0])

        theta = np.pi / 8.0
        r = np.cos(theta)
        s = np.sin(theta)
        rotation = np.array([[r, s], [s, -r]])

        samples = np.dot(np.vstack([class1, class2]), rotation)

        labels = np.zeros(n)
        labels[:n / 2] = -1
        labels[n / 2:] = 1
        return samples, labels


    if True:
        samples, labels = create_overlapping_classification_problem()

        c = ['red'] * 50 + ['blue'] * 50
        pylab.scatter(samples[:, 0], samples[:, 1], color=c)

        # import pdb
        # pdb.set_trace()
        P, q, h, G, x = svm_slack(samples, labels, c=2.0)
        # print P, q, h, G
        line_params = list(x[:2]) + [x[-1]]

        xlim = pylab.gca().get_xlim()
        ylim = pylab.gca().get_ylim()
        print
        xlim, ylim

        plot_line(line_params, xlim, ylim)
        print
        line_params

        pylab.show()

    if False:
        samples, labels = create_classification_problem()
        P, q, h, G, x = svm(samples, labels)
        print
        x

    if False:
        c = ['red'] * 50 + ['blue'] * 50
        pylab.scatter(samples[:, 0], samples[:, 1], color=c)

        xlim = pylab.gca().get_xlim()
        ylim = pylab.gca().get_ylim()
        print
        xlim, ylim

        plot_line(x, xlim, ylim)
        pylab.show()
