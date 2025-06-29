# main.py

from src.ingest.data_loader import load_california_housing_data
from src.preprocessing.data_splitter import split_data
from src.preprocessing.handle_missing import handle_missing_values
from src.preprocessing.scaler import scale_features
from src.modeling.model_trainer import train_model
from src.modeling.evaluator import evaluate_model
from src.utils.config_loader import load_config
from src.utils.logger import get_logger

logger = get_logger(__name__)

def main():
    logger.info("🚀 Starting Property Price Prediction Pipeline...")

    config = load_config()
    df = load_california_housing_data()

    X_train, X_test, y_train, y_test = split_data(
        df=df,
        target_column=config["data_loader"]["target_column"],
        test_size=config["data_loader"]["test_size"],
        random_state=config["data_loader"]["random_state"]
    )

    X_train, X_test = handle_missing_values(X_train, X_test)
    X_train, X_test = scale_features(X_train, X_test)

    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    logger.info("✅ Pipeline execution completed successfully.")

if __name__ == "__main__":
    main()
