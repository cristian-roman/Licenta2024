import gc
import os
from datetime import datetime

import torch

from ModelState.model_state import ModelState
from utils import os_interactor
from utils.injector import Injector


class TrainerModelState(ModelState):
    inc_patience: int
    dec_patience: int
    learning_rate: float
    __should_rename: bool
    best_loss: float

    def __init__(self, with_load):
        super().__init__(with_load)

        train_config = Injector.get_instance("config")["train_settings"]
        self.optimizer = torch.optim.Adam(self.model.parameters(), train_config["starting_learning_rate"])
        class_weights = torch.tensor(0.75).to(self.device)
        self.criterion = torch.nn.BCEWithLogitsLoss(pos_weight=class_weights)
        self.best_loss = float("inf")
        self.__should_rename = True

        if with_load:
            self.load_checkpoint()
            # self._load_model_from_checkpoint()
        else:
            config = Injector.get_instance("config")
            os_interactor.create_folder(config["checkpoint_directory"])

    def load_checkpoint(self):
        super()._load_model_from_checkpoint()
        logger = Injector.get_instance("logger")

        checkpoint = torch.load(self.checkpoint_file_location)

        self.best_loss = checkpoint["best_loss"]
        self.optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
        self.__should_rename = False

        logger.log_info(f"Best loss: {self.best_loss}")
        logger.log_info(f"Learning rate: {self.optimizer.param_groups[0]['lr']}")

    def train_step(self, img_np, mask_np):
        loss = self.__step(img_np, mask_np)
        loss.backward()

    def test_step(self, img_np, mask_np, total_loss: list):
        loss = self.__step(img_np, mask_np)
        total_loss[0] += loss.item()

    def __step(self, img_np, mask_np):
        mask_tensor = torch.tensor(mask_np).float().to(self.device)
        mask_tensor = torch.where(mask_tensor >= 0.58, torch.tensor(1.0).to(self.device), torch.tensor(0.0).to(self.device))
        output = self.forward(img_np)

        del img_np, mask_np
        gc.collect()

        loss = self.criterion(output, mask_tensor)

        print(f"\033[92mLoss: {loss.item()}\033[0m")
        return loss

    def save_model_state(self, new_loss: float):
        logger = Injector.get_instance("logger")
        logger.log_info(f"Saving model checkpoint to\n{self.checkpoint_file_location}")

        self.best_loss = new_loss

        if self.__should_rename and os.path.exists(self.checkpoint_file_location):
            logger.log_warning(f"Old model state found at\n{self.checkpoint_file_location}\nRenaming the old one...")
            logger.log_warning("From this point further the model will be overwritten by the new one.")

            new_name = self.__get_new_checkpoint_file_name()
            os_interactor.rename_file(self.checkpoint_file_location, new_name)

            logger.log_info(f"Old model state renamed to {new_name}")
            self.__should_rename = False

        torch.save({
            'model_state_dict': self.model.state_dict(),
            'best_loss': self.best_loss,
            'optimizer_state_dict': self.optimizer.state_dict(),
        }, self.checkpoint_file_location)

        logger.log_info(f"Model state saved successfully at\n{self.checkpoint_file_location}")

    @staticmethod
    def __get_new_checkpoint_file_name():
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"model_checkpoint_[{current_datetime}]"
