# Assignments 10/20
*Adiricast*
## HOMEWORK 2
### 1
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/10201.PNG)

Code 
```python
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
  if event==cv2.EVENT_RBUTTONDBLCLK:
    cv2.circle(img,(x,y),5,(0,0,255),3)

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
  cv2.imshow('image',img)
  if cv2.waitKey(20)&0xFF==27:
       break
cv2.destroyAllWindows()

cv2.imshow('image',img)
```

### 1
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/10202.PNG)

Code 
```python
import cv2
import numpy as np


def draw_circle(event,x,y,flags,param):
  if event==cv2.EVENT_RBUTTONDBLCLK:
    cv2.circle(img,(x,y),5,(0,0,255),-1)

img=cv2.imread('R-C.jfif',cv2.IMREAD_UNCHANGED)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
  cv2.imshow('image',img)
  if cv2.waitKey(20)&0xFF==27:
       break
cv2.destroyAllWindows()

```


