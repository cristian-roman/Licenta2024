from Repository.db_connection import DbConnection


def get_annotation_entry_image_id(img_id):
    with DbConnection() as (db, _):
        return db.annotated_images.find_one({'img_id': img_id})
