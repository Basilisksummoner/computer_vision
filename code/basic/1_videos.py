import os
import cv2


# Для чтения видео в cv2 исп .VideoCapture(путь)
video_1 = cv2.VideoCapture(os.path.join('.', 'data', 'video.mp4'))

# Теперь для визуализации видео
ret = True


while ret:
    ret, frame = video_1.read()     # .read() возвращает два значения
    if ret:
        cv2.imshow('Video', frame)
        cv2.waitKey(7)


# Чтобы не забивать память
video_1.release()
cv2.destroyAllWindows()