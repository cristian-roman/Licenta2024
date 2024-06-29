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


def get_img_from_np(np_array):
    # Ensure the array is in the correct format (uint8)
    if np_array.dtype != np.uint8:
        np_array = (255 * (np_array - np_array.min()) / (np_array.max() - np_array.min())).astype(np.uint8)

    # Convert the NumPy array to an image using OpenCV
    is_success, buffer = cv2.imencode('.png', np_array)

    # Convert buffer to BytesIO object
    buf = BytesIO(buffer)

    return buf


def get_np_from_image_bytes(img_bytes):
    img = plt.imread(BytesIO(img_bytes), format='PNG')
    img = resize_np(img, (320, 320))
    if len(img.shape) == 3:
        img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    return img
