import cv2
import numpy as np


def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(0,0,255),3)


path="D:/sc/cow.jpg"
img=cv2.imread(path,cv2.IMREAD_COLOR)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break

cv2.destroyAllWindows ()
