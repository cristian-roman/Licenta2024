import os

import torch

from ai.model import Model
from utils.injector import Injector


class ModelState:

    def __init__(self, with_load=False):
        self.__set_device()
        self.model = Model().to(self.device)
        self.__set_checkpoint_file_location()

        if with_load:
            self._load_model_from_checkpoint()

    def __set_device(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger = Injector.get_instance("logger")
        logger.log_info(f"Using device: {self.device}")

    def __set_checkpoint_file_location(self):
        config = Injector.get_instance("config")
        self.checkpoint_file_location = os.path.join(config["checkpoint_directory"], "model.pth")

    def _load_model_from_checkpoint(self):
        logger = Injector.get_instance("logger")

        logger.log_info("Loading model parameters from checkpoint found in\n"
                        f"{self.checkpoint_file_location}\n")

        if not os.path.exists(self.checkpoint_file_location):
            logger.log_error("Checkpoint file does not exist")
            exit(1)

        checkpoint = torch.load(self.checkpoint_file_location)
        self.model.load_state_dict(checkpoint["model_state_dict"])

        logger.log_info(f"Model parameters loaded successfully")

    def forward(self, np_img):
        tr_tensor = torch.tensor(np_img).unsqueeze(0).float().to(self.device)
        tr_tensor *= 15
        output = self.model(tr_tensor)
        return output

    def annotate_image(self, img_np):
        with torch.no_grad():
            output = self.forward(img_np).squeeze()
            output = torch.sigmoid(output)
            binary_mask = torch.where(output >= 0.5, torch.tensor(1).to(self.device), torch.tensor(0).long().to(self.device))
            return binary_mask.squeeze().cpu().numpy().astype('uint8')

