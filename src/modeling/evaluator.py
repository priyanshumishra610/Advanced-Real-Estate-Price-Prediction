# src/modeling/evaluator.py

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
from typing import Tuple
import pandas as pd
from sklearn.base import RegressorMixin
from src.utils.logger import get_logger

logger = get_logger(__name__)

def evaluate_model(
    model: RegressorMixin,
    X_test: pd.DataFrame,
    y_test: pd.Series
) -> Tuple[float, float, float]:
    """
    Evaluates the regression model using MAE, RMSE, and R².

    Args:
        model (RegressorMixin): Trained model.
        X_test (pd.DataFrame): Testing features.
        y_test (pd.Series): True labels.

    Returns:
        Tuple of (MAE, RMSE, R²)
    """
    try:
        logger.info("Evaluating model...")
        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        r2 = r2_score(y_test, y_pred)

        logger.info(f"MAE: {mae:.4f}, RMSE: {rmse:.4f}, R²: {r2:.4f}")
        return mae, rmse, r2

    except Exception as e:
        logger.exception("Model evaluation failed.")
        raise e
