#!/bin/bash
# train_yolov5.sh
# Assumes you have cloned ultralytics/yolov5 into ../yolov5
# Usage: ./train_yolov5.sh /path/to/dataset_yaml
DATA_YAML=${1:-./data_lei.yaml}
PYTHON=${PYTHON:-python3}
# install requirements (run once)
# $PYTHON -m pip install -r ../yolov5/requirements.txt
# Train
$PYTHON ../yolov5/train.py --img 640 --batch 8 --epochs 50 --data $DATA_YAML --weights yolov5s.pt --device 0
