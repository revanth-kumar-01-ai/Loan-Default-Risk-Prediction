# Data transformation
import warnings  

from loan_default_risk.config.configuration import ConfigurationManager
from loan_default_risk.components.data_transformation import DataTransformation 
from loan_default_risk import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spiting()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
