from loan_default_risk import logger 
from loan_default_risk.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeLine 
from loan_default_risk.pipeline.stage_02_data_preprocessing import DataPreprocessTrainingPipeLine
from loan_default_risk.pipeline.stage_03_data_validation import DataValidationTrainingPipeLine
from loan_default_risk.pipeline.stage_04_data_transformation import DataTransformationTrainingPipeLine


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


STAGE_NAME = "Data Validation Stage"


try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_validation = DataValidationTrainingPipeLine()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation Stage"

try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_transformation = DataTransformationTrainingPipeLine()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
