import warnings 

from loan_default_risk.config.configuration import ConfigurationManager
from loan_default_risk.components.data_ingestion import DataIngestion 
from loan_default_risk import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data ingestion stage"

class DataIngestionTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.fetch_data_from_database()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e