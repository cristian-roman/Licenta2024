from io import BytesIO

import cv2
import numpy as np
from matplotlib import pyplot as plt


def get_np_from_img_location(img_location):
    img_np = cv2.imread(img_location)
    if len(img_np.shape) == 3:
        img_np = np.dot(img_np[..., :3], [0.2989, 0.5870, 0.1140])
    return img_np


def resize_np(np_img, size):
    return cv2.resize(np_img, size)


def get_img_bytes_from_np(np_array):
    fig, ax = plt.subplots()
    ax.imshow(np_array, cmap='gray')
    ax.axis('off')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
    plt.close(fig)
    buf.seek(0)
    return buf


def get_np_from_image_bytes(img_bytes):
    img = plt.imread(BytesIO(img_bytes), format='JPG')
    img = resize_np(img, (320, 320))
    if len(img.shape) == 3:
        img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    return img
