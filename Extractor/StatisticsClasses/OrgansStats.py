import json
from threading import Thread

from db_connection import DbConnection


class OrganStats:
    def __init__(self, provenience: str):
        self.provenience = provenience
        self.slices = 0
        self.diseased = 0
        self.healthy = 0

    def update_statistics(self, mask_np):
        self.slices += 1

        if any(mask_np.flatten() > 0):
            self.diseased += 1
        else:
            self.healthy += 1

    def save_to_db(self, threads):

        def save_task():
            with DbConnection() as (db, fs):
                db.organs_stats.insert_one(self.__dict__)

        thr = Thread(target=save_task)
        thr.start()
        threads.append(thr)
