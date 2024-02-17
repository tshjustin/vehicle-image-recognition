from dotenv import load_dotenv, find_dotenv
import os 

load_dotenv(find_dotenv()) # Load Env keys 

# General 
AUTH_HEADERS - {
    "AccountKey": os.getenv('LTA_API_KEY')
}