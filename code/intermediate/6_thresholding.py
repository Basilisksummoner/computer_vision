import os
import cv2


img = cv2.imread(
    os.path.join('.','data','image.jpg')
)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img, 80, 120, cv2.THRESH_BINARY)

thresh_1 = cv2.adaptiveThreshold(
    img_gray, 
    255, 
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
    cv2.THRESH_BINARY,
    11,
    2
)

cv2.imshow('thresh', thresh_1)
cv2.imshow('Original bird', img)
cv2.waitKey(0)