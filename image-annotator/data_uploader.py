from Data.db_connection import DbConnection
from ModelState.model_state import ModelState
from utils import images_master
from utils.injector import Injector


def annotate_dataset(model_state: ModelState):
    logger = Injector.get_instance('logger')
    logger.log_info("Annotating dataset")

    cnt = 0
    documents = __get_database_documents()
    for img_id, img_np in __images_np_iterator():
        cnt += 1
        print(f"Annotating image {cnt} / {documents}")

        annotated_img_id = __get_annotated_img_id(img_id)
        if annotated_img_id is not None:
            __delete_annotated_img(annotated_img_id)

        annotated_img = model_state.annotate_image(img_np).astype('float32')
        annotated_img *= 255

        __save_annotated_img(img_id, annotated_img)

    logger.log_info("Dataset annotated")


def __get_database_documents():
    with DbConnection() as (db, _):
        documents = db.image_mask_pairs.count_documents({})
        return documents


def __get_annotated_img_id(img_id):
    logger = Injector.get_instance('logger')
    try:
        with DbConnection() as (db, _):
            annotated_img = db.annotated_images.find_one({'img_id': img_id})
            if annotated_img:
                return annotated_img['annotated_img_id']
            return None
    except Exception as e:
        logger.log_error(f"Error while getting annotated image id: {e}")
        return None


def __delete_annotated_img(annotated_img_id):
    logger = Injector.get_instance('logger')
    logger.log_warning("Deleting the annotated image for this image")

    with DbConnection() as (db, fs):
        db.annotated_images.delete_one({'annotated_img_id': annotated_img_id})
        fs.delete(annotated_img_id)


def __images_np_iterator():
    with DbConnection() as (db, fs):
        for entry in db.image_mask_pairs.find():
            img_id = entry['img_id']
            img_np = images_master.get_np_from_gridFs(img_id, fs)

            yield img_id, img_np


def __save_annotated_img(img_id, annotated_img):
    with DbConnection() as (db, fs):
        img_bytes = images_master.get_img_from_np(annotated_img).read()
        annotated_img_id = fs.put(img_bytes)
        db.annotated_images.insert_one({'img_id': img_id, 'annotated_img_id': annotated_img_id})
