import cv2
path = 'Resources/micheal.jpg' 
img = cv2.imread(path)
print(img.shape)

frameWidth = 400
frameHeight = 400

imgResize = cv2.resize(img, (frameWidth, frameHeight))
print(imgResize.shape)

imgCropped = img[0:700, 100:550]

imgCropResize = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))


cv2.imshow('tems', img)
cv2.imshow('tems resize', imgResize)
cv2.imshow('micheal cropped', imgCropped)
cv2.imshow('micheal croppedresize', imgCropResize)

cv2
cv2.waitKey(0)