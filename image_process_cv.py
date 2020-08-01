import cv2
import numpy as np


def get_images():
    images = []
    for i in range(64):
        img = cv2.imread('official/auto_grader/image/%d.png' % i)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        images.append(img)
    return np.array(images)


def get_color(img):
    R, G, B = cv2.split(img)
    r = np.sum(R)
    g = np.sum(G)
    b = np.sum(B)

    max = np.argmax([r, g, b])
    return max


def convert_to_gray(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img
