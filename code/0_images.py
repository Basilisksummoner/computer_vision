import os     # Начинаем любой код с импорта библиотек
import cv2


image_path = os.path.join('.','data', 'image.jpg') # Указываем путь 
img_1 = cv2.imread(image_path)

# Можно не указывать путь а сразу писать:
# img_1 = cv2.imread(os.path.join('.','data', 'image.jpg'))

cv2.imshow('Image',img_1)  # Визуализируем, принимает два аргумента 
cv2.waitKey(0)             # waitKey чтобы окно с image не закрывалось

new_image = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)

cv2.imshow('Image_2',new_image)  # Визуализируем, принимает два аргумента 
cv2.waitKey(0)           