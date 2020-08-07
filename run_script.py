import image_process_cv
from number_recognition_kNN_PCA import predict as predict_knn
from number_recognition_svm_PCA import predict as predict_svm
from number_recognition_keras import predict as predict_cnn
import correction
import numpy as np
from colorama import Fore, Back, Style
import os

current_dir = os.getcwd()
os.chdir('official/auto_grader')
from official.auto_grader.auto_grader import auto_grader
import time


class status:
    def __init__(self, ans):
        self.ans = ans

    def write_status(self, file='map.txt'):
        with open(file, 'w') as f:
            for x in self.ans:
                print(x, end=' ', file=f)
            print(file=f)

    def print_status(self):
        print('Status: ')
        for x in self.ans:
            print(x, end=' ')
        print()

    def is_ok(self):
        for x in self.ans:
            if x != 0:
                return False

        return True


if __name__ == '__main__':
    enable_ui = True
    ag = auto_grader(enable_ui=enable_ui)
    print('waiting')
    time.sleep(3)
    os.chdir(current_dir)
    images = image_process_cv.get_images()
    print('images:', images.shape)

    gray_images = np.array([image_process_cv.convert_to_gray(x) for x in images])
    print('gray_images:', gray_images.shape)

    colors = np.array([image_process_cv.get_color(x) for x in images])
    print('colors:', colors.shape)

    predict_funcs = [('knn', predict_knn), ('svm', predict_svm), ('cnn', predict_cnn)]
    # predict_funcs = [('svm', predict_svm)]

    pl = len(predict_funcs)
    predicts = np.zeros((64, pl), dtype=int)
    for i in range(pl):
        print('predicting using', predict_funcs[i][0])
        res = predict_funcs[i][1](gray_images)
        for j in range(64):
            predicts[j, i] = res[j]

    raw_predict = np.zeros(64, dtype=int)
    for i in range(64):
        counts = np.bincount(predicts[i])
        raw_predict[i] = np.argmax(counts)

    print('raw_predict', raw_predict)

    numbers = correction.get_number_and_correct(raw_predict, colors)
    print('numbers: ', numbers.shape)

    if enable_ui:
        color_dict = ['R', 'G', 'B']
    else:
        color_dict = [Fore.RED, Fore.GREEN, Fore.BLUE]
    ans_list = [numbers[i] + 10 * (colors[i] + 1) for i in range(64)]

    for i in range(8):
        for j in range(8):
            if enable_ui:
                print(str(numbers[i * 8 + j]) + color_dict[colors[i * 8 + j]], end=', ')
            else:
                print(color_dict[colors[i * 8 + j]], numbers[i * 8 + j], end=' ')
        print()
    if not enable_ui:
        print(Style.RESET_ALL)
    s = status(ans_list)

    try:
        while not s.is_ok():
            s.write_status()
            s.print_status()
            os.system('./algorithms/solution <map.txt >solution.txt')
            with open('solution.txt', 'r') as f:
                line = f.readline().strip()
                if line:
                    solutions = [(int(x) // 8, int(x) % 8) for x in line.split(' ')]
                    for i in range(len(solutions) // 2):
                        r1, c1 = solutions[i * 2]
                        r2, c2 = solutions[i * 2 + 1]
                        result = ag.link(r1, c1, r2, c2)
                        if isinstance(result, list):
                            # We got a problem
                            co1, n1 = result[0]
                            co2, n2 = result[1]
                            s.ans[r1 * 8 + c1] = (co1 + 1) * 10 + n1
                            s.ans[r2 * 8 + c2] = (co2 + 1) * 10 + n2
                            break  # for
                        else:
                            s.ans[r1 * 8 + c1] = 0
                            s.ans[r2 * 8 + c2] = 0
                else:
                    for i in range(len(s.ans)):
                        if s.ans[i] != 0:
                            s.ans[i] = s.ans[i] // 10 * 10
                            # change everything in the same color to zero



    except Exception as e:
        print(e)

    input('enter to exit')
