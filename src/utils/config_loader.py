# src/utils/config_loader.py

import yaml
from typing import Any, Dict
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_config(path: str = "config/config.yaml") -> Dict[str, Any]:
    """
    Loads a YAML configuration file.

    Args:
        path (str): Path to the YAML file.

    Returns:
        dict: Parsed configuration dictionary.
    """
    try:
        logger.info(f"Loading configuration from {path}")
        with open(path, "r") as file:
            config = yaml.safe_load(file)
        logger.info("Configuration loaded successfully")
        return config
    except Exception as e:
        logger.exception("Failed to load configuration.")
        raise e
