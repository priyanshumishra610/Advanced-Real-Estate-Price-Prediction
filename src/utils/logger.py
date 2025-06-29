# src/utils/logger.py

import logging
import sys
from datetime import datetime
from pathlib import Path

# Create logs directory if it doesn't exist
Path("logs").mkdir(exist_ok=True)

# Generate log file name with timestamp
log_file = f"logs/run_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout),
    ],
)

def get_logger(name: str) -> logging.Logger:
    """Returns a logger instance with the given module name."""
    return logging.getLogger(name)
