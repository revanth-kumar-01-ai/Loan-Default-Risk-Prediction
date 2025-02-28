from loan_default_risk import logger 
from loan_default_risk.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeLine 


STAGE_NAME = "Data Ingestion Stage"


try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   data_ingestion = DataIngestionTrainingPipeLine()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
