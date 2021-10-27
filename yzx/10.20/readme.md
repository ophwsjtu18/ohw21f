**Task 1**

**Code**
```python
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
   if event==cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(img,(x,y),5,(0,0,255),3)
      
img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
   cv2.imshow('image',img)
   if cv2.waitKey(20)&0xFF==27:
    break
cv2.destroyAllWindows()
```

**Picture**

![circle](https://github.com/ophwsjtu18/ohw21f/blob/1bfd8244e6671f05537c5ee040475548a3081ad4/yzx/10.20/circle.png)

**Task 2**

**Code**
```python
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
```

**Picture**

![cow_circle](https://github.com/ophwsjtu18/ohw21f/blob/1bfd8244e6671f05537c5ee040475548a3081ad4/yzx/10.20/cow_circle.png)
