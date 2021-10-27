import numpy as np
import cv2

img=cv2.imread('a1f39428ecdc56ba195af814050991d4.jpeg',1)

def draw_circle(event,x,y,flags,param):
   if event==cv2.EVENT_RBUTTONDBLCLK:
      cv2.circle(img,(x,y),5,(0,0,255),-1)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image',draw_circle)

while(1):
   cv2.imshow('image',img)
   if cv2.waitKey(20)&0xFF==27:
      break
cv2.destroyAllWindows()



