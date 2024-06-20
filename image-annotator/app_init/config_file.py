import os

from utils import os_interactor
from utils.injector import Injector


def register_config_file(config_file_name):
    working_dir = Injector.get_instance('working_dir')
    config_file_path = str(os.path.join(working_dir, config_file_name))
    if not os.path.exists(config_file_path):
        raise FileNotFoundError(f'Configuration file not found: {config_file_path}')
    else:
        config = os_interactor.load_json_document(config_file_path)
        config_file_name = config_file_name.split('.')[0]
        Injector.register_instance(config_file_name, config)
