# Components
import os
from pathlib import Path

import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from feature_engine.outliers import Winsorizer

from loan_default_risk import logger
from loan_default_risk.utils.common import get_size
from loan_default_risk.entity.config_entity import DataPreProcessingConfig



# df = pd.read_csv('artifacts/data_ingestion/loanDataset.csv')
class DataPreprocessing:
    def __init__(self, config: DataPreProcessingConfig):
        self.config = config
        self.df = pd.read_csv('artifacts/data_ingestion/loanDataset.csv')

    
    def create_column_transfer_pipeline(self):
        try: 
            df = self.df
            # Numeric features
            numeric_features = df.select_dtypes(exclude=['object']).columns

            # Categorical features
            categorical_features = df.select_dtypes(include=['object']).columns

            # Check if the pipeline file already exists
            if not os.path.exists(self.config.columnTransferPipeline):
                # Create numeric pipeline
                num_pipeLine = Pipeline(steps=[
                    ('impute', SimpleImputer(strategy='mean')),
                    ('Scale', MinMaxScaler())
                ])

                # Create categorical pipeline
                encoding_pipeline = Pipeline([
                    ('oneHotEncode', OneHotEncoder(sparse_output=False))
                ])

                # Combine numeric and categorical pipelines
                preprocess_pipeline = ColumnTransformer([
                    ('numeric', num_pipeLine, numeric_features),
                    ('categorical', encoding_pipeline, categorical_features)
                ])

                # Save the pipeline to a file
                joblib.dump(preprocess_pipeline, self.config.columnTransferPipeline)
                logger.info(f"Pipeline saved at: {self.config.columnTransferPipeline}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.columnTransferPipeline))}")

        except Exception as e:
            # Log any exceptions that occur
            logger.error(f"Error occurred during pipeline creation: {e}")
            raise e 
        
    def outliersPipeline(self):
            try:
                # Check if the outliers pipeline file already exists
                if not os.path.exists(self.config.outliersPipeline):
                    # Define features to handle outliers
                    outliersFeatures = [
                        'numeric__months_loan_duration',
                        'numeric__amount',
                        'numeric__age'
                    ]

                    # Create Winsorizer object
                    winsor = Winsorizer(
                        capping_method='iqr',  # Use IQR rule boundaries
                        tail='both',  # Cap both tails
                        fold=1.5,  # Fold value for IQR
                        variables=outliersFeatures
                    )

                    # Save the Winsorizer pipeline to a file
                    joblib.dump(winsor, self.config.outliersPipeline)
                    logger.info(f"Outliers pipeline saved at: {self.config.outliersPipeline}")
                else:
                    logger.info(f"File already exists of size: {get_size(Path(self.config.outliersPipeline))}")

            except Exception as e:
                # Log any exceptions that occur
                logger.error(f"Error occurred during outliers pipeline creation: {e}")
                raise e  # Re-raise the exception if needed
            
    
    def preprocessingDataset(self):
        try:
            df = self.df
            # Load the preprocessing pipeline
            preprocess = joblib.load(self.config.columnTransferPipeline)

            # Load the outliers pipeline
            outlier = joblib.load(self.config.outliersPipeline)

            # Apply the preprocessing pipeline to the dataset
            df = pd.DataFrame(
                preprocess.fit_transform(df),
                columns=preprocess.get_feature_names_out()
            )

            # Apply the outliers pipeline to specific numeric features
            df[['numeric__months_loan_duration', 'numeric__amount', 'numeric__age']] = outlier.fit_transform(
                df[['numeric__months_loan_duration', 'numeric__amount', 'numeric__age']]
            )

            # Save the cleaned dataset to a CSV file
            if not os.path.exists(self.config.cleanDataset):
                df.to_csv(self.config.cleanDataset, index=False)
                logger.info(f"{self.config.cleanDataset} saved! with following info: cleanDataset.csv")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.cleanDataset))}")

        except Exception as e:
            # Log any exceptions that occur
            logger.error(f"Error occurred during dataset preprocessing: {e}")
            raise e  # Re-raise the exception if needed
        
        
        