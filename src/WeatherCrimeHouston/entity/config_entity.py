"""
Module: data_ingestion_config.py

This module defines a data class for data ingestion configuration. It uses the `dataclasses` library to create an immutable class.

Classes:
    DataIngestionConfig: A data class representing the configuration for data ingestion.

Attributes:
    - root_dir (Path): The root directory where data will be stored.
    - source_URL (str): The URL from which data will be downloaded.
    - local_data_file (Path): The path to the local data file.
    - unzip_dir (Path): The directory where data will be extracted or unzipped.
"""
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path




@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict



@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path



# @dataclass(frozen=True)
# class ModelTrainerConfig:
#     root_dir: Path
#     train_data_path: Path
#     test_data_path: Path
#     model_name: str
#     alpha: float
#     l1_ratio: float
#     target_column: str




# @dataclass(frozen=True)
# class ModelEvaluationConfig:
#     root_dir: Path
#     test_data_path: Path
#     model_path: Path
#     all_params: dict
#     metric_file_name: Path
#     target_column: str
#     mlflow_uri: str