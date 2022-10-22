import cv2
import numpy as np 

FrameWidth = 400
FrameLength = 400

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


path = 'Resources/rig.jpg' 
img = cv2.imread(path)
img = cv2.resize(img, (FrameLength, FrameWidth))

cv2.imshow('rig', img)

cv2.setMouseCallback('rig', mousePoints)





cv2.waitKey(0)
