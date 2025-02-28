import warnings 

from loan_default_risk.config.configuration import ConfigurationManager
from loan_default_risk.components.data_preprocessing import DataPreprocessing 
from loan_default_risk import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data ingestion stage"

class DataPreprocessTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config=data_preprocessing_config)
        data_preprocessing.create_column_transfer_pipeline()
        data_preprocessing.outliersPipeline()
        data_preprocessing.preprocessingDataset()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataPreprocessTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e