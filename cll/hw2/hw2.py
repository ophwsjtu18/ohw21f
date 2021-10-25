# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 01:12:06 2021

@author: LilyChang
"""
import cv2
import numpy as np
#mouse callback function


def drawCircle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        radius=param[0]
        color=param[1]
        thickness=param[2] # If thickness=-1, draw solid circles
        cv2.circle(img,(x,y),radius,color,thickness)

#%% Task1: Draw hollow circles
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
radius=10
color=(0,0,255)
thickness=3
cv2.setMouseCallback('image',drawCircle,[radius,color,thickness])
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
            break
cv2.imwrite('Task1_hollowCircle.png',img)
cv2.destroyAllWindows()


#%% Task 2: Draw solid circles
thickness=-1 # Draw solid circles
img=cv2.imread("cow.jpg")
cv2.namedWindow('cow')
cv2.setMouseCallback('cow',drawCircle,[radius,color,thickness])
while(1):
    cv2.imshow('cow',img)
    if cv2.waitKey(20)&0xFF==27:
            break
cv2.imwrite('Task2_solidCircle.png',img)
cv2.destroyAllWindows()