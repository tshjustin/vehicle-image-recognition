from ultralytics import YOLO
from settings import get_logger, ROBOFLOW_DIR
from typing import List

logger = get_logger('YOLOv8')

'''
Training of YoloV8 model using Custom Annotated Dataset from Roboflow
'''

class YoloV8Model:

    def __init__(self, weights: str = 'yolov8n.pt'):
        self.model = YOLO(weights) # load a pretrained model - Fine tuning model to incoporate Custom Dataset

    
    def inference(self, paths: List[str]):
        """
        Run inference on a set of images as specified by paths

        Params
        ------
        paths : List[str]
            List of image paths
        """
        logger.info(f'Inference')
        results = self.model.predict(paths, save=True)
        logger.info(f'Predictions saved at \"runs/detect/predict\"')

        return results


    def train(self, epochs: int = 100, imgsz: int = 640):
        '''
        Download & Trains Data
        '''
        from annotated_data import download_annotated_data

        download_annotated_data()
        self.model.train(data=f'{ROBOFLOW_DIR}/data.yaml', epochs=epochs, imgsz=imgsz)
        logger.info(f'Training Done')
        self.save()
    
    
    def save(self):
        '''
        Export Data as ONNX Format 
        '''
        path = self.model.export(format="onnx")
        logger.info(f'Saved ONNX model to {path}')

if __name__ == '__main__':
    model = YoloV8Model('models/yolov8n.pt')  # Loads the pre-trained model that is obtained from YoloV8 GitHub
    model.train()
    model.save()