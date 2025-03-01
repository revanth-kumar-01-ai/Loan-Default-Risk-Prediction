# configuration manager in src config
import warnings 

from loan_default_risk.constants import * 
from loan_default_risk.utils.common import read_yaml, create_directories 
from loan_default_risk.entity.config_entity import (
                                                    DataIngestionConfig,
                                                    DataPreProcessingConfig,
                                                    DataValidationConfig,
                                                    DataTransformationConfig, 
                                                    ModelTrainerConfig
                                                    )


warnings.filterwarnings('ignore')

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):


        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)


        create_directories([self.config.artifacts_root])

    # data ingestion 💉
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion


        create_directories([config.root_dir])


        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_query=config.source_query,
            load_data=config.load_data,
        )


        return data_ingestion_config
    
    # Data preprocessing ⚙️
    def get_data_preprocessing_config(self) -> DataPreProcessingConfig:
        config = self.config.data_preprocessing_model


        create_directories([config.root_dir])


        data_preprocessing_config = DataPreProcessingConfig(
            root_dir=config.root_dir,
            columnTransferPipeline=config.columnTransferPipeline,
            outliersPipeline=config.outliersPipeline,
            cleanDataset = config.cleanDataset
        )


        return data_preprocessing_config
    
    # Data Validation 
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS


        create_directories([config.root_dir])


        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            cleanDataset = config.cleanDataset,
            all_schema=schema,
        )


        return data_validation_config
    
    # Data transformation
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.DecisionTreeClassifier
        schema =  self.schema.TARGET_COLUMN


        create_directories([config.root_dir])


        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            max_depth = params.max_depth,
            criterion = params.criterion,
            target_column = schema.name
        )


        return model_trainer_config
