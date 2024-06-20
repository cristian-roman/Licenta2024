from Repository.db_connection import DbConnection


def get_entry(_type, modified: bool):
    assert _type in ["images", "masks"], "Invalid type. Must be 'images' or 'masks'."
    with DbConnection() as (db, _):
        query = {"type": _type, "modified": modified}
        return db.images_stats.find_one(query)
