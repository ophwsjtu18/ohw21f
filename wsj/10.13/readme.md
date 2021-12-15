# 10.13作业
## 代码
```python
import numpy as np
import cv2
img=cv2.imread('cow.jpg',1)
for i in range(0,3):
    for j in range(0,3):
        cv2.rectangle(img,(50*i,50*j),(50*(1+i),50*(1+j)),(0,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
