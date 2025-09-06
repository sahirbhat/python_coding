import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    # Set up the basic configuration for logging
    logging.basicConfig(
        level=logging.INFO,  # Set global logging level
        format='%(asctime)s:%(levelname)s:%(message)s',  # Log format
        handlers=[            # Add handlers
            RotatingFileHandler(
                'app.log',         # Log file path
                maxBytes=1024,     # Max size of 1 KB before rotating
                backupCount=2      # Keep up to 2 backup files
            )
        ]
    )

# # Call the setup function
# setup_logging()

# Example logging
for i in range(100):
    setup_logging()
    logging.info(f"This is log entry number {i}")

print("Logs have been generated.")
