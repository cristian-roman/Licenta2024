import numpy as np

from Repository import image_mask_repository, images_repository, annotated_images_repository
from utils import images_master


def get_images_count(provenience_filter, health_state_filter):
    diseased = None
    if health_state_filter == 'diseased':
        diseased = True
    elif health_state_filter == 'healthy':
        diseased = False

    answer = image_mask_repository.count_entries(provenience_filter, diseased)
    return answer


def get_image(provenience_filter, health_state_filter, index, _type):
    entry = __get_image_mask_entry_after_index(provenience_filter, health_state_filter, index)

    if _type == 'image' or _type == 'ai':
        id_field = 'img_id'
    elif _type == 'mask' or _type == 'averaged_mask':
        id_field = 'mask_id'
    else:
        raise ValueError("Invalid type")

    fs_id = entry[id_field]

    if _type == 'ai':
        annotation_entry = annotated_images_repository.get_annotation_entry_image_id(fs_id)
        image_bytes = images_repository.get_image_as_bytes(annotation_entry['annotated_img_id'])

    else:
        image_bytes = images_repository.get_image_as_bytes(fs_id)

        if _type == 'averaged_mask':
            np_image = images_master.get_np_from_image_bytes(image_bytes)
            threshold = 0.58
            np_image = np.where(np_image >= threshold, 255, 0)
            image_bytes = images_master.get_img_bytes_from_np(np_image)

    return image_bytes


def __get_image_mask_entry_after_index(provenience_filter, health_state_filter, index):
    diseased = None
    if health_state_filter == 'diseased':
        diseased = True
    elif health_state_filter == 'healthy':
        diseased = False

    return image_mask_repository.get_entry_after_index(provenience_filter, diseased, index)
