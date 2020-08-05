import sys

import numpy as np


def to_numbers(labels):
    if len(labels) == 10:  # if it's one hot encoded
        labels = np.array([one_hot_label.argmax() for one_hot_label in labels])
    return labels


def get_counts(ans, colors):
    counts = np.zeros((3, 10), dtype=int)
    for i in range(ans.shape[0]):
        counts[colors[i], ans[i]] += 1
    return counts


def get_number_and_correct(raw_predict, color_list):
    raw_ans = to_numbers(raw_predict)
    # for i in range(raw_ans.shape[0]):
    #     p = raw_ans[i]
    #     assert raw_predict[i][p] > 0.95

    counts = get_counts(raw_ans, color_list)
    print('statistics before correction')
    print(counts)

    # we want a pair of odd numbers with the same color
    # of which one is only one, while the other has multiple ones
    for c in range(counts.shape[0]):
        one = None
        multi_odd = None
        for i in range(counts.shape[1]):
            if counts[c][i] == 1:
                one = i
            elif counts[c][i] % 2 == 1:
                multi_odd = i

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
