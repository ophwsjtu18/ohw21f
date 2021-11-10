1.

```PYTHON
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret,frame = cap.read()
cap.release()

cv2.imshow('frame',frame)
cv2.waitKey(0)
```
![HW4_1](https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW4_1.png)
2.

```PYTHON
"""
Created on 2021 11 09
@author: zjw
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

3.

```python
"""
Created on 2021 11 09
@author: zjw
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    # Our operations on the frame come here
    frame2 = cv2.flip(frame, 1)
    frame2 = np.hstack((frame, frame2))

    # Display the resulting frame
    cv2.imshow('frame',frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
![HW4_2](https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW4_2.png)
