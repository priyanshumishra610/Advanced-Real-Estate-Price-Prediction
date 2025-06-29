# main.py

from src.ingest.data_loader import load_california_housing_data
from src.preprocessing.data_splitter import split_data
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

    logger.info("✅ Data splitting completed.")
    logger.info(f"Sample train data:\n{X_train.head()}")

if __name__ == "__main__":
    main()
