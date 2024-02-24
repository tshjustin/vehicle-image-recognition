import json
import logging
from flask import abort, Flask, request, Response
from imread_from_url import imread_from_url
from requests.exceptions import ConnectionError

from yolov8.YOLOv8 import yolov8_detector

logger = logging.getLogger('App')

app = Flask(__name__)

def error_(e: str) -> Response:
    '''
    Returns standard error for bad url / invalid image 
    '''
    return Response(response=json.dumps({'error': e, 'boxes': [], 'classes': [], 'conf': []}), status=400)

@app.route('/inference')
def inference():
    """
    error: str,                // error message if req failed, else None
    boxes: list[list[float]],  // coords of bounding boxes (top left as origin, (x1 y1 x2 y2)) if success, else [] 
    classes: list[int],        // class indexes if success, else [] - len(classes) returns the number of objects that are present in the image 
    conf: list[float]          // confidence levels if success, else []
    """
    url = request.args.get('url', default='', type=str)

    if not url:
        return error_('No URL received')

    try:
        img = imread_from_url(url)
        boxes, scores, class_ids = yolov8_detector(img)

    except ConnectionError: # Invalid image URL format - Since images from APIs may have timeout timer 
        return error_('Invalid image URL')
    
    except Exception as e: # Unknown error  
        return error_(str(e))
    
    return Response(response=json.dumps({
            'error': None, 
            'boxes': boxes.tolist(), 
            'classes': class_ids.tolist(), 
            'conf': scores.tolist()
        }), status=200)

if __name__ == '__main__':
    app.run() 