import numpy as np
import cv2
cap=cv2.VideoCapture(0)

while(True):
    ret,inbox=cap.read()
    cv2.imshow('inbox',inbox)
    outbox=cv2.flip(inbox,1)
    cv2.imshow('outbox',outbox)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
