import sys

import numpy as np


def to_one_hot(labels):
    l = len(labels)
    r = np.zeros((l, 10))
    r[np.arange(l), np.array(labels)] = 1
    return r


def to_numbers(label):
    if len(label) == 10:  # if it's one hot encoded
        label = label.argmax()
    return label


def get_counts(ans, colors):
    counts = np.zeros((3, 10), dtype=int)
    for i in range(ans.shape[0]):
        counts[colors[i], ans[i]] += 1
    return counts


def get_number_and_correct(raw_predict, color_list):
    counts = get_counts(raw_predict, color_list)
    print('statistics before correction')
    print(counts)

    raw_ans = raw_predict
    # for i in range(raw_ans.shape[0]):
    #     p = raw_ans[i]
    #     assert raw_predict[i][p] > 0.95


    # we want a pair of odd numbers with the same color
    # of which one is only one, while the other has multiple ones
    for c in range(counts.shape[0]):
        one = None
        multi_odd = None
        for i in range(counts.shape[1]):
            if counts[c][i] == 1:
                if one:
                    print("There can only be one number that appears once each color", file=sys.stderr)
                    break
                one = i
            elif counts[c][i] % 2 == 1:
                if multi_odd:
                    print("There can only be one number that appears odd times other than once each color", file=sys.stderr)
                    break
                multi_odd = i
        else:
            continue

        if not ((one is not None and multi_odd is not None)
                or (one is None and multi_odd is None)):
            print("There can only be an even number of odds", file=sys.stderr)
            continue

        if one is not None and multi_odd is not None:
            for i in range(raw_ans.shape[0]):
                if raw_ans[i] == one:
                    raw_ans[i] = multi_odd

    counts = get_counts(raw_ans, color_list)
    print('statistics after correction')
    print(counts)
    return raw_ans
