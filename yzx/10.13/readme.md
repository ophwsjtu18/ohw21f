**Because of the previous *VPN* problem, I couldn't log on to the *Github* website, so the time for the first week of homework was overdue. Dr. Xie also knows this situation, and I am very sorry!**

**Code**

```python
import numpy as np
import cv2
img=cv2.imread('a1f39428ecdc56ba195af814050991d4.jpeg',1)
for i in range(0,3):
    for j in range(0,3):
        cv2.rectangle(img,(50*i,50*j),(50*(1+i),50*(1+j)),(0,255,0),3)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

**Picture**

![cow_with_rectangle](https://github.com/ophwsjtu18/ohw21f/blob/d2b213f4f7844af74cb65c6895c9a5dd2493c94b/yzx/10.13/cow_rectangle.png)
