```python
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:13:25 2021

@author: 申荣强
"""
import cv2 as cv
import numpy as np

def mouse_drawing(event,x,y,flags,param):
    if event==cv.EVENT_RBUTTONDBLCLK:
        cv.circle(str, (x,y), 100, (255,0,0),3)

str = np.zeros((512,512,3),np.uint8)
cv.namedWindow("mouse_demo")
cv.setMouseCallback("mouse_demo", mouse_drawing)
while True:
    cv.imshow("mouse_demo", str)
    a = cv.waitKey(10)
    if a == 27:
        break
cv.destoryAllWindows()
```
