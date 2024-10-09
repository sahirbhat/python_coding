import logging
import requests
from ..logger_config import setup_logger


logger = setup_logger()
# Configure logging with correct levelname formatting
# logging.basicConfig(filename='app.log', format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

def get_data(url):
    baseurl = url
    try:
        # Log the start of the request
        logging.info(f"Attempting to retrieve data from {baseurl}")
        
        response = requests.get(url=baseurl)
        
        if response.status_code == 200:
            logging.info(f"Data successfully retrieved from {baseurl}")
            print(response.content)  # Display response content
        else:
            logging.warning(f"Received status code {response.status_code} from {baseurl}")
    
    except requests.exceptions.RequestException as e:
        # Log detailed error message
        logging.error(f"An error occurred while retrieving data: {e}")

# Call the function with a URL
get_data('https://jsonplaceholder.typicode.com/posts')
