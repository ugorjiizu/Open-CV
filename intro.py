import cv2
# img = cv2.imread('Resources/izu.jpg')

# cv2.imshow('izu', img)
# cv2.waitKey(0)

frameWidth = 400
frameHeight = 400

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success,img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow('Video', img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   