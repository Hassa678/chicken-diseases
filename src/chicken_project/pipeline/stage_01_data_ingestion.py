import os
import sys
# Get the absolute path of the project root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

# Add the project root to the Python path
sys.path.insert(0, project_root)
from src.chicken_project.exception import CustomException

from src.chicken_project.config.configuration import ConfigurationManager
from src.chicken_project.components.data_ingestion import DataIngestion
from src.chicken_project import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        raise CustomException(e, sys)