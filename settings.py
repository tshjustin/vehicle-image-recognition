from dotenv import load_dotenv, find_dotenv
import os 
import logging 

load_dotenv(find_dotenv()) # Load Env keys 

# Set Logger 
logging.basicConfig(level=logging.INFO) # Ensure normal working conditions

def get_logger(name):
    return logging.getLogger(name)

# URLS 
LTA_TRAFFIC_URL = 'https://api.data.gov.sg/v1/transport/traffic-images'

# General 
AUTH_HEADERS = {
    "AccountKey": os.getenv('LTA_API_KEY')
}

DOWNLOAD_FOLDER = 'assests'
