import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,0,255),3)

img = cv2.imread("cow.jpg",1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==115:
        cv2.imwrite("circleCowHollow.jpg",img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()