'''
Queries the Endpoints and obtain Traffic Images each minute 
'''
from settings import AUTH_HEADERS, LTA_TRAFFIC_URL
import requests 

def download():
    '''
    Downloads the traffic images from LTA API and store into a Folder 
    
    r type: Returns a Dictionary, with the content inside the Value of 'Value' Key
    '''
    response = requests.get(LTA_TRAFFIC_URL, headers=AUTH_HEADERS) 
    print(response.json())
    
if __name__ == '__main__':
    download()
