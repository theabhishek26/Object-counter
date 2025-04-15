import cv2
from ultralytics import  YOLO
# from cv2 import


model=YOLO("../Yolo_Weights/yolov8l.pt")
results=model("Images/1.jpg",show=True);
cv2.waitKey(0)