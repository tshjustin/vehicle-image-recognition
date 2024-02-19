import cv2
import time

from yolov8.YOLOv8 import yolov8_detector

IMG_PATH = 'assests/7bf0ca92-a3a6-4b15-9e87-b8e6d13439b5.jpg'

if __name__ == '__main__':
    # Read image
    img = cv2.imread(IMG_PATH)

    # Detect Objects
    boxes, scores, class_ids = yolov8_detector(img)

    for score, cls in list(zip(scores, class_ids)):
        print(f'Class {cls} : Score {score}')

    # Draw detections
    combined_img = yolov8_detector.draw_detections(img)
    cv2.imwrite(f'{time.time()}.{IMG_PATH.split(".")[-1]}', combined_img)

    # Open image
    cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
    cv2.imshow("Detected Objects", combined_img)
    cv2.waitKey(0)