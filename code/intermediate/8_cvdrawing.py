import os
import cv2

img = cv2.imread(os.path.join('.','data','image.jpg'))

cv2.line(img, (100, 150), (200, 350), (0,255,0), 3)
cv2.rectangle(img, (500, 190), (70, 500), (0,255,0), 3)
cv2.circle(img, (300, 90), 70, (0,255,0), 3)


cv2.imshow('frame', img)
cv2.waitKey(0)