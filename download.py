from settings import LTA_TRAFFIC_URL, DOWNLOAD_FOLDER, get_logger
import requests 
import time
import os 

'''
Queries the Endpoints and obtain Traffic Images each minute 
'''
# Schema of items 
'''
[
    {
        timestap: str 
        camera: [ {...} ]
    }
    
]
'''

# Schema of "cameras" field in Items
'''
{
    timestamp=str, 
    image=str
    location = {}
}
'''

logger = get_logger(__name__)

def download(url: str):
    '''
    Downloads the traffic images from LTA API and store into a Folder 
    
    r type: Returns a Dictionary, with the content inside the Value of 'Value' Key
    '''
    img_data = requests.get(url).content # Upon GET to the endpoint, image is downloaded
    logger.info(f'Downloading: {url}') 
    
    # Stores the images into a folder 
    try:
        if not os.path.exists(DOWNLOAD_FOLDER):
            os.mkdir(DOWNLOAD_FOLDER)

        with open(f'{DOWNLOAD_FOLDER}/{url.split("/")[-1]}', 'wb') as handler: # Images in JPEG - Work with binary data 
            handler.write(img_data)
    except Exception as e:
        logger.error(e)
    
def loop(n: int=50):
    '''
    Downloads batches of Data from API
    '''
    count = 1 
    response = requests.get(LTA_TRAFFIC_URL) 
    logger.info(f'Response Status: {response.status_code}')
    items = response.json().get('items',[]) # Returns a list of Dict
    
    for item in items: 
        for camera in item.get('cameras', []):
            url_download = camera.get('image')
            
            if url_download:
                download(url_download)
                count +=1 
                
                if count > n:
                    return
                
if __name__ == '__main__':
    loop(30)