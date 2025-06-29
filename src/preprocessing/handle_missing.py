# src/preprocessing/handle_missing.py

import pandas as pd
from sklearn.impute import SimpleImputer
from typing import Tuple
from src.utils.logger import get_logger

logger = get_logger(__name__)

def handle_missing_values(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Fills missing values using mean imputation.

    Args:
        X_train (pd.DataFrame): Training features.
        X_test (pd.DataFrame): Testing features.

    Returns:
        Tuple of transformed train and test features.
    """
    try:
        logger.info("Handling missing values using mean imputation...")

        imputer = SimpleImputer(strategy="mean")
        X_train_imputed = pd.DataFrame(
            imputer.fit_transform(X_train), columns=X_train.columns
        )
        X_test_imputed = pd.DataFrame(
            imputer.transform(X_test), columns=X_test.columns
        )

        logger.info("Missing value handling completed.")
        return X_train_imputed, X_test_imputed

    except Exception as e:
        logger.exception("Error during missing value imputation.")
        raise e
