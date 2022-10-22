import cv2
import numpy as np
from myutils import stackImages
from numpy.core.fromnumeric import resize, shape
from numpy.core.shape_base import hstack, vstack  



frameWidth = 400
frameHeight = 400

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success,img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    # cv2.imshow('Video', img)
    # path = 'Resources/rig.jpg'
    # img = cv2.imread(path)
    img = cv2.resize(img, (400, 400))
    kernel = np.ones((5, 5), np.uint8)
    
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(img, (15,15), 0)
    imgCanny = cv2.Canny(img, 100,100)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=2 )

    stackedImages = stackImages(0.5, ([img, imgGray, imgBlur, img, imgGray, imgBlur],
                                    [imgCanny, imgDilation, imgEroded, imgCanny, imgDilation, imgEroded],
                                    [imgCanny, imgDilation, imgEroded, imgCanny, imgDilation, imgEroded],
                                    [imgCanny, imgDilation, imgEroded, imgCanny, imgDilation, imgEroded]))

    cv2.imshow('izu', stackedImages)


    # cv2.imshow('izu', img)
    # cv2.imshow('Bwizu', imgGray)
    # cv2.imshow('Bizu', imgBlur) 
    # cv2.imshow('Cizu', imgCanny)
    # cv2.imshow('Dizu', imgDilation)
    # cv2.imshow('Eizu', imgEroded)




    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
