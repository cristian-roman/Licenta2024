from Repository.db_connection import DbConnection


def get_all_entries(provenience, diseased: bool):
    assert provenience in ["all", "heart", "prostate", "endometriosis"]
    with DbConnection() as (db, _):
        query = {"provenience": provenience, "diseased": diseased}
        return db.image_mask.find(query)


def count_entries(provenience, diseased=None):
    assert provenience in ["all", "heart", "prostate", "endometriosis"]
    with DbConnection() as (db, _):
        query = {}
        if provenience != "all":
            query["provenience"] = provenience
        if diseased is not None:
            query["diseased"] = diseased
        return db.image_mask_pairs.count_documents(query)


def get_entry_after_index(provenience, diseased: bool, index):
    assert provenience in ["all", "heart", "prostate", "endometriosis"]
    with DbConnection() as (db, _):
        query = {}
        if provenience != "all":
            query["provenience"] = provenience
        if diseased is not None:
            query["diseased"] = diseased
        return db.image_mask_pairs.find(query).skip(index - 1).limit(1).next()
