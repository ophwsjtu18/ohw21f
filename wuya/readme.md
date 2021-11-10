# ohw21f

## chapter 1
<details>
    <summary>Unfold</summary>

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

</details>
    
## 第二章 作业

### 202111013
<details>
    <summary>展开</summary>

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

</details>

### 20211020
<details>
    <summary>展开</summary>
    
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

</details>

### 20211027
<details>
    <summary>展开</summary>
    
```python
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

fill=1

def createHouse(x,y,z):
    building=[
        (1,(0,0,0),(x-1,y-z,z-1),0),#Remove All Blocks
        (1,(0,0,0),(x-1,0,z-1),5),#Floor
        (1,(0,1,0),(0,y-2,z-1),4),#Wall 1
        (1,(0,1,0),(x-1,y-2,0),4),#Wall 2
        (1,(0,1,9),(x-1,y-2,z-1),4),#Wall 3
        (1,(9,1,0),(x-1,y-2,z-1),4),#Wall 4
        (1,(0,y-1,0),(x-1,y-1,z-1),20)]#Roof
    if y<4:
        return building

    if x%2:#Door
        building+=[(1,(int((x-1)/2),2,0),(int((x-1)/2),2,0),0)]
        building+=[(1,(int((x-1)/2),1,0),(int((x-1)/2),1,0),0)]
    else:
        building+=[(1,(int(x/2-1),2,0),(int(x/2),2,0),0)]
        building+=[(1,(int(x/2-1),1,0),(int(x/2),1,0),0)]

    if y<5:#Window
        if z%2:
            building+=[(1,(x-1,1,int((z-3)/2)),(x-1,2,int((z+1)/2)),20)]
        else:
            building+=[(1,(x-1,1,int((z-2)/2)),(x-1,2,int(z/2)),20)]
    else:
        if z%2:
            building+=[(1,(x-1,2,int((z-3)/2)),(x-1,3,int((z+1)/2)),20)]
        else:
            building+=[(1,(x-1,2,int((z-2)/2)),(x-1,3,int(z/2)),20)]
    return building

def buildCMD(base,mc,building):
    for command in building:
        if command[0]==1:
            b=command[3]
            x=range(command[1][0],command[2][0]+1)
            y=range(command[1][1],command[2][1]+1)
            z=range(command[1][2],command[2][2]+1)
            print(b,x,y,z)
            for _x in x:
                for _y in y:
                    for _z in z:
                        mc.setBlock(base[0]+_x,base[1]+_y,base[2]+_z,b)

def house(x,y,z,l,w,h):
    buildCMD((x,y,z),mc,createHouse(l,h,w))

while(1):
    pos=mc.player.getTilePos()
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    hits=mc.events.pollBlockHits() 
    for hit in hits:
        base=(hit.pos.x+5,hit.pos.y+5,hit.pos.z+5)
        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
        mx=hit.pos.x
        my=hit.pos.y
        mz=hit.pos.z
        house(mx,my,mz,10,10,6)
        house(mx+20,my,mz,14,5,12)
        house(mx+40,my,mz,18,10,30)
        break

    time.sleep(0.5)
```
![20211027](/wuya/20211027.png)

</details>

### 20211103
<details>
<summary>展开</summary>
    
```python
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
if cap.isOpened()==False:
    exit()
cv2.namedWindow('mainWindow',cv2.WINDOW_AUTOSIZE)

while(True):
    ret,frame=cap.read()
    if ret==False:
        break
    framef=cv2.flip(frame,1)
    flash=np.hstack([frame,framef])
    cv2.imshow('mainWindow',flash)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```
![20211103](/wuya/20211103.png)
    
</details>
