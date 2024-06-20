from Data.data_loader import DataLoader
from Data.db_connection import DbConnection
from utils.images_master import get_np_from_gridFs


class DataProvider(DataLoader):

    def __init__(self, with_load):
        super().__init__(with_load)

    def training_data_iterator(self):
        cnt = 0
        for _id in self.training_split:
            entry = self.__get_db_entry(_id)
            img_id = entry['img_id']
            mask_id = entry['mask_id']

            img_np = get_np_from_gridFs(img_id)
            mask_np = get_np_from_gridFs(mask_id)

            cnt += 1
            yield img_np, mask_np, cnt

    def testing_data_iterator(self):
        cnt = 0
        for _id in self.testing_split:
            entry = self.__get_db_entry(_id)
            img_id = entry['img_id']
            mask_id = entry['mask_id']

            img_np = get_np_from_gridFs(img_id)
            mask_np = get_np_from_gridFs(mask_id)

            cnt += 1
            yield img_np, mask_np, cnt

    def validation_data_iterator(self):
        cnt = 0
        for _id in self.validation_split:
            entry = self.__get_db_entry(_id)
            img_id = entry['img_id']
            mask_id = entry['mask_id']

            img_np = get_np_from_gridFs(img_id)
            mask_np = get_np_from_gridFs(mask_id)

            cnt += 1
            yield img_np, mask_np, cnt

    @staticmethod
    def __get_db_entry(_id):
        with DbConnection() as (db, _):
            return db.image_mask_pairs.find_one({'_id': _id})
