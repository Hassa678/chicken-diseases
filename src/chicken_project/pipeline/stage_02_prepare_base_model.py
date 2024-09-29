import os
import sys

# Get the absolute path of the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Add the project root to the Python path
sys.path.insert(0, project_root)

from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.prepare_base_model import PrepareBaseModel
from src.chicken_project import logger

STAGE_NAME = "Prepare base model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()





if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e