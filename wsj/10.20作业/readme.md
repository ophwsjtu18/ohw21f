# 10.20作业
## 任务一
### 代码
```python
import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
   if event==cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(img,(x,y),10,(255,0,255),4)
      
img=np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image1')
cv2.setMouseCallback('image1',draw_circle)

while(1):
   cv2.imshow('image1',img)
   if cv2.waitKey(20)&0xFF==27:
       cv2.imwrite('circle1.png',img)
       break
cv2.destroyAllWindows()
```
### 效果图
![sds](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/10.20作业/circle1.png）
