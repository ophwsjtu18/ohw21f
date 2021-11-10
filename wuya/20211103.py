import cv2
import numpy as np

cap=cv2.VideoCapture(0)
if cap.isOpened()==False:
    exit()
cv2.namedWindow('mainWindow',cv2.WINDOW_AUTOSIZE)

while(True):
    ret,frame=cap.read()
    if ret==False:
        break
    framef=cv2.flip(frame,1)
    flash=np.hstack([frame,framef])
    cv2.imshow('mainWindow',flash)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()