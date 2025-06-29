# main.py

from src.ingest.data_loader import load_california_housing_data
from src.utils.logger import get_logger
from src.utils.config_loader import load_config

logger = get_logger(__name__)

def main():
    logger.info("Starting the property price prediction pipeline...")

    config = load_config()
    logger.info(f"Loaded Config:\n{config}")

    df = load_california_housing_data()
    logger.info(f"Sample data preview:\n{df.head()}")
    logger.info(f"Dataset shape: {df.shape}")

if __name__ == "__main__":
    main()
