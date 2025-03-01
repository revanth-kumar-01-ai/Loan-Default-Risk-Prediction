# Data validation
import warnings  

from loan_default_risk.config.configuration import ConfigurationManager
from loan_default_risk.components.data_validation import DataValidation 
from loan_default_risk import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data validation stage"

class DataValidationTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
