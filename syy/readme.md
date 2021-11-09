# Assignments 10/27
*Adiricast*
## HOMEWORK 3
### 1
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11301.png)

Code 
```python
from mcpi.minecraft import Minecraft
import time


mc=Minecraft.create()
pos=mc.player.getTilePos()

for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,126)
        mc.setBlock(pos.x+x,pos.y+6,pos.z+z,126)

for x in range(12):
    for y in range(7):
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z-1,46)
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z+10,46)
        mc.setBlock(pos.x-1,pos.y+y,pos.z+x-1,46)
        mc.setBlock(pos.x+10,pos.y+y,pos.z+x-1,46)
for z in range(2):
    for y in range(2):
        mc.setBlock(pos.x-1,pos.y+y+2,pos.z+z+4,20)
mc.setBlock(pos.x+5,pos.y+1,pos.z-1,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z-1,0)


```

### 2
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11302.png)

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
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11303.png)

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



