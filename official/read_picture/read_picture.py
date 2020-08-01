import struct
import numpy as np
from PIL import Image

#读取图片和标签
def read_image_data(image_path,  label_path):
    image_file = open(image_path, 'rb')
    label_file = open(label_path, 'rb')
    
    print("开始读取mnist数据集:图片集:" + str(image_path) + ",标签集:" + str(label_path))
    
    image_raw_data = image_file.read()
    label_raw_data = label_file.read()
    
    print("读取完毕mnist数据集")
    
    image_file.close()
    label_file.close()
    
    image_index = 0
    label_index = 0
    
    image_magic_num, image_len, image_rows, image_cols = struct.unpack_from('>IIII', image_raw_data, image_index)
    label_magic_num, label_len = struct.unpack_from('>II', label_raw_data, label_index)
    
    image_index += struct.calcsize('>IIII')
    label_index += struct.calcsize('>II')
    
    if image_magic_num != 2051 or label_magic_num != 2049:
        print("魔数校验失败")
        return None
    print("魔数校验成功")
    
    if image_len != label_len:
        print("图片集和标签集校核为不相等")
        return None
    print("图片集和标签集长度校核为相等")
    
    
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
    

def image_save(im, rgb, image_name):
    cols, rows = np.shape(im)
    rgb_image = np.zeros((cols, rows, 3))
    
    i = 0
    while i < cols:
        j = 0
        while j < rows:
            num = 0
            while num < 3:
                if num == rgb:
                    rgb_image[i][j][num] = im[i][j]
                else:
                    rgb_image[i][j][num] = 0
                num += 1
            j += 1
        i += 1
    
    img = Image.fromarray(rgb_image.astype('uint8')).convert('RGB')
    img.save(image_name)
    
    
    
    
    
    


if __name__ == "__main__":
    import random
    train_image, train_label = read_image_data('../../mnist_data/train-images.idx3-ubyte', '../../mnist_data/train-labels.idx1-ubyte')
    test_image, test_label = read_image_data('../../mnist_data/train-images.idx3-ubyte', '../../mnist_data/train-labels.idx1-ubyte')
    
    i = 0
    while i < 10:
        image_save(train_image[i], random.randint(0,2), "../../mnist_data/train/"+str(i)+".png")
        i+=1
    
    i = 0
    while i < 10:
        image_save(train_image[i], random.randint(0,2), "../../mnist_data/test/"+str(i)+".png")
        i+=1
    




