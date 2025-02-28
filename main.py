from loan_default_risk import logger 
from loan_default_risk.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeLine 
from loan_default_risk.pipeline.stage_02_data_preprocessing import DataPreprocessTrainingPipeLine


STAGE_NAME = "Data Ingestion Stage"


try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



STAGE_NAME = "Data Preprocess Stage"


try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_preprocess = DataPreprocessTrainingPipeLine()
   data_preprocess.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
