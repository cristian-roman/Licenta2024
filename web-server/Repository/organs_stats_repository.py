from Repository.db_connection import DbConnection


def get_entry(provenience):
    assert provenience in ["heart", "prostate", "endometriosis"]
    with DbConnection() as (db, _):
        query = {"provenience": provenience}
        return db.organs_stats.find_one(query)
