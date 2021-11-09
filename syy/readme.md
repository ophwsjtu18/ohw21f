# Assignments 10/27
*Adiricast*
## HOMEWORK 3
### 1
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11031.PNG)

Code 
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret,frame = cap.read()
cap.release()

cv2.imshow('cam',frame)
cv2.imwrite('cam.png',frame)
#cv2.destroyAllWindows()

```

### 2
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11032.PNG)

Code 
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('video.avi',fourcc,20.0,(1920,1080))
    while(1):
        ret,frame = cap.read()
        if ret==True:
           
             video.write(frame) 
             cv2.imshow('frame',frame)
             if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break


cap.release()
video.release()
cv2.destroyAllWindows()

```
### 3
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11033.PNG)

Code 
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('video.avi',fourcc,20.0,(1920,1080))
    while(1):
        ret,frame = cap.read()
        if ret==True:
             frameflip = cv2.flip(frame,1)
             frameflix=np.hstack((frame,frameflip))

             video.write(frameflip) 
             cv2.imshow('frame',frameflix)
             if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break


cap.release()
video.release()
cv2.destroyAllWindows()

```



