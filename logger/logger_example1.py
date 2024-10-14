import logging
from logging.handlers import RotatingFileHandler


def set_up_logger():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s:%(message)s:%(levelname)s',
        handlers=[
            RotatingFileHandler(
                '../filelogs.log',
                maxBytes=1024,
                backupCount=3
            )
        ]
    )

for i in range(1000) :
    set_up_logger()
    logging.info("logger function called")
    logging.info(f"this is {i} log") 
print("logs have been generated")    
