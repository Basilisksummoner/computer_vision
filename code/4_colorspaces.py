import os
import cv2


bird_img = cv2.imread(os.path.join('.','data','image.jpg'))


# Чтобы конверитровать цветные каналы с BGR
new_image = cv2.cvtColor(bird_img, cv2.COLOR_BGR2RGB)
# .COLOR_BGR2GRAY - в серый
# .COLOR_BGR2HSV - для color detecting

cv2.imshow('Converted Image', new_image)
cv2.waitKey(0)