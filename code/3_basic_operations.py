import os
import cv2


img_1 = cv2.imread(os.path.join('.', 'data', 'image.jpg'))


print(img_1.shape)    # .shape возвращает 3 аргумента (высота, ширина, каналы цветов)   


# Basic operation 1. Resizing
resized_image = cv2.resize(img_1, (509,200))    # .resize два аргумента

# (230,100) - новая ширина и высота ! не наоборот !



# Basic operation 2. Cropping
cropped_image = img_1[30:450, 130:400]


cv2.imshow('Normal image', img_1)
cv2.imshow('Resized', resized_image)
cv2.imshow('Cropped', cropped_image)
cv2.waitKey(0)