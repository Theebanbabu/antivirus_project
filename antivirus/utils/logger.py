import os
import logging

LOG_FILE = "logs/antivirus.log"

def setup_logger():
    """Set up the logger."""
    # Create the logs directory if it doesn't exist
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Print the log file path for debugging
    print(f"Log file path: {LOG_FILE}")

def log(message, level="info"):
    """Log a message."""
    if level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
