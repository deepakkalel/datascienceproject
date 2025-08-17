import os
import yaml #this is to read others yaml files
from src.datascience import logger
import json
import joblib #it helps to create and save models in .joblib format which is serialized itself
from ensure import ensure_annotations
from box import ConfigBox 
# it is for easiness to bringout key / read keys from yaml files (we hav many), we can directly call config box and get keys
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError #for handling box configuration errors


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns its contents as a ConfigBox

    Args: 
        path_to_yaml: The path to the YAML file to read. (input)

    Raises:
        ValueError: If the YAML file is empty.
        e: empty file

    Returns:
        ConfigBox: configbox type The contents of the YAML file as a ConfigBox.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml_file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose: True):
    """create list of directories

    Args:
        path_to_directories: list of directories to be created
        ignore_log(bool, optional): if True, suppress logging, ignores if multiple dirs is to be created. defaults to False
        verbose: if True, print the directories being created
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
    

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary as a JSON file.

    Args:
        path (Path): The path to the JSON file to save.
        data (dict): The dictionary to save as JSON.

    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4) #indent is 4 spaces

    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (Path): The path to the JSON file to load.

    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox.
                     data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file.

    Args:
        path (Path): The path to the binary file to save.
        data (Any): The data to save to the binary file.

    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file.

    Args:
        path (Path): The path to the binary file to load.

    Returns:
        Any: The data loaded from the binary file.

    """
    data = joblib.load(filename=path)
    logger.info(f"binary file loaded from: {path}")
    return data
