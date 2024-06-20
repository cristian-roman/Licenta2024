import socket

import numpy as np

from utils.common.injector import Injector


def send_image_to_server(img_bytes):
    host = 'localhost'
    port = 5432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            logger = Injector.get_instance('logger')
            logger.log_info('Connected to server')

            __send_image(img_bytes, s)

            annotated_img = __recv_annotated_image(s)
            return annotated_img

    except Exception as e:
        logger = Injector.get_instance('logger')
        logger.log_error(f'Error: {e}')
        return None


def __send_image(img_bytes, s):
    packets = len(img_bytes) / 1024
    if len(img_bytes) % 1024 != 0:
        packets += 1

    packets = int(packets)
    s.send(packets.to_bytes(4, 'big'))

    logger = Injector.get_instance('logger')
    logger.log_info(f'Sending {packets} packets')

    for i in range(int(packets)):
        end = min(len(img_bytes), (i + 1) * 1024)
        s.send(img_bytes[i * 1024:end])

    logger.log_info('Image sent')


def __recv_annotated_image(s):
    lng_bytes = s.recv(4)
    lng = int.from_bytes(lng_bytes, 'big')
    buffer = b''
    while len(buffer) < lng:
        buffer += s.recv(lng - len(buffer))
    x = np.frombuffer(buffer, dtype='uint8').reshape(320, 320)
    logger = Injector.get_instance('logger')
    logger.log_info(f'Image received: {x.shape}')
    return x
