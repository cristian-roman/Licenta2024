from utils.injector import Injector
from utils.logger import Logger


def register_logger():
    log_levels = {"INFO", "WARNING"}
    logger = Logger(log_levels)
    Injector.register_instance('logger', logger)
