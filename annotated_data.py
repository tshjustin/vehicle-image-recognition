from roboflow import Roboflow
from settings import get_logger, ROBOFLOW_API_KEY, ROBOFLOW_DIR, ROBOFLOW_PROJECT, ROBOFLOW_VERSION, ROBOFLOW_WORKSPACE
import os 

logger = get_logger(__name__)

def download_annotated_data():
    '''
    Downloads annotated dataset from Roboflow to be fed into YoloV8. 
    '''
    rf = Roboflow(api_key=ROBOFLOW_API_KEY)
    project = rf.workspace(ROBOFLOW_WORKSPACE).project(ROBOFLOW_PROJECT)
    project.version(ROBOFLOW_VERSION).download("yolov8") # Updates the annotation of images to suit YoloV8
    logger.info(f'Downloaded Annotated Roboflow dataset to \"{ROBOFLOW_DIR}\"')
    
    update_yaml()
    
def update_yaml():
    """
    Updates the train, valuea and test field in YAML file 
    """
    yaml_path = os.path.join(ROBOFLOW_DIR, 'data.yaml')

    with open(yaml_path, 'r') as f: # Val , Train and Test lines are at the bottom of the file
        lines = f.readlines()

    lines[-1] = f'val: {os.path.join(ROBOFLOW_DIR, "valid", "images")}\n'
    lines[-2] = f'train: {os.path.join(ROBOFLOW_DIR, "train", "images")}\n'
    lines[-3] = f'test: {os.path.join(ROBOFLOW_DIR, "test", "images")}\n'

    with open(yaml_path, 'w') as f:
        f.write('\n'.join(lines)) # Rewrite the data with the abs path 

if __name__ == '__main__':
    download_annotated_data()