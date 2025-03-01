from dataclasses import dataclass 
from pathlib import Path 

# data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_query: str  
    load_data: Path

# data preprocessing
@dataclass(frozen=True)
class DataPreProcessingConfig:
    root_dir: Path
    columnTransferPipeline: Path
    outliersPipeline: Path
    cleanDataset: Path

# data validation 
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    cleanDataset: Path
    all_schema: dict

# data transformation 
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

