import os

from utils.injector import Injector


def __get_absolute_path(tar_folder_location, relative_path):
    absolute_path = os.path.join(tar_folder_location, relative_path)
    if not os.path.exists(absolute_path):
        relative_path = relative_path[2:]
        absolute_path = os.path.join(tar_folder_location, relative_path)
        if not os.path.exists(absolute_path):
            raise FileNotFoundError(f"File {relative_path} not found")
    return absolute_path


def image_mask_abs_path_iterator(tar_folder_location, dataset_json):
    logger = Injector.get_instance("logger")
    relative_path_pairs = dataset_json['training']

    for relative_path in relative_path_pairs:
        tr_image_relative_path = relative_path['image']
        ts_image_relative_path = relative_path['label']
        try:
            tr_image_absolute_path = __get_absolute_path(tar_folder_location, tr_image_relative_path)
            ts_image_absolute_path = __get_absolute_path(tar_folder_location, ts_image_relative_path)
        except FileNotFoundError as e:
            logger.log_error(str(e))
            continue

        yield tr_image_absolute_path, ts_image_absolute_path
