import cv2
import numpy as np  

path = 'Resources/iphone.jpg'
img = cv2.imread(path)
# img = cv2.resize(img, (500,500))
# print(img.shape)

circles = np.zeros((4,2), np.int)
counter = 0
width, height = 170,250

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(circles)

while True:
    
    if counter == 4:
        phonepts = np.float32([circles[0], circles[1], circles[2], circles[3]])
        # print(phonepts)
        phonepts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
        matrix = cv2.getPerspectiveTransform(phonepts, phonepts2)
        output = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow('warp', output)


    for x in range(0,4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 4, (255,0,0), cv2.FILLED)

    cv2.imshow('iphone', img)
    cv2.setMouseCallback('iphone', mousePoints)

    cv2.waitKey(1)
