from threading import Thread

import numpy as np

from db_connection import DbConnection


class ImagesStats:
    def __init__(self, _type, modified):
        self.type = _type
        self.modified = modified
        self.unique_sizes = dict()
        self.unique_sizes_count = 0
        self.unique_np_values_count = 0
        self.max_np_value = 0.0
        self.min_np_value = 0.0
        self.weighted_average_np_value = 0

        self.unique_np_values = dict()

    def update_statistics(self, np_img):
        img_shape_str = f"{np_img.shape[0]}x{np_img.shape[1]}"
        if img_shape_str not in self.unique_sizes:
            self.unique_sizes[img_shape_str] = 1
            self.unique_sizes_count += 1
        else:
            self.unique_sizes[img_shape_str] += 1

        self.unique_np_values_count += len(np.unique(np_img))
        self.max_np_value = max(self.max_np_value, float(np_img.max()))
        self.min_np_value = min(self.min_np_value, float(np_img.min()))

        for value in np_img.flatten():
            np_value_key = float(value)

            if np_value_key not in self.unique_np_values:
                self.unique_np_values[np_value_key] = 1
            else:
                self.unique_np_values[np_value_key] += 1

    def save_to_db(self, threads):
        self.weighted_average_np_value = self.__get_weighted_average()
        del self.unique_np_values

        def save_task():
            with DbConnection() as (db, fs):
                db.images_stats.insert_one(self.__dict__)

        thr = Thread(target=save_task)
        thr.start()
        threads.append(thr)

    def __get_weighted_average(self):
        total_values = 0
        total_sum = 0

        for key, value in self.unique_np_values.items():
            total_values += value
            total_sum += key * value

        return total_sum / total_values
