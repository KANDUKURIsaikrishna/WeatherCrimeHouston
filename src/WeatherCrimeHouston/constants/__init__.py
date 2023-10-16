"""
Module: file_paths.py

This module defines file paths for various configuration and data files using the `pathlib` library.

Attributes:
    CONFIG_FILE_PATH (Path): The path to the configuration file, typically stored in "config/config.yaml".
    PARAMS_FILE_PATH (Path): The path to the parameters file, typically stored in "params.yaml".
    SCHEMA_FILE_PATH (Path): The path to the schema file, typically stored in "schema.yaml".
"""
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")
