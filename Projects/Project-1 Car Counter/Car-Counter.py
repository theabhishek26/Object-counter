import numpy as np
from ultralytics import  YOLO
import  cv2
import cvzone
import math
from sort import *

cap = cv2.VideoCapture("../../Vedios/cars.mp4")

model=YOLO("../Yolo_Weights/yolov8l.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

mask=cv2.imread("mask.png")

#Tracking
tracker=Sort(max_age=20,min_hits=3,iou_threshold=0.3)

limits=[400,297,673,297]
tot_count=[]

while True:
    success, img = cap.read()
    mask = cv2.resize(mask, (img.shape[1], img.shape[0]))
    imgRegion=cv2.bitwise_and(img,mask)

    imgGraphics=cv2.imread("graphics.png",cv2.IMREAD_UNCHANGED)
    img=cvzone.overlayPNG(img,imgGraphics,(0,0))

    results=model(imgRegion,stream=True)

    detections=np.empty((0,5))
    for i in results:
        boxes=i.boxes
        for box in boxes:
            #Bounding Box
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2= int(x1),int(y1),int(x2),int(y2)
            # print( x1,y1,x2,y2)
            # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)

            w,h = x2-x1,y2-y1


            #Confidence
            conf=math.ceil(box.conf[0]*100)/100
            # print(conf)
            # cvzone.putTextRect(img,f'{conf}',(max(0,x1),max(35,y1)))

            #Class Name
            cls=int(box.cls[0])
            curclass=classNames[cls]

            if curclass=="car" or curclass=="bus" or curclass=="truck" or curclass=="motorbike" and conf>0.3:
                # cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)),
                #                scale=0.6,thickness=1,offset=3)
                # cvzone.cornerRect(img, (x1, y1, w, h), l=9,rt=5)
                curArray=np.array([x1,y1,x2,y2,conf])
                detections=np.vstack((detections,curArray))

    resultsTracker=tracker.update(detections)
    cv2.line(img,(limits[0],limits[1]),(limits[2],limits[3]),(0,0,255),4)

    for result in resultsTracker:
        x1,y1,x2,y2,id=result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2,colorR=(255,0,0))
        cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)
        cx,cy=x1+w//2,y1+h//2
        cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)

        if limits[0]<cx<limits[2] and limits[1]-15<cy<limits[1]+15:
            if tot_count.count(id)==0:
                tot_count.append(id)
                cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 4)

    # cvzone.putTextRect(img, f'{len(tot_count)}', (50,50))
    cv2.putText(img,str(len(tot_count)),(255,100),cv2.FONT_HERSHEY_PLAIN,5,(50,50,250),8)
    cv2.imshow("Vehicle_Counter",img)
    # cv2.imshow("Image_Region", imgRegion)
    cv2.waitKey(1)


