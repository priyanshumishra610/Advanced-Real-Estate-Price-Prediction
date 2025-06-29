# src/ingest/data_loader.py

from sklearn.datasets import fetch_california_housing
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

def load_california_housing_data(as_df: bool = True) -> pd.DataFrame:
    """
    Loads the California Housing dataset.

    Args:
        as_df (bool): If True, returns the dataset as a pandas DataFrame.

    Returns:
        pd.DataFrame: The dataset with feature columns and target column 'MedHouseVal'.
    """
    try:
        logger.info("Loading California housing dataset from sklearn...")
        dataset = fetch_california_housing()
        df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
        df["MedHouseVal"] = dataset.target
        logger.info("Dataset loaded successfully with shape: %s", df.shape)
        return df

    except Exception as e:
        logger.exception("Failed to load California housing dataset.")
        raise e
