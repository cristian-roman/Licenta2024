import data_uploader
import trainer
import validator

from Data.data_provider import DataProvider
from ModelState.trainer_model_state import TrainerModelState
from app_init.init import register_dependencies
from utils.injector import Injector


def main():

    with_load = True

    register_dependencies()
    logger = Injector.get_instance('logger')
    epochs = Injector.get_instance('config')['train_settings']['epochs']

    model_state = TrainerModelState(with_load)
    data_provider = DataProvider(with_load)

    for epoch in range(epochs):
        logger.log_info(f'Epoch {epoch + 1} started')

        trainer.run_training_phase(model_state, data_provider)
        current_epoch_loss = trainer.run_testing_phase(model_state, data_provider)

        if current_epoch_loss < model_state.best_loss:
            logger.log_info(f"New best model state found")
            model_state.save_model_state(current_epoch_loss)

        else:
            logger.log_info("No new best model state found")

        logger.log_info(f'Epoch {epoch + 1} finished')

    logger.log_info("Training finished")

    validator.run_validation_phase(model_state, data_provider)

    data_uploader.annotate_dataset(model_state)


if __name__ == "__main__":
    main()
