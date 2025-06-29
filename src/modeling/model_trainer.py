# src/modeling/model_trainer.py

from sklearn.linear_model import LinearRegression
from typing import Tuple
import pandas as pd
from sklearn.base import RegressorMixin
from src.utils.logger import get_logger

logger = get_logger(__name__)

def train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series
) -> RegressorMixin:
    """
    Trains a Linear Regression model.

    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Target variable.

    Returns:
        Trained regression model.
    """
    try:
        logger.info("Training Linear Regression model...")
        model = LinearRegression()
        model.fit(X_train, y_train)
        logger.info("Model training completed.")
        return model

    except Exception as e:
        logger.exception("Model training failed.")
        raise e
