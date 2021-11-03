# 从摄像头中读取图像并且翻转显示
## 申荣强 2021/11/3
```python
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 22:30:02 2021

@author: 申荣强
"""
import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    ret, img = cap.read()
    if ret == True:
        #cv.imshow("input", img)
        h_image = cv.flip(img,1)
        cv.imshow("output", h_image)
    if(cv.waitKey(20)&0xff==27):
        break
cap.release()
cv.destroyAllWindows()

```
![](https://s3.bmp.ovh/imgs/2021/11/fd7cb80a6889ee1f.png)
