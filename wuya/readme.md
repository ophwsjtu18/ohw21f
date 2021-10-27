# ohw21f

## chapter 1
Open Source Hardware

### chapter 1.1
Markdown

1. Table

| Num | Des | Val |
|-------|-------|-------|
| 1 | a | **123** |
| 2 | b | *45*6 |
| 9 | @ | ***43-*** |

2. Picture

![A Picture](/wuya/4k纯黑.png)

## 第二章 作业

### 202111013
```python
import cv2
img=cv2.imread("xixihaha.jpg",cv2.IMREAD_UNCHANGED)
a=[10,70,130]
for i in a:
    for j in a:
        cv2.rectangle(img,(i,j),(i+50,j+50),(0,255,0),3)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```
![20211013-1](/wuya/20211013-1.png)

### 20211020
#### 20211020-2
```python
import cv2
import numpy as np

img=np.zeros((512,512,3),np.uint8)
img.fill(255)

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,0,255),3)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()
```
![20211020-2](/wuya/20211020-2.png)

#### 20211020-3
```python
import cv2
import numpy as np

img=cv2.imread('xixihaha.jpg',cv2.IMREAD_UNCHANGED)

def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,0,255),-1)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.destroyAllWindows()
```
![20211020-3](/wuya/20211020-3.png)
