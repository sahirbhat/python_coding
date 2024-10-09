import logging

def setup_logger():
    logging.basicConfig(
        filename='app.log',
        format='%(asctime)s:%(levelname)s:%(message)s',
        level=logging.INFO,
    )
    logger = logging.getLogger()
    return logger