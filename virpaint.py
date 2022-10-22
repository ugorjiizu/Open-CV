import cv2
import numpy as np   

frameWidth = 640
frameHeight = 480

colorlist = [[62,73,212,179,255,255],[23,43,149,60,117,255], [140,0,215,168,21,235]] #Blue, Green, pale pink
colorValues = [[255,0,0], [0,255,0], [216,208,230]] #BGR values
myPoints=[]

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>800:
            # cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2, y

def findcolor(img,colorlist,colorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in colorlist:
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getcontours(mask)
        cv2.circle(imgContour, (x,y), 15, colorValues[count], cv2.FILLED)
        if x!= 0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints
        
def drawOnCanvas(myPoints, colorValues):
    for point in myPoints:
        cv2.circle(imgContour, (point[0], point[1]), 10, colorValues[point[2]], cv2.FILLED)
        

while True:
    success,img = cap.read()
    imgContour = img.copy()
    newPoints = findcolor(img,colorlist,colorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, colorValues)
    cv2.imshow('Video', imgContour)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 