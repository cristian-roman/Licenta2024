import os

from utils.injector import Injector


def register_working_dir():
    current_file_location = os.path.abspath(__file__)
    app_init_dir = os.path.dirname(current_file_location)
    working_dir = os.path.dirname(app_init_dir)
    Injector.register_instance('working_dir', working_dir)
