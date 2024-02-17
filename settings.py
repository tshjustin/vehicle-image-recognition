from dotenv import load_dotenv, find_dotenv
import os 

load_dotenv(find_dotenv()) # Load Env keys 

# URLS 
LTA_TRAFFIC_URL = 'http://datamall2.mytransport.sg/ltaodataservice/Traffic-Imagesv2'

# General 
AUTH_HEADERS = {
    "AccountKey": os.getenv('LTA_API_KEY')
}

