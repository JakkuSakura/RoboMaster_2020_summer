import image_process_cv
import number_recognition_keras
import numpy as np
from colorama import Fore, Back, Style

def to_numbers(one_hot_labels):
    labels = np.array([one_hot_label.argmax() for one_hot_label in one_hot_labels])
    return labels


if __name__ == '__main__':
    images = image_process_cv.get_images()
    print('images:', images.shape)

    gray_images = np.array([image_process_cv.convert_to_gray(x) for x in images])
    print('gray_images:', gray_images.shape)

    colors = np.array([image_process_cv.get_color(x) for x in images])
    print('colors:', colors.shape)

    numbers = to_numbers(number_recognition_keras.predict(gray_images))
    print('numbers: ', numbers.shape)

    # color_dict = ['R', 'G', 'B']
    color_dict = [Fore.RED, Fore.GREEN, Fore.BLUE]
    ans_list = [numbers[i] + 10 * (colors[i] + 1) for i in range(64)]

    for i in range(8):
        for j in range(8):
            # print(str(numbers[i * 8 + j]) + color_dict[colors[i * 8 + j]], end=', ')
            print(color_dict[colors[i*8+j]], numbers[i*8+j], end=' ')
        print()
    print(Style.RESET_ALL)
    print('Below is for other programs')
    for x in ans_list:
        print(x, end=' ')
    print()

