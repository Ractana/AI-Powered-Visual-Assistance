# object_detection.py
from ultralytics import YOLO
import cv2
import numpy as np

class ObjectDetector:
    def __init__(self, model_path='yolov8n.pt', device='cpu', conf=0.3):
        self.model = YOLO(model_path)
        self.device = device
        self.conf = conf

    def detect(self, frame):
        results = self.model.predict(source=frame, device=self.device, conf=self.conf, verbose=False)
        detections = []
        if len(results) > 0:
            r = results[0]
            boxes = r.boxes
            for box in boxes:
                cls = int(box.cls.cpu().numpy()[0])
                conf = float(box.conf.cpu().numpy()[0])
                xyxy = box.xyxy.cpu().numpy()[0].astype(int).tolist()
                label = self.model.names.get(cls, str(cls))
                detections.append({'label': label, 'conf': conf, 'bbox': xyxy})
        return detections
