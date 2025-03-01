# model trainer
import warnings  

from loan_default_risk.config.configuration import ConfigurationManager
from loan_default_risk.components.modelTrainer import  ModelTrainer
from loan_default_risk import logger 

warnings.filterwarnings('ignore')

STAGE_NAME = "Data Model Trainer Stage"

class ModelTrainingPipeLine:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_Trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_Trainer_config)
        model_trainer.train()
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeLine()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
