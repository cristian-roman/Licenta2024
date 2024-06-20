from utils import os_interactor
from utils.injector import Injector

from datetime import datetime


class Logger:

    @staticmethod
    def __get_log_file_location():
        working_dir = Injector.get_instance('working_dir')
        logs_directory = f"{working_dir}/logs"
        os_interactor.create_folder(logs_directory)

        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file_name = f"log_[{current_datetime}].log"
        log_file_location = f"{logs_directory}/{log_file_name}"
        return log_file_location

    def __init__(self, log_levels: set):
        self.log_levels = log_levels
        self.log_file_location = self.__get_log_file_location()

    def __log(self, level, message):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_message = f"[{level}] ------------------------------------------------------------------------------\n"
        new_message += f"[{current_datetime}] {message}"
        new_message += "\n-------------------------------------------------------------------------------------\n"

        with open(self.log_file_location, "a") as f:
            f.write(new_message + "\n")

        new_message = f"[{current_datetime}] [{level}] {message}"
        if level == "INFO":
            print("\033[1;92m", new_message, "\033[0m")
        elif level == "WARNING":
            print("\033[1;93m", new_message, "\033[0m")
        elif level == "ERROR":
            print("\033[1;91m", new_message, "\033[0m")

    def log_info(self, message):
        if "INFO" in self.log_levels:
            self.__log("INFO", message)

    def log_debug(self, message):
        self.__log("DEBUG", message)

    def log_warning(self, message):
        if "WARNING" in self.log_levels:
            self.__log("WARNING", message)

    def log_error(self, message):
        self.__log("ERROR", message)
