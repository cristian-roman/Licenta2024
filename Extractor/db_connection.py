from gridfs import GridFS
from pymongo import MongoClient

from utils.injector import Injector


class DbConnection:
    def __enter__(self):
        secrets = Injector.get_instance('secrets')

        self.db_name = secrets['mongodb_database']
        self.username = secrets['mongodb_username']
        self.password = secrets['mongodb_password']

        while True:
            try:
                self.client = MongoClient(f"mongodb://{self.username}:{self.password}@localhost:27017/")
                self.db = self.client[self.db_name]
                self.fs = GridFS(self.db)
                return self.db, self.fs
            except Exception as e:
                logger = Injector.get_instance("logger")
                logger.log_error(f"Error while connecting to database. Error: {e}")
                logger.log_warning("Retrying connection...")
                continue

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
