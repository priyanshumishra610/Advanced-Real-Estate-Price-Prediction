# src/preprocessing/scaler.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import Tuple
from src.utils.logger import get_logger

logger = get_logger(__name__)

def scale_features(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Applies standard scaling to numerical features.

    Args:
        X_train (pd.DataFrame): Training data.
        X_test (pd.DataFrame): Testing data.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: Scaled training and testing data.
    """
    try:
        logger.info("Scaling features using StandardScaler...")

        scaler = StandardScaler()
        X_train_scaled = pd.DataFrame(
            scaler.fit_transform(X_train), columns=X_train.columns
        )
        X_test_scaled = pd.DataFrame(
            scaler.transform(X_test), columns=X_test.columns
        )

        logger.info("Feature scaling completed.")
        return X_train_scaled, X_test_scaled

    except Exception as e:
        logger.exception("Error during feature scaling.")
        raise e
