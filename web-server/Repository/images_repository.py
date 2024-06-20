from Repository.db_connection import DbConnection


def get_image_as_bytes(img_id):
    with DbConnection() as (_, fs):
        return fs.get(img_id).read()
