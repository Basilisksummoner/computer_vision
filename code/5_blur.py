import os
import cv2


img = cv2.imread(os.path.join('.','data','image.jpg'))


# Указываем область блюра
k_size = 7
blur_img = cv2.blur(img, (k_size, k_size)) # .blur принимает два аргумента


# Gaussian Blur
gaussian_blur = cv2.blur(img, (k_size, k_size), 3) # 3 аргумента


# Median Blur
median_blur = cv2.medianBlur(img, k_size) # 2 аргумента


cv2.imshow('Original', img)
cv2.imshow('blur_img', blur_img)
cv2.imshow('gaussian_blur', gaussian_blur)
cv2.imshow('median_blur', median_blur)
cv2.waitKey(0)