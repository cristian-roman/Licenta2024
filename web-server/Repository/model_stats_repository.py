from Repository.db_connection import DbConnection


def get_entry():
    with DbConnection() as (db, _):
        return db.model_stats.find_one({})
