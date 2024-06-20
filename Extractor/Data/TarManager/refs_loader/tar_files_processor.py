import os
from queue import Queue
from threading import Event, Thread
import nibabel as nib

from Data.TarManager.refs_loader.utils.image_mask_abs_path import image_mask_abs_path_iterator
from utils.os_interactor import unzip_file, load_json_document, delete_folder, delete_file
from utils.injector import Injector


def extract_references(concurrently_tar_files_counter: int, image_mask_ref_pairs: Queue):
    close_flag = Event()
    Injector.register_instance('tar_files_processor_closing_flag', close_flag)

    logger = Injector.get_instance("logger")
    threads = []

    for tar_file in tar_files_iterator():
        logger.log_debug(f"Processing {tar_file}")

        if close_flag.is_set():
            break

        if concurrently_tar_files_counter == 1:
            __extract_reference(tar_file, image_mask_ref_pairs)
            continue

        else:
            thr = Thread(target=__extract_reference, args=(tar_file, image_mask_ref_pairs))
            thr.start()
            threads.append(thr)
            while len(threads) == concurrently_tar_files_counter:
                for thread in threads:
                    if not thread.is_alive():
                        threads.remove(thread)
                        thread.join()

    for thread in threads:
        thread.join()
    image_mask_ref_pairs.put(None)

    while not close_flag.is_set():
        pass

    for tar_file in tar_files_iterator():
        __delete_unzipped_folder(tar_file)
        __delete_hidden_file(tar_file)


def tar_files_iterator():
    config = Injector.get_instance("config")
    tar_files = config["tar_files"]
    for tar_file in tar_files:
        yield tar_file


def __get_organ_provenience(tar_file):
    organ_tar = tar_file.split('_')[1]
    organ = organ_tar.split('.')[0]
    lowercase_organ = organ.lower()
    return lowercase_organ


def __extract_reference(tar_file, image_mask_ref_pairs: Queue):
    logger = Injector.get_instance("logger")
    close_flag = Injector.get_instance("tar_files_processor_closing_flag")

    unzipped_folder_location = __unzip_tar_file(tar_file)

    dataset_json = __parse_dataset_json(unzipped_folder_location)

    for nib_abs_path_pair in image_mask_abs_path_iterator(unzipped_folder_location, dataset_json):
        tr_nib_path, ts_nib_path = nib_abs_path_pair
        tr_nib = nib.load(tr_nib_path)
        ts_nib = nib.load(ts_nib_path)

        if close_flag.is_set():
            logger.log_info("Closing flag set before finishing adding all pairs to the queue.\n"
                            f"Closing thread for {tar_file}")
            break

        source = __get_organ_provenience(tar_file)
        image_mask_ref_pairs.put((tr_nib, ts_nib, source))
        logger.log_debug(f"Added a new pair to the queue:\n"
                         f"Training image: {tr_nib_path}\n"
                         f"Test image: {ts_nib_path}\n\n")

    logger.log_info(f"[tar_files_process] Finished extracting nib images from {tar_file}. Closing thread")


def __unzip_tar_file(tar_file):
    logger = Injector.get_instance("logger")
    unzipped_folder_location = __get_unzipped_folder_location(tar_file)

    if not os.path.exists(unzipped_folder_location):
        logger.log_debug(f"Unzipping file {tar_file}")

        unzip_file(
            __get_tar_file_location(tar_file),
            __get_tar_files_dir_path()
        )

        logger.log_debug(f"Unzipping file {tar_file} - Done")
    else:
        logger.log_debug(f"Folder {unzipped_folder_location} already exists")

    return unzipped_folder_location


def __get_tar_files_dir_path():
    config = Injector.get_instance("config")

    dataset_path = config["dataset_path"]
    tar_files_directory = config["tar_files_directory"]

    return str(os.path.join(dataset_path, tar_files_directory))


def __get_unzipped_folder_location(tar_file):
    unzipped_folder_name = tar_file.split('.')[0]
    return str(os.path.join(__get_tar_files_dir_path(), unzipped_folder_name))


def __get_tar_file_location(tar_file):
    return str(os.path.join(__get_tar_files_dir_path(), tar_file))


def __parse_dataset_json(unzipped_folder_location):
    logger = Injector.get_instance("logger")

    logger.log_debug(f"Parsing 'dataset.json' file")

    dataset_json_file_path = os.path.join(unzipped_folder_location, 'dataset.json')
    dataset_json = load_json_document(dataset_json_file_path)

    logger.log_debug(f"Parsing 'dataset.json' file - Done")
    return dataset_json


def __delete_unzipped_folder(tar_file):
    logger = Injector.get_instance("logger")
    unzipped_folder_location = __get_unzipped_folder_location(tar_file)

    logger.log_debug(f"Deleting folder {unzipped_folder_location}")
    delete_folder(unzipped_folder_location)
    logger.log_debug(f"Deleting folder {unzipped_folder_location} - Done")


def __delete_hidden_file(tar_file):
    logger = Injector.get_instance("logger")
    tar_file_name = tar_file.split('.')[0]

    logger.log_debug("Deleting any hidden file")

    hidden_file_name = f"._{tar_file_name}"
    hidden_file_path = os.path.join(__get_tar_files_dir_path(), hidden_file_name)
    delete_file(hidden_file_path)

    logger.log_debug("Deleting any hidden file - Done")
