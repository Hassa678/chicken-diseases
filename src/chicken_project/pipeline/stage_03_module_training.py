import os
import sys

# Get the absolute path of the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Add the project root to the Python path
sys.path.insert(0, project_root)
from src.chicken_project.exception import CustomException
from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.prepare_callbacks import PrepareCallback
from src.chicken_project.components.model_training import Training
from src.chicken_project import logger

STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()


        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )




if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)