import cv2
from cv2 import VideoCapture
import numpy as np

nplateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")

######################################################

frameWidth = 400
frameHeight = 400
minArea = 500
color = (255,0,255)
count = 0
######################################################
# VideoCapture
# cap = cv2.VideoCapture('Resources/test_video.mp4')
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

# while True:
#     success,img = cap.read()
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     numberplates = nplateCascade.detectMultiScale(imgGray, 1.1, 4)
#     for (x,y,w,h) in numberplates:
#         area = w*h
#         if area > minArea:
#             cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
#             cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
#             imgRoi = img[y:y+h, x:x+w]
#             cv2.imshow('ROI', imgRoi)

#     cv2.imshow('Video', img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break  
######################################################

img = cv2.imread('Resources/p3.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

numberplates = nplateCascade.detectMultiScale(imgGray, 1.1, 4)
for (x,y,w,h) in numberplates:
    area = w*h
    if area > minArea:
        cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
        cv2.putText(img, "Number Plate", (x,y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
        imgRoi = img[y:y+h, x:x+w]
        cv2.imshow('ROI', imgRoi)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)

cv2.imshow('Image', img)

cv2.imwrite("Resources/Scanned/NoPlate_"+str(count)+".jpg",imgRoi)
cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX, 2,(0,0,255),2)
cv2.imshow("Result",img)
cv2.waitKey(500)
cv2.waitKey(0)