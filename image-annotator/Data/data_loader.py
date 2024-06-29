import random

from Data.db_connection import DbConnection
from utils.injector import Injector


class DataLoader:

    def __init__(self, with_load):

        if with_load:
            self.__load_indices()
        else:
            # dataset_split = Injector.get_instance('config')['dataset_split']
            self.training_split = list()
            self.testing_split = list()
            self.validation_split = self.__get_validation_indices()

            # max_available_testing_data = self.__get_minimum_documents()
            # self.__set_indices(max_available_testing_data, dataset_split['testing_percent'])

            for i in range(42):
                self.training_split.append(self.validation_split.pop())

            for i in range(17):
                self.testing_split.append(self.validation_split.pop())

            # self.__save_indices_to_db()

        self.count_testing_indices = len(self.testing_split)
        self.count_training_indices = len(self.training_split)
        self.count_validation_indices = len(self.validation_split)

    def __load_indices(self):
        last_id = DataLoader.__get_last_indices_id('loading')
        with DbConnection() as (db, _):
            indices = db.train_indices.find_one({'_id': last_id})
            self.training_split = indices['training_split']
            self.testing_split = indices['testing_split']
            self.validation_split = indices['validation_split']

    @staticmethod
    def __get_validation_indices():
        with DbConnection() as (db, _):
            query = {"provenience": "endometriosis"}
            results = db.image_mask_pairs.find(query, {"_id": 1})
            ids = [result['_id'] for result in results]
            random.shuffle(ids)
            return ids

    @staticmethod
    def __get_minimum_documents():
        with DbConnection() as (db, _):
            healthy_hearts = db.image_mask_pairs.count_documents({'provenience': 'heart', 'diseased': False})
            healthy_prostates = db.image_mask_pairs.count_documents({'provenience': 'prostate', 'diseased': False})
            diseased_hearts = db.image_mask_pairs.count_documents({'provenience': 'heart', 'diseased': True})
            diseased_prostates = db.image_mask_pairs.count_documents({'provenience': 'prostate', 'diseased': True})

            return min(healthy_hearts, healthy_prostates, diseased_hearts, diseased_prostates)

    def __set_indices(self, max_available_testing_data, training_data_percent):
        healthy_heart_indices = self.__get_indices_for_entry('heart', False)
        diseased_heart_indices = self.__get_indices_for_entry('heart', True)
        healthy_prostate_indices = self.__get_indices_for_entry('prostate', False)
        diseased_prostate_indices = self.__get_indices_for_entry('prostate', True)

        testing_data_amount = int(max_available_testing_data * training_data_percent)

        for i in range(testing_data_amount):
            self.testing_split.append(healthy_heart_indices[i])
            self.testing_split.append(diseased_heart_indices[i])
            self.testing_split.append(healthy_prostate_indices[i])
            self.testing_split.append(diseased_prostate_indices[i])

        for i in range(15):
            self.training_split.append(self.validation_split.pop())

        self.__add_indices_to_training_split(healthy_heart_indices, testing_data_amount)

        self.__add_indices_to_training_split(diseased_heart_indices, testing_data_amount)

        self.__add_indices_to_training_split(healthy_prostate_indices, testing_data_amount)

        self.__add_indices_to_training_split(diseased_prostate_indices, testing_data_amount)

    @staticmethod
    def __get_indices_for_entry(provenience, diseased: bool):
        with DbConnection() as (db, _):
            query = {
                "provenience": provenience,
                "diseased": diseased,
            }
            results = db.image_mask_pairs.find(query)
            ids = [result['_id'] for result in results]
            random.shuffle(ids)
            return ids

    def __add_indices_to_training_split(self, entry_list, starting_point):
        for i in range(starting_point, len(entry_list)):
            self.training_split.append(entry_list[i])

    def __save_indices_to_db(self):
        last_id = self.__get_last_indices_id('saving')
        if last_id is not None:
            self.__delete_last_indices_id(last_id)

        with DbConnection() as (db, _):
            indices = {
                'training_split': list(self.training_split),
                'testing_split': list(self.testing_split),
                'validation_split': list(self.validation_split)
            }
            db.train_indices.insert_one(indices)

    @staticmethod
    def __get_last_indices_id(purpose: str):
        with DbConnection() as (db, _):
            try:
                _id = db.train_indices.find_one(sort=[("date", -1)])['_id']
                return _id
            except:
                logger = Injector.get_instance('logger')
                if purpose == 'saving':
                    logger.log_warning('No preceding indices found. Creating new indices.')
                    return None
                elif purpose == 'loading':
                    logger.log_error('No preceding indices found. Cannot load indices.')
                    exit(1)
                else:
                    logger.log_error('Invalid purpose for loading indices.\n'
                                     'The parameter must be either "saving" or "loading".')
                    exit(1)

    @staticmethod
    def __delete_last_indices_id(last_id):
        logger = Injector.get_instance('logger')
        logger.log_warning("Another set of indices already exists. Deleting the last set in 'no with load' mode.")
        with DbConnection() as (db, _):
            db.train_indices.delete_one({'_id': last_id})
