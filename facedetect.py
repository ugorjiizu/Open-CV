import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

######################################################
# Face Detect using webcam

# frameWidth = 400
# frameHeight = 400

# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

# while True:
#     success,img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
#     faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#     for (x,y,w,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

#     cv2.imshow('Video', img)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break  
    
######################################################

img = cv2.imread('Resources/lenna.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)