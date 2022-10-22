import cv2
import numpy as np  
from myutils import stackImages




img = cv2.imread('Resources/lenna.png')
imgStack = stackImages(0.5,([img,img,img],[img,img,img]))

# img1 = cv2.imread('Resources/rig.jpg')
# img1 = cv2.resize(img1, (700, 700))
# img2 = cv2.imread('Resources/micheal.jpg')

# print(img1.shape)
# print(img2.shape)


# img1 = cv2.resize(img1, (0,0), None, 0.5, 0.5)
# img2 = cv2.resize(img2, (0,0), None, 0.5, 0.5)

# hor = np.hstack((img1, img2))
# ver = np.vstack((img1, img2))


# cv2.imshow('Horizontal', hor)
# cv2.imshow('Vertical', ver)

cv2.imshow('Imagestacks', imgStack)


cv2.waitKey(0)



