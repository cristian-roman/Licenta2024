from queue import Queue
from threading import Thread

from utils.injector import Injector
from Data.TarManager.refs_loader.image_mask_ref_generator import image_mask_ref_iterator


def image_mask_np_iterator(max_in_memory_np_pairs):
    logger = Injector.get_instance("logger")
    logger.log_debug("Extracting np arrays from nib images started.")

    np_image_mask_queue = Queue(max_in_memory_np_pairs)

    t = Thread(target=__extract_np_pairs, args=(np_image_mask_queue,))
    t.start()

    np_package = np_image_mask_queue.get()
    while np_package is not None:
        yield np_package
        np_package = np_image_mask_queue.get()
    t.join()


def __extract_np_pairs(np_image_mask_queue: Queue):
    logger = Injector.get_instance("logger")
    logger.log_info("[refs_to_np] [image_mask_np_generator] Extracting np arrays from nib references started.")

    workers = 5
    threads = []
    for nib_package in image_mask_ref_iterator(2):
        if nib_package is None:
            break
        # __fetch_np_from_refs(nib_package, np_image_mask_queue)
        thr = Thread(target=__fetch_np_from_refs, args=(nib_package, np_image_mask_queue))
        thr.start()
        threads.append(thr)

        while len(threads) >= workers:
            for thr in threads:
                if not thr.is_alive():
                    threads.remove(thr)
                    thr.join()

    for thr in threads:
        thr.join()

    np_image_mask_queue.put(None)
    logger.log_info("[refs_to_np] [image_mask_np_generator] Extracting np arrays from nib references finished.")

    __allow_deletion_of_unzipped_folders()


def __fetch_np_from_refs(nib_package, result_queue):
    try:
        tr_img_nib, ts_img_nib, provenience = nib_package
        local_tr_np = tr_img_nib.get_fdata()
        local_ts_np = ts_img_nib.get_fdata()
        result_queue.put((local_tr_np, local_ts_np, provenience))
    except:
        return


def __allow_deletion_of_unzipped_folders():
    tar_files_manager_close_flag = Injector.get_instance("tar_files_processor_closing_flag")
    tar_files_manager_close_flag.set()
