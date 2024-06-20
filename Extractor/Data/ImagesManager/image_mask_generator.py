import os

from utils.images_master import get_np_from_img_location
from utils.injector import Injector


def image_mask_iterator():
    logger = Injector.get_instance("logger")

    images_name = "eco.jpg"
    masks_name = "mask.jpg"

    for directory in __directories_iterator():
        provenience = directory.lower()

        directory_path = str(os.path.join(Injector.get_instance("config")["dataset_path"], directory))
        entries = os.listdir(directory_path)
        for entry in entries:
            try:
                image_location = os.path.join(directory_path, entry, images_name)
                mask_location = os.path.join(directory_path, entry, masks_name)

                img_np = get_np_from_img_location(image_location)
                mask_np = get_np_from_img_location(mask_location)

                yield img_np, mask_np, provenience
            except Exception as e:
                logger.log_error(f"Error while processing {entry} in {directory}. Error: {e}")
                continue


def __directories_iterator():
    config = Injector.get_instance("config")

    for directory in config["images_directories"]:
        yield directory
