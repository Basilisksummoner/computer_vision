import os
import cv2


my_camera = cv2.VideoCapture(0)    # В аргументах пишем 0 (номер вебки начинается с нуля)


# Теперь визуализируем
while True:
    x, frame = my_camera.read()
    cv2.imshow('Camera', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):    # Тут мы пишем что будем ждать 40мс и
        break                               # если user нажмёт `q` `break` из цикла


my_camera.release()
cv2.destroyAllWindows()