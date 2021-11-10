import numpy as np
import cv2
cap = cv2.VideoCapture(0)
cv2.namedWindow("left")
cv2.namedWindow("right")

while True:
    ret,frame = cap.read()
    # print(ret)
    # print(frame)
    if ret:
        cv2.imshow('right',frame)
        frame = cv2.flip(frame,1)
        # 似乎加了以后反而镜像了
        cv2.imshow('left',frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()