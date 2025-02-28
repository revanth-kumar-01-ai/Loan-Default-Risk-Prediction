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

# 