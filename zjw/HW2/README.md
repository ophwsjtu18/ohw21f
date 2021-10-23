```python
"""
Created on 2021/10/23
author: zjw
"""
import cv2
import numpy as np

def draw_circle(event, x, y, flag, param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img, (x,y), 5, (0, 0, 255), 3)

img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if  cv2.waitKey(20) & 0xff == 27:
        break

cv2.destroyAllWindows()
```
![HW2_1](https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW2_1.png)

```python
"""
2021 10 20
HW2
"""
import cv2
import numpy as np

#mouse callback function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
        # 创建图像与窗口并将窗口与回调函数绑定

img = cv2.imread('cattle.webp', 1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27: # ascii(27) = ESC
        break
cv2.destroyAllWindows()
```
![HW2_2](https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW2_2.png)
