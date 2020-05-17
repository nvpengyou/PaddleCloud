from io import BytesIO
import numpy as np
import os
import random
import zipfile
from PIL import Image

def arc_train(data_dir):
    label_file = os.path.join(data_dir, 'label.txt')
    zip_file = zipfile.ZipFile(os.path.join(data_dir, 'images.zip'), 'r')
    train_image_list = None
    with open(label_file, 'r') as f:
        train_image_list = f.readlines()
    random.shuffle(train_image_list)

    def reader():
        for j in range(len(train_image_list)):
            path, label = train_image_list[j].split()
            bytes_image = zip_file.read(path)
            img = Image.open(BytesIO(bytes_image))
            if random.randint(0, 1) == 1:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img = np.array(img).astype('float32').transpose((2, 0, 1))
            yield img, label

    return reader
