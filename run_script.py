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
                print(color_dict[colors[i*8+j]], numbers[i*8+j], end=' ')
        print()
    if not enable_ui:
        print(Style.RESET_ALL)
    print('Below is for other programs')
    for x in ans_list:
        print(x, end=' ')
    print()
    with open('map.txt', 'w') as f:
        for x in ans_list:
            print(x, end=' ', file=f)
        print(file=f)
    os.system('./algorithms/solution <map.txt >solution.txt')

    try:
        with open('solution.txt', 'r') as f:
            solutions = [(int(x) // 8, int(x) % 8) for x in f.readline().strip().split(' ')]
        for i in range(len(solutions) // 2):
            r1, c1 = solutions[i*2]
            r2, c2 = solutions[i*2+1]
            ag.link(r1, c1, r2, c2)
    except:
        print('No solution!')


    input('enter to exit')
