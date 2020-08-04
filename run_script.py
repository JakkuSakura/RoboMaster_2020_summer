import image_process_cv
import number_recognition_keras
import correction
import numpy as np
from colorama import Fore, Back, Style
import os
current_dir = os.getcwd()
os.chdir('official/auto_grader')
from official.auto_grader.auto_grader import auto_grader
import time
import pipes
if __name__ == '__main__':
    enable_ui = True
    ag = auto_grader(enable_ui=enable_ui)
    time.sleep(5)
    os.chdir(current_dir)
    images = image_process_cv.get_images()
    print('images:', images.shape)

    gray_images = np.array([image_process_cv.convert_to_gray(x) for x in images])
    print('gray_images:', gray_images.shape)

    colors = np.array([image_process_cv.get_color(x) for x in images])
    print('colors:', colors.shape)

    raw_predict = number_recognition_keras.predict(gray_images)
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
    except:
        print('No solution!')

    for i in range(len(solutions) // 2):
        r1, c1 = solutions[i*2]
        r2, c2 = solutions[i*2+1]
        ag.link(r1, c1, r2, c2)

    input('enter to exit')
