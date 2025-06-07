import logging
from functools import wraps

logging.basicConfig(
    level= logging.INFO,
    format=('[%(levelname)s] -%(asctime)s - %(message)s'),
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def log_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        logging.info(f'func is called {func.__name__}')
        result=func(*args,**kwargs)
        logging.info(f'logger function completed {func.__name__}')
    
        return result
    return wrapper



@log_decorator
def sample_test():
    logging.info(f'this function sample called')




sample_test()
       
    
    