import cv2
import numpy as np 

# img = np.zeros((512,512,3), np.uint8)
# # img[:] = 255,0,0
# # print(img)

# cv2.line(img, (0,0,), (img.shape[1], img.shape[0]), (0,0,255), 3)
# cv2.rectangle(img, (300,100), (400,270), (0,255,0), cv2.FILLED)
# cv2.circle(img, (100,200), 50, (255,0,0), cv2.FILLED )
# cv2.putText(img, 'PyCv Shape works ', (75,400), cv2.FONT_HERSHEY_COMPLEX, 1, (0,150,0), 1)


img = cv2.imread('Resources/cards.jpg')
print(img.shape[:2])
width, height = img.shape[:2]
pts1 = np.float32([[158,36], [272,60], [123,195], [236,219]])
pts2 = np.float32([[0,0], [width,0], [0,height], [width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, matrix, (width, height))


cv2.imshow('image', img)
cv2.imshow('warp', output)

cv2.waitKey(0)