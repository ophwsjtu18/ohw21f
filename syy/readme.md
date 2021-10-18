# Assignments 10/13

## chapter1
### openCV intoduction


*Adiricast*

## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/%E6%8D%95%E8%8E%B7.PNG)

Code 
```python
import cv2
import numpy as np
img=cv2.imread('R-C.jfif',cv2.IMREAD_UNCHANGED)
linethick=3
color=(0,255,0)
for i in range(0,150,50):
 for j in range(0,150,50):
  lt=(i,j)
  rb=(i+50,j+50)
  cv2.rectangle(img,lt,rb,color,linethick,4)
cv2.imshow('image',img)




