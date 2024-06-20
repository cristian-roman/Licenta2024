from queue import Queue
from threading import Thread

from Data.TarManager.refs_loader.tar_files_processor import extract_references
from utils.injector import Injector


def image_mask_ref_iterator(concurrently_tar_files_counter: int):
    logger = Injector.get_instance("logger")
    logger.log_info(f"[image_mask_ref_generator] Refs nib images extraction started.\n"
                    f"Processing {concurrently_tar_files_counter} files in parallel.")

    image_mask_ref_pairs = Queue()

    t = Thread(target=extract_references, args=(concurrently_tar_files_counter, image_mask_ref_pairs))
    t.start()

    nib_package = image_mask_ref_pairs.get()
    while nib_package is not None:
        yield nib_package
        nib_package = image_mask_ref_pairs.get()
    yield None
    t.join()
