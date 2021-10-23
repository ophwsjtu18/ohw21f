```python
import cv2
import numpy as np
img = cv2.imread('cattle.webp', 1)

"""
draw 3x3=9 rectangle 
thickness = 3
green (0, 255, 0)
"""
cv2.rectangle(img, (0,0), (150,150), (0, 255, 0), 3)
cv2.line(img, (50,0), (50,150), (0, 255, 0), 3)
cv2.line(img, (100, 0), (100, 150), (0, 255, 0), 3)
cv2.line(img, (0, 50), (150, 50), (0, 255, 0), 3)
cv2.line(img, (0, 100), (150, 100), (0, 255, 0),3)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
![HW1](https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/%E4%BD%9C%E4%B8%9A1.png)
