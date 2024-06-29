from threading import Lock

from db_connection import DbConnection
from utils.images_master import get_img_from_np


def save_np_pair_to_db(img_np, mask_np, provenience, locker: Lock):
    img_from_np = get_img_from_np(img_np, locker)
    mask_from_np = get_img_from_np(mask_np, locker)

    diseased = __is_diseased(mask_np)

    with DbConnection() as (db, fs):
        img_id = __save_np_as_image(img_from_np, fs)
        mask_id = __save_np_as_image(mask_from_np, fs)

        db.image_mask_pairs.insert_one({"provenience": provenience,
                                        "img_id": img_id,
                                        "mask_id": mask_id,
                                        "diseased": diseased})


def __save_np_as_image(img_from_np, fs):
    img_id = fs.put(img_from_np)
    return img_id


def __is_diseased(mask_np):
    return any(mask_np.flatten() > 0)
