# 第二次作业
## 鼠标右键双击画圆
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:36:03 2021

@author: 申荣强
"""
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

def mouse_drawing(event,x,y,flags,param):
    if event==cv.EVENT_RBUTTONDBLCLK:
        cv.circle(str, (x,y), 5, (0,0,255),3)

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
![1dac4103a9fb296c18bdde23d5eb754.png](https://i.loli.net/2021/10/23/5CPHGcquVhBylbs.png)
## 在牛的图片基础上完成鼠标画圆
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 18:36:03 2021

@author: 申荣强
"""
# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

def mouse_drawing(event,x,y,flags,param):
    if event==cv.EVENT_RBUTTONDBLCLK:
        cv.circle(str, (x,y), 5, (0,0,255),-1)

#str = np.zeros((512,512,3),np.uint8)
str = cv.imread("D:/picturebox/af13a9fca43f95e27da1504dac1b9f8.jpg")
cv.namedWindow("mouse_demo")
cv.setMouseCallback("mouse_demo", mouse_drawing)
while True:
    cv.imshow("mouse_demo", str)
    if cv.waitKey(20)&0xFF ==27:
        break
cv.destoryAllWindows()
```
![6949594a7fdf242b3b21725f16b37db.png](https://i.loli.net/2021/10/23/361T2rvM94WmAVS.png)
