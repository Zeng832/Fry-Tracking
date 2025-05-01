# Ultralytics YOLO 🚀, AGPL-3.0 license

from yolov8.yolo.v8.classify.predict import ClassificationPredictor, predict
from yolov8.yolo.v8.classify.train import ClassificationTrainer, train
from yolov8.yolo.v8.classify.val import ClassificationValidator, val

__all__ = 'ClassificationPredictor', 'predict', 'ClassificationTrainer', 'train', 'ClassificationValidator', 'val'
