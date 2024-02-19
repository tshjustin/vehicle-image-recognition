from dotenv import load_dotenv, find_dotenv
import logging 
import os 

load_dotenv(find_dotenv()) # Load Env keys 

# Set Logger 
logging.basicConfig(level=logging.INFO) # Ensure normal working conditions

def get_logger(name):
    return logging.getLogger(name)

# URLS 
LTA_TRAFFIC_URL = 'https://api.data.gov.sg/v1/transport/traffic-images'

# Folders
DOWNLOAD_FOLDER = 'assests'

# Roboflow Annotated Data 
ROBOFLOW_API_KEY = os.environ.get('ROBOFLOW_API_KEY')
ROBOFLOW_WORKSPACE = os.environ.get('ROBOFLOW_WORKSPACE')
ROBOFLOW_PROJECT = os.environ.get('ROBOFLOW_PROJECT')
ROBOFLOW_VERSION = int(os.environ.get('ROBOFLOW_VERSION'))
ROBOFLOW_DIR = os.path.join(os.getcwd(), f'{ROBOFLOW_PROJECT}-{ROBOFLOW_VERSION}')

# ONNX 
ONNX_MODEL = 'models/yolov8n.onnx'
CONF_THRESHOLD = 0.3