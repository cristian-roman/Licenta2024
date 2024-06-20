import torch

from Data.data_provider import DataProvider
from ModelState.trainer_model_state import TrainerModelState
from utils.injector import Injector


def __set_model_state_for_training(model_state: TrainerModelState):
    model_state.model.train()
    model_state.optimizer.zero_grad()


def run_training_phase(model_state: TrainerModelState, data_provider: DataProvider):
    logger = Injector.get_instance("logger")

    logger.log_info(f"Starting training....")
    __set_model_state_for_training(model_state)

    for (img_np, mask_np, index) in data_provider.training_data_iterator():
        print(f"Learning from input {index} / {data_provider.count_training_indices}")
        model_state.optimizer.zero_grad()
        model_state.train_step(img_np, mask_np)
        torch.nn.utils.clip_grad_norm_(model_state.model.parameters(), max_norm=1.0)
        model_state.optimizer.step()

    logger.log_info(f"Training finished")


def run_testing_phase(model_state: TrainerModelState, data_provider: DataProvider):
    logger = Injector.get_instance("logger")

    logger.log_info(f"Starting testing....")
    model_state.model.eval()
    total_loss = [0]

    with torch.no_grad():
        for (img_np, mask_np, index) in data_provider.testing_data_iterator():
            print(f"Testing input {index} / {data_provider.count_testing_indices}")
            model_state.test_step(img_np, mask_np, total_loss)

    logger.log_info(
        f"Testing finished........ Loss of current best model state: {total_loss[0]}  vs Current loss: {model_state.best_loss}")

    return total_loss[0]