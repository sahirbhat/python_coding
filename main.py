# main.py
from logger_config import setup_logger

# Set up global logger
logger = setup_logger()

def main():
    logger.info("Application started")
    # Your main code logic here
    logger.info("Application finished")

if __name__ == "__main__":
    main()
