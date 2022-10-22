import cv2
import numpy as np  

kernel = np.ones((5, 5), np.uint8)
# print(kernel)

path = 'Resources/rig.jpg'
img = cv2.imread(path)
img = cv2.resize(img, (400, 400))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (15,15), 0)
imgCanny = cv2.Canny(img, 100,100)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
imgEroded = cv2.erode(imgDilation, kernel, iterations=2 )

cv2.imshow('izu', img)
cv2.imshow('Bwizu', imgGray)
cv2.imshow('Bizu', imgBlur)
cv2.imshow('Cizu', imgCanny)
cv2.imshow('Dizu', imgDilation)
cv2.imshow('Eizu', imgEroded)




cv2.waitKey(0)
