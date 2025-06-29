# src/preprocessing/data_splitter.py

from sklearn.model_selection import train_test_split
import pandas as pd
from typing import Tuple
from src.utils.logger import get_logger

logger = get_logger(__name__)

def split_data(
    df: pd.DataFrame,
    target_column: str,
    test_size: float,
    random_state: int
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Splits the dataset into training and testing sets.

    Args:
        df (pd.DataFrame): The full dataset.
        target_column (str): Name of the target column.
        test_size (float): Proportion of the test split.
        random_state (int): Random seed for reproducibility.

    Returns:
        Tuple[X_train, X_test, y_train, y_test]: Split data.
    """
    try:
        logger.info("Splitting data into train and test sets...")
        X = df.drop(columns=[target_column])
        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )

        logger.info(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
        return X_train, X_test, y_train, y_test

    except Exception as e:
        logger.exception("Error during data splitting.")
        raise e
