import struct
import numpy as np

# 读取图片和标签
def read_image_data(image_path, label_path):
    image_file = open(image_path, 'rb')
    label_file = open(label_path, 'rb')

    image_raw_data = image_file.read()
    label_raw_data = label_file.read()


    image_file.close()
    label_file.close()

    image_index = 0
    label_index = 0

    image_magic_num, image_len, image_rows, image_cols = struct.unpack_from('>IIII', image_raw_data, image_index)
    label_magic_num, label_len = struct.unpack_from('>II', label_raw_data, label_index)

    image_index += struct.calcsize('>IIII')
    label_index += struct.calcsize('>II')

    if image_magic_num != 2051 or label_magic_num != 2049:
        return None

    if image_len != label_len:
        return None


    image_list = []
    label_list = []

    for i in range(0, image_len):
        im = struct.unpack_from('>784B', image_raw_data, image_index)
        image_index += struct.calcsize('>784B')

        im = np.array(im, dtype='uint8')
        im = im.reshape(image_cols, image_rows)

        label = struct.unpack_from('>B', label_raw_data, label_index)[0]
        label_index += struct.calcsize('>B')

        image_list.append(im)
        label_list.append(label)

    return image_list, label_list
