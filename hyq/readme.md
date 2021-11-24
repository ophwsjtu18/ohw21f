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


## 2021.11.15 
### HOMEWORK

#### 导入yolo文件
```python
import numpy as np
import cv2
import os
import time
from mcpi.minecraft import Minecraft

yolo_dir = 'C:/Users/skywang/Desktop/yolov3/yolov3/'  # YOLO文件路径一定不能有中文在路径里面
weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
CONFIDENCE = 0.5  # 过滤弱检测的最小概率
THRESHOLD = 0.4  # 非最大值抑制阈值

with open(labelsPath, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')
# 加载网络、配置权重
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)  ## 利用下载的文件

#初始化
mc=Minecraft.create()
cap=cv2.VideoCapture(0)
count = 0
```

#### 主循环
```python
while True:
    pos = mc.player.getTilePos()
    ret,img=cap.read()
    img = cv2.flip(img,1)
    
    # 加载图片、转为blob格式、送入网络输入层 获取网络输出层信息（所有输出层的名字），设定并前向传播
    start = time.time()
    (H,W) = img.shape[:2]
    blobImg = cv2.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
    net.setInput(blobImg)  ## 调用setInput函数将图片送入输入层
    #net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
    #net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    outInfo = net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
    layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
    boxes = [] # 所有边界框（各层结果放一起）
    confidences = [] # 所有置信度
    classIDs = [] # 所有分类ID
    for out in layerOutputs:  # 各个输出层
        for detection in out:  # 各个框框
            # 拿到置信度
            scores = detection[5:]  # 各个类别的置信度
            classID = np.argmax(scores)  # 最高置信度的id即为分类id
            confidence = scores[classID]  # 拿到置信度
            # 根据置信度筛查
            if confidence > CONFIDENCE:
                box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
                (centerX, centerY, width, height) = box.astype("int")
                x = int(centerX - (width / 2))
                y = int(centerY - (height / 2))
                boxes.append([x, y, int(width), int(height)])
                confidences.append(float(confidence))
                classIDs.append(classID)
    #应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
    # 应用检测结果
    np.random.seed(42)
    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
    
    if len(idxs) > 0:
        for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
            if labels[classIDs[i]] == 'cell phone': # 仅展示与使用cell phone标签
                cordx = pos.x
                cordy = pos.y
                cordz = pos.z
                if count == 0: # 记录cell phone的初位置
                    x0,y0,w0,h0 = boxes[i][0],boxes[i][1],boxes[i][2],boxes[i][3]
                    count = count+1
                else:
                    x,y,w,h = boxes[i][0],boxes[i][1],boxes[i][2],boxes[i][3]
                    #print(x,y,w,h)
                    #判断更新位置和初位置的关系，具体阈值参数由上方print函数与经验取得
                    if h > h0+50:
                        cordz = cordz+5
                        mc.player.setTilePos(cordx,cordy,cordz)
                        print('go forword')
                        continue
                    if h < h0-40:
                        cordz = cordz-5
                        mc.player.setTilePos(cordx,cordy,cordz)
                        print('go back')
                        continue
                    if x < x0-100:
                        cordx = cordx+5
                        print('go left')
                    if x > x0+100:
                        cordx = cordx-5
                        print('go right')
                    mc.player.setTilePos(cordx,cordy,cordz)
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
                    text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
                    cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  #cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
    end = time.time()
    print("YOLO1 took {:.6f} seconds".format(end - start))
    
    #展示并保存
    cv2.imshow('target detect result1', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

#### 效果视频
MP4 FILE:
https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/video_yolo.mp4?raw=true

## 2021.11.24 
### HOMEWORK

####  HW1
```python
from mcpi.minecraft import Minecraft
import mcpi.block as block

class House:
    def __init__(self,x,y,z,L,W,H):
        self.mc = Minecraft.create()
        self.posx = x
        self.posy = y
        self.posz = z
        self.L = L
        self.W = W
        self.H = H
        
    def build(self):
        for x in range(self.L):
            for z in range(self.W):
                self.mc.setBlock(self.posx+x,self.posy,self.posz+z,block.WOODEN_SLAB.id)
                self.mc.setBlock(self.posx+x,self.posy+self.H,self.posz+z,block.GLASS.id)
    
        for x in range(self.L+2):
            for y in range(self.H+1):
                self.mc.setBlock(self.posx+x-1,self.posy+y,self.posz-1,block.DIAMOND_BLOCK.id)
                self.mc.setBlock(self.posx+x-1,self.posy+y,self.posz+self.W,block.DIAMOND_BLOCK.id)
        for z in range(self.W+2):
            for y in range(self.H+1):
                self.mc.setBlock(self.posx-1,self.posy+y,self.posz+z-1,block.DIAMOND_BLOCK.id)
                self.mc.setBlock(self.posx+self.L,self.posy+y,self.posz+z-1,block.DIAMOND_BLOCK.id)
        for z in range(2):
            for y in range(2):
                self.mc.setBlock(self.posx-1,self.posy+y+int((self.H-1)/2),self.posz+z+int((self.W-1)/2),20)
        self.mc.setBlock(self.posx+int((self.L-1)/2),self.posy+1,self.posz-1,0)
        self.mc.setBlock(self.posx+int((self.L-1)/2),self.posy+2,self.posz-1,0)
    
    def gohome(self):
        self.mc.player.setTilePos(self.posx+1,self.posy+1,self.posz+1)
        
house1 = House(100,20,100,10,10,10)
house1.build()
house1.gohome()
```

#### 效果图
![1](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/hw6-1.png?raw=true)

####  HW2
```python
from mcpi.minecraft import Minecraft
import mcpi.block as block

class House:
    def __init__(self,x,y,z,L,W,H):
        self.mc = Minecraft.create()
        self.posx = x
        self.posy = y
        self.posz = z
        self.L = L
        self.W = W
        self.H = H
        
    def build(self):
        for x in range(self.L):
            for z in range(self.W):
                self.mc.setBlock(self.posx+x,self.posy,self.posz+z,block.WOODEN_SLAB.id)
                self.mc.setBlock(self.posx+x,self.posy+self.H,self.posz+z,block.GLASS.id)
    
        for x in range(self.L+2):
            for y in range(self.H+1):
                self.mc.setBlock(self.posx+x-1,self.posy+y,self.posz-1,block.DIAMOND_BLOCK.id)
                self.mc.setBlock(self.posx+x-1,self.posy+y,self.posz+self.W,block.DIAMOND_BLOCK.id)
        for z in range(self.W+2):
            for y in range(self.H+1):
                self.mc.setBlock(self.posx-1,self.posy+y,self.posz+z-1,block.DIAMOND_BLOCK.id)
                self.mc.setBlock(self.posx+self.L,self.posy+y,self.posz+z-1,block.DIAMOND_BLOCK.id)
        for z in range(2):
            for y in range(2):
                self.mc.setBlock(self.posx-1,self.posy+y+int((self.H-1)/2),self.posz+z+int((self.W-1)/2),20)
        self.mc.setBlock(self.posx+int((self.L-1)/2),self.posy+1,self.posz-1,0)
        self.mc.setBlock(self.posx+int((self.L-1)/2),self.posy+2,self.posz-1,0)
    
    def gohome(self):
        self.mc.player.setTilePos(self.posx+1,self.posy+1,self.posz+1)
        
house1 = House(100,20,100,10,10,10)
house2 = House(200,20,200,20,20,5)
house3 = House(300,20,300,5,20,20)

house1.build()
house2.build()
house3.build()

#house1.gohome()
#house2.gohome()
house3.gohome()
```

#### 效果图
![1](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/hw6-2_1.png?raw=true)
![2](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/hw6-2_2.png?raw=true)
![3](https://github.com/ophwsjtu18/ohw21f/blob/main/hyq/hw6-2_3.png?raw=true)

