# 作业

## 任务一

### 代码
```python
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
   if event==cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(img,(x,y),5,(0,255,255),3)
      
img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
   cv2.imshow('image',img)
   if cv2.waitKey(20)&0xFF==27:
    break
cv2.destroyAllWindows()
```
### 效果图
![sds](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/xiaoguotu1.png?raw=true)

## 任务二

### 代码
```python
import numpy as np
import cv2

img=cv2.imread('picture.jfif',1)

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
```

### 效果图
![sdsd](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/xiaoguotu2.png?raw=true)
