## 2021.10.15 
### HOMEWORK

#### 导入图片
```python
import numpy as np
import cv2
img = cv2.imread('1.jpg',cv2.IMREAD_COLOR)
# cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
# cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
# cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道
```

#### 在左上角画9个矩形
```python
for i in range(0,3):
    for j in range(0,3):
        cv2.rectangle(img,(50*i,50*j),(50*i+50,50*j+50),(0,255,0),3)
# emptyImage = np.zeros(img.shape, np.uint8)
# cv2.imshow("EmptyImage",emptyImage)
# empty2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",empty2)
```
#### 展示并保存
```python
cv2.imshow("Image",img)
cv2.imwrite('1-1.jpg',img)
cv2.waitKey (0)
cv2.destroyAllWindows()
```
#### 效果图
![example](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/1-1.jpg?raw=true)


## 2021.10.23 
### HOMEWORK

#### 1. 复现代码并画圆
```python
import cv2
import numpy as np
#mouse callback function
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,0,255),3) # 创建图像与窗口并将窗口与回调函数绑定
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:
        break
cv2.imwrite('1-3.jpg',img)  #自动保存
cv2.destroyAllWindows()
```
#### 效果图
![22](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/1-3.jpg?raw=true)


#### 2. 在牛的图片上画实心圆
```python
import cv2
import numpy as np
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img,(x,y),5,(0,0,255),-1)

print('----Press ESC to quit----')
img = cv2.imread("C:/Users/skywang/Desktop/1.jpeg")
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',draw_circle)

while(1):
    cv2.imshow("Image",img)
    if cv2.waitKey(20)&0xFF == 27:
        break
        
cv2.imwrite('1-2.jpg',img)  #自动保存
cv2.destroyAllWindows()
```

#### 效果图
![22222222](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/1-2.jpg?raw=true)


## 2021.10.30 
### HOMEWORK

####  HW1
```python
from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()
#mc.player.setTilePos(-84,-3,29)   #移动至平地

##while 1:
##    pos=mc.player.getTilePos()
##    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
##    time.sleep(0.5)

pos=mc.player.getTilePos()
for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,block.WOODEN_SLAB.id)
        mc.setBlock(pos.x+x,pos.y+6,pos.z+z,block.GLASS.id)

for x in range(12):
    for y in range(7):
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z-1,block.DIAMOND_BLOCK.id)
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z+10,block.DIAMOND_BLOCK.id)
        mc.setBlock(pos.x-1,pos.y+y,pos.z+x-1,block.DIAMOND_BLOCK.id)
        mc.setBlock(pos.x+10,pos.y+y,pos.z+x-1,block.DIAMOND_BLOCK.id)
for z in range(2):
    for y in range(2):
        mc.setBlock(pos.x-1,pos.y+y+2,pos.z+z+4,20)
mc.setBlock(pos.x+5,pos.y+1,pos.z-1,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z-1,0)
```
![1](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/4.png?raw=true)
![2](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/3.png?raw=true)

####  HW2
```python
from mcpi.minecraft import Minecraft
import mcpi.block as block

def house(x0,y0,z0,L,W,H):
    mc.player.setTilePos(x0+1,y0+1,z0+1)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0,z0+z,block.WOODEN_SLAB.id)
            mc.setBlock(x0+x,y0+H,z0+z,block.GLASS.id)

    for x in range(L+2):
        for y in range(H+1):
            mc.setBlock(x0+x-1,y0+y,z0-1,block.DIAMOND_BLOCK.id)
            mc.setBlock(x0+x-1,y0+y,z0+W,block.DIAMOND_BLOCK.id)
    for z in range(W+2):
        for y in range(H+1):
            mc.setBlock(x0-1,y0+y,z0+z-1,block.DIAMOND_BLOCK.id)
            mc.setBlock(x0+L,y0+y,z0+z-1,block.DIAMOND_BLOCK.id)
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0-1,y0+y+int((H-1)/2),z0+z+int((W-1)/2),20)
    mc.setBlock(x0+int((L-1)/2),y0+1,z0-1,0)
    mc.setBlock(x0+int((L-1)/2),y0+2,z0-1,0)

mc=Minecraft.create()
for x in range(3):
    msg_1=input("input the coordinate (use ',' to split) : ").split(',')
    msg_2=input("input the length width height (use ',' to split) : ").split(',')
    cord=[int(x) for x in msg_1]
    size=[int(x) for x in msg_2]
    house(cord[0],cord[1],cord[2],size[0],size[1],size[2])
```
![3](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/1.png?raw=true)
![4](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/2.png?raw=true)


## 2021.11.07
### HOMEWORK

####  HW1 打开摄像头
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret,frame = cap.read()
cap.release()

cv2.imshow('frame',frame)
cv2.imwrite('hw1.png',frame)
#cv2.destroyAllWindows()
```
![110701](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/hw1.png?raw=true)

####  HW2 用while True
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi',fourcc,20.0,(640,480))
    while(1):
        ret,frame = cap.read()
        if ret==True:
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break
else:
    print("The camera cannot be initialized!")

cap.release()
out.release()
cv2.destroyAllWindows()
```
MP4 FILE:
https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/video_Trim.mp4?raw=true

####  HW3 opencv clip左右镜像
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if cap.isOpened():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video2.avi',fourcc,20.0,(1280,480))
    while(1):
        ret,frame1 = cap.read()
        if ret==True:
            frame2 = cv2.flip(frame1, 1)
            framemix = np.hstack((frame1, frame2))
            cv2.imshow('frame', framemix)
            out.write(framemix)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break
else:
    print("The camera cannot be initialized!")

cap.release()
out.release()
cv2.destroyAllWindows()
```
![110703](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/video2_Moment.jpg?raw=true)

