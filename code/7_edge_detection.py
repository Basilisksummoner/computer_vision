import os
import cv2


img = cv2.imread(os.path.join('.','data','image.jpg'))

edge_detection = cv2.Canny(img, 100, 400)

cv2.imshow('Frame', edge_detection)
cv2.waitKey(0)