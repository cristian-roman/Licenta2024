import os
from threading import Thread, Lock

import db_images
from Data.aggregator import image_mask_aggregator
from StatisticsClasses.ImagesStats import ImagesStats
from StatisticsClasses.OrgansStats import OrganStats
from app_init.init import register_dependencies
from db_connection import DbConnection
from utils.images_master import resize_np
from utils.injector import Injector

unmodified_images_stats = ImagesStats("images", False)
modified_images_stats = ImagesStats("images", True)
unmodified_masks_stats = ImagesStats("masks", False)
modified_masks_stats = ImagesStats("masks", True)


def main():
    global unmodified_images_stats, \
        modified_images_stats, \
        unmodified_masks_stats, \
        modified_masks_stats

    register_dependencies()
    os.system("sh create_mongo_docker.sh")

    logger = Injector.get_instance("logger")
    workers = 10
    threads = []
    organs_stats_classes = dict()
    pairs = 0
    locker = Lock()
    for image, mask, provenience in image_mask_aggregator():
        if provenience not in organs_stats_classes:
            organs_stats_classes[provenience] = OrganStats(provenience)
        organ_stats = organs_stats_classes[provenience]

        organ_stats.update_statistics(mask)

        unmodified_images_stats.update_statistics(image)
        unmodified_masks_stats.update_statistics(mask)

        image, mask = modify_image_mask(image, mask)

        modified_images_stats.update_statistics(image)
        modified_masks_stats.update_statistics(mask)

        thr = Thread(target=db_images.save_np_pair_to_db, args=(image, mask, provenience, locker))
        thr.start()
        threads.append(thr)

        pairs += 1
        logger.log_info("Image saved and statistics updated..............pair: " + str(pairs))
        while len(threads) >= workers:
            for thr in threads:
                if not thr.is_alive():
                    threads.remove(thr)
                    thr.join()

    for thread in threads:
        thread.join()

    log_saved_pairs_counter()

    threads = []
    for organ_stats in organs_stats_classes.values():
        organ_stats.save_to_db(threads)

    unmodified_images_stats.save_to_db(threads)
    modified_images_stats.save_to_db(threads)
    unmodified_masks_stats.save_to_db(threads)
    modified_masks_stats.save_to_db(threads)

    for thread in threads:
        thread.join()

    logger = Injector.get_instance("logger")
    logger.log_info("Stats saved to database. Program finished.")


def modify_image_mask(image, mask):
    size = (320, 320)
    mask[mask == 2.0] = 1.0

    image = resize_np(image, size)
    mask = resize_np(mask, size)

    return image, mask


def log_saved_pairs_counter():
    logger = Injector.get_instance("logger")
    with DbConnection() as (db, fs):
        saved_pairs = db.image_mask_pairs.count_documents({})
        logger.log_info(f"Saved {saved_pairs} image-mask pairs to database.")


if __name__ == "__main__":
    main()
