import numpy as np
import cv2

cap = cv2.VideoCapture(0)

ret,frame = cap.read()
cap.release()

cv2.imshow('hw4-1pic',frame)
cv2.imwrite('hw4-1pic',frame)

cv2.waiKey(0.25)
cv2.destroyAllWindows()
