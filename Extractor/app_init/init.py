from app_init.config_file import register_config_file
from app_init.logger import register_logger
from app_init.working_dir import register_working_dir


def register_dependencies():
    register_working_dir()
    register_config_file('config.json')
    register_config_file('secrets.json')
    register_logger()
