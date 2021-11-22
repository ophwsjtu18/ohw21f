# ohw21f

## chapter 1
><details>
>    <summary>Unfold</summary>
>
>Open Source Hardware
>
>### chapter 1.1
>Markdown
>
>1. Table
>
>| Num | Des | Val |
>|-------|-------|-------|
>| 1 | a | **123** |
>| 2 | b | *45*6 |
>| 9 | @ | ***43-*** |
>
>2. Picture
>
>![A Picture](/wuya/4k纯黑.png)
>
></details>
    
## 第二章 作业

### 202111013
><details>
>    <summary>展开</summary>
>
>```python
>import cv2
>img=cv2.imread("xixihaha.jpg",cv2.IMREAD_UNCHANGED)
>a=[10,70,130]
>for i in a:
>    for j in a:
>        cv2.rectangle(img,(i,j),(i+50,j+50),(0,255,0),3)
>cv2.imshow("img",img)
>cv2.waitKey(0)
>cv2.destroyAllWindows()
>
>```
>![20211013-1](/wuya/20211013-1.png)
>    
></details>


### 20211020
><details>
>    <summary>展开</summary>
>    
>#### 20211020-2
>```python
>import cv2
>import numpy as np
>
>img=np.zeros((512,512,3),np.uint8)
>img.fill(255)
>
>def draw_circle(event,x,y,flags,param):
>    if event==cv2.EVENT_RBUTTONDBLCLK:
>        cv2.circle(img,(x,y),5,(0,0,255),3)
>
>cv2.namedWindow('image')
>cv2.setMouseCallback('image',draw_circle)
>
>while(1):
>    cv2.imshow('image',img)
>    if cv2.waitKey(20)&0xFF==27:
>        break
>cv2.destroyAllWindows()
>```
>![20211020-2](/wuya/20211020-2.png)
>
>#### 20211020-3
>```python
>import cv2
>import numpy as np
>
>img=cv2.imread('xixihaha.jpg',cv2.IMREAD_UNCHANGED)
>
>def draw_circle(event,x,y,flags,param):
>    if event==cv2.EVENT_RBUTTONDBLCLK:
>        cv2.circle(img,(x,y),5,(0,0,255),-1)
>
>cv2.namedWindow('image')
>cv2.setMouseCallback('image',draw_circle)
>
>while(1):
>    cv2.imshow('image',img)
>    if cv2.waitKey(20)&0xFF==27:
>        break
>cv2.destroyAllWindows()
>```
>![20211020-3](/wuya/20211020-3.png)
>
></details>


### 20211027
><details>
>    <summary>展开</summary>
>    
>```python
>from mcpi.minecraft import Minecraft
>import time
>
>mc=Minecraft.create()
>pos=mc.player.getTilePos()
>
>fill=1
>
>def createHouse(x,y,z):
>    building=[
>        (1,(0,0,0),(x-1,y-z,z-1),0),#Remove All Blocks
>        (1,(0,0,0),(x-1,0,z-1),5),#Floor
>        (1,(0,1,0),(0,y-2,z-1),4),#Wall 1
>        (1,(0,1,0),(x-1,y-2,0),4),#Wall 2
>        (1,(0,1,9),(x-1,y-2,z-1),4),#Wall 3
>        (1,(9,1,0),(x-1,y-2,z-1),4),#Wall 4
>        (1,(0,y-1,0),(x-1,y-1,z-1),20)]#Roof
>    if y<4:
>        return building
>
>    if x%2:#Door
>        building+=[(1,(int((x-1)/2),2,0),(int((x-1)/2),2,0),0)]
>        building+=[(1,(int((x-1)/2),1,0),(int((x-1)/2),1,0),0)]
>    else:
>        building+=[(1,(int(x/2-1),2,0),(int(x/2),2,0),0)]
>        building+=[(1,(int(x/2-1),1,0),(int(x/2),1,0),0)]
>
>    if y<5:#Window
>        if z%2:
>            building+=[(1,(x-1,1,int((z-3)/2)),(x-1,2,int((z+1)/2)),20)]
>        else:
>            building+=[(1,(x-1,1,int((z-2)/2)),(x-1,2,int(z/2)),20)]
>    else:
>        if z%2:
>            building+=[(1,(x-1,2,int((z-3)/2)),(x-1,3,int((z+1)/2)),20)]
>        else:
>            building+=[(1,(x-1,2,int((z-2)/2)),(x-1,3,int(z/2)),20)]
>    return building
>
>def buildCMD(base,mc,building):
>    for command in building:
>        if command[0]==1:
>            b=command[3]
>            x=range(command[1][0],command[2][0]+1)
>            y=range(command[1][1],command[2][1]+1)
>            z=range(command[1][2],command[2][2]+1)
>            print(b,x,y,z)
>            for _x in x:
>                for _y in y:
>                    for _z in z:
>                        mc.setBlock(base[0]+_x,base[1]+_y,base[2]+_z,b)
>
>def house(x,y,z,l,w,h):
>    buildCMD((x,y,z),mc,createHouse(l,h,w))
>
>while(1):
>    pos=mc.player.getTilePos()
>    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
>
>    hits=mc.events.pollBlockHits() 
>    for hit in hits:
>        base=(hit.pos.x+5,hit.pos.y+5,hit.pos.z+5)
>        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
>        mx=hit.pos.x
>        my=hit.pos.y
>        mz=hit.pos.z
>        house(mx,my,mz,10,10,6)
>        house(mx+20,my,mz,14,5,12)
>        house(mx+40,my,mz,18,10,30)
>        break
>
>    time.sleep(0.5)
>```
>![20211027](/wuya/20211027.png)
>    
></details>


### 20211103

><details>
><summary>展开</summary>
>    
>```python
>import cv2
>import numpy as np
>
>cap=cv2.VideoCapture(0)
>if cap.isOpened()==False:
>    exit()
>cv2.namedWindow('mainWindow',cv2.WINDOW_AUTOSIZE)
>
>while(True):
>    ret,frame=cap.read()
>    if ret==False:
>        break
>    framef=cv2.flip(frame,1)
>    flash=np.hstack([frame,framef])
>    cv2.imshow('mainWindow',flash)
>    if cv2.waitKey(1)&0xFF==ord('q'):
>        break
>
>cap.release()
>cv2.destroyAllWindows()
>```
>![20211103](/wuya/20211103.png)
>    
></details>

### 20211110

><details>
><summary>展开</summary>
>    
>```python
>from math import sqrt
>import numpy as np
>import cv2
>import os
>import time
>from mcpi.minecraft import Minecraft
>import serial
>
>yolo_dir = 'E:/python/yolov3/yolov3'  # YOLO文件路径一定不能有中文在路径里面
>weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
>configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
>labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
>imgPath = os.path.join(yolo_dir, 'person.jpg')  # 测试图像
>CONFIDENCE = 0.5  # 过滤弱检测的最小概率
>THRESHOLD = 0.4  # 非最大值抑制阈值
>
>with open(labelsPath, 'rt') as f:
>    labels = f.read().rstrip('\n').split('\n')
># 加载网络、配置权重
>net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)  ## 利用下载的文件
>
>cap=cv2.VideoCapture(0)
>mc=Minecraft.create()
>#ser=serial.Serial('COM5')
>
>while True:
>    # 加载图片、转为blob格式、送入网络输入层 获取网络输出层信息（所有输出层的名字），设定并前向传播
>    start = time.time()
>    #img = cv2.imread(imgPath)
>    ret,frame=cap.read()
>    img=cv2.flip(frame,1)
>    (H, W) = img.shape[:2]
>    blobImg = cv2.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
>    net.setInput(blobImg)  ## 调用setInput函数将图片送入输入层
>    #net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
>    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
>    outInfo = net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
>    layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
>    boxes = [] # 所有边界框（各层结果放一起）
>    confidences = [] # 所有置信度
>    classIDs = [] # 所有分类ID
>    for out in layerOutputs:  # 各个输出层
>        for detection in out:  # 各个框框
>            # 拿到置信度
>            scores = detection[5:]  # 各个类别的置信度
>            classID = np.argmax(scores)  # 最高置信度的id即为分类id
>            confidence = scores[classID]  # 拿到置信度
>            # 根据置信度筛查
>            if confidence > CONFIDENCE:
>                box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
>                (centerX, centerY, width, height) = box.astype("int")
>                x = int(centerX - (width / 2))
>                y = int(centerY - (height / 2))
>                boxes.append([x, y, int(width), int(height)])
>                confidences.append(float(confidence))
>                classIDs.append(classID)
>    #应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
>    idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
>    # 应用检测结果
>    np.random.seed(42)
>    COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
>    if len(idxs) > 0:
>        for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
>            (x, y) = (boxes[i][0], boxes[i][1])
>            (w, h) = (boxes[i][2], boxes[i][3])
>            color = [int(c) for c in COLORS[classIDs[i]]]
>            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
>            text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
>            cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
>            
>            if classIDs[i]==67:
>                #img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
>                if h>0.7*H:
>                    pos=mc.player.getPos()
>                    yaw=mc.player.getDirection()
>                    mc.player.setPos(pos.x+yaw.x*1.5,pos.y+yaw.y*1.5,pos.z+yaw.z*1.5)
>                    #ser.write('Fa'.encode())
>                elif(w<0.3*H):
>                    pos=mc.player.getPos()
>                    yaw=mc.player.getDirection()
>                    mc.player.setPos(pos.x-yaw.x*1.5,pos.y-yaw.y*1.5,pos.z-yaw.z*1.5)
>                    #ser.write('Ba'.encode())
>                elif x<(W-w)*0.2:
>                    pos=mc.player.getPos()
>                    yaw=mc.player.getDirection()
>                    length=sqrt(yaw.x*yaw.x+yaw.z*yaw.z)
>                    yaw2=[-yaw.z/length,0,yaw.x/length]
>                    mc.player.setPos(pos.x-yaw2[0]*1.5,pos.y+yaw2[1]*1.5,pos.z-yaw2[2]*1.5)
>                    #ser.write('La'.encode())
>                elif x>W-w-(W-w)*0.2:
>                    qpos=mc.player.getPos()
>                    yaw=mc.player.getDirection()
>                    length=sqrt(yaw.x*yaw.x+yaw.z*yaw.z)
>                    yaw2=[yaw.z/length,0,-yaw.x/length]
>                    mc.player.setPos(pos.x-yaw2[0]*1.5,pos.y+yaw2[1]*1.5,pos.z-yaw2[2]*1.5)
>                    #ser.write('Ra'.encode())
>
>    end = time.time()
>    print("YOLO1 took {:.6f} seconds".format(end - start))
>    cv2.imshow('target detect result1', img)
>    if(cv2.waitKey(100)&0xff==ord('q')):
>        break
>    time.sleep(2)
>#
>##以下是给插了Intel 的神经计算棒加速棒使用的速度比对代码，没有插的话请从此行以后全部删除
>#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
>#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
>#outInfo = net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
>#layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
>#boxes = [] # 所有边界框（各层结果放一起）
>#confidences = [] # 所有置信度
>#classIDs = [] # 所有分类ID
>#for out in layerOutputs:  # 各个输出层
>#    for detection in out:  # 各个框框
>#        # 拿到置信度
>#        scores = detection[5:]  # 各个类别的置信度
>#        classID = np.argmax(scores)  # 最高置信度的id即为分类id
>#        confidence = scores[classID]  # 拿到置信度
>#        # 根据置信度筛查
>#        if confidence > CONFIDENCE:
>#            box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
>#            (centerX, centerY, width, height) = box.astype("int")
>#            x = int(centerX - (width / 2))
>#            y = int(centerY - (height / 2))
>#            boxes.append([x, y, int(width), int(height)])
>#            confidences.append(float(confidence))
>#            classIDs.append(classID)
>##应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
>#idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
>## 应用检测结果
>#np.random.seed(42)
>#COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
>#if len(idxs) > 0:
>#    for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
>#        (x, y) = (boxes[i][0], boxes[i][1])
>#        (w, h) = (boxes[i][2], boxes[i][3])
>#        color = [int(c) for c in COLORS[classIDs[i]]]
>#        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
>#        text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
>#        cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
>#end = time.time()
>#print("YOLO2 took {:.6f} seconds".format(end - start))
>#cv2.imshow('target detect result2', img)
>#cv2.waitKey()
>#
>#
>#
>#
>```
>![20211103](/wuya/20211110-1.png)
>    
></details>

    
### 20211117

><details>
><summary>展开</summary>
>    
>```python
>from mcpi.minecraft import Minecraft
>import time
>
>mc=Minecraft.create()
>pos=mc.player.getTilePos()
>
>fill=1
>
>class House:
>    def __init__(self,x,y,z):
>        self.building=[
>        (1,(0,0,0),(x-1,y-z,z-1),0),#Remove All Blocks
>        (1,(0,0,0),(x-1,0,z-1),5),#Floor
>        (1,(0,1,0),(0,y-2,z-1),4),#Wall 1
>        (1,(0,1,0),(x-1,y-2,0),4),#Wall 2
>        (1,(0,1,9),(x-1,y-2,z-1),4),#Wall 3
>        (1,(9,1,0),(x-1,y-2,z-1),4),#Wall 4
>        (1,(0,y-1,0),(x-1,y-1,z-1),20)]#Roof
>        if y<4:
>            return
>        if x%2:#Door
>            self.building+=[(1,(int((x-1)/2),2,0),(int((x-1)/2),2,0),0)]
>            self.building+=[(1,(int((x-1)/2),1,0),(int((x-1)/2),1,0),0)]
>        else:
>            self.building+=[(1,(int(x/2-1),2,0),(int(x/2),2,0),0)]
>            self.building+=[(1,(int(x/2-1),1,0),(int(x/2),1,0),0)]
>
>        if y<5:#Window
>            if z%2:
>                self.building+=[(1,(x-1,1,int((z-3)/2)),(x-1,2,int((z+1)/2)),20)]
>            else:
>                self.building+=[(1,(x-1,1,int((z-2)/2)),(x-1,2,int(z/2)),20)]
>        else:
>            if z%2:
>                self.building+=[(1,(x-1,2,int((z-3)/2)),(x-1,3,int((z+1)/2)),20)]
>            else:
>                self.building+=[(1,(x-1,2,int((z-2)/2)),(x-1,3,int(z/2)),20)]
>        return
>    
>    def build(self,_mc,base):
>        for command in self.building:
>            if command[0]==1:
>                b=command[3]
>                x=range(command[1][0],command[2][0]+1)
>                y=range(command[1][1],command[2][1]+1)
>                z=range(command[1][2],command[2][2]+1)
>                print(b,x,y,z)
>                for _x in x:
>                    for _y in y:
>                        for _z in z:
>                            _mc.setBlock(base[0]+_x,base[1]+_y,base[2]+_z,b)
>
>
>while(1):
>    pos=mc.player.getTilePos()
>    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
>
>    hits=mc.events.pollBlockHits() 
>    for hit in hits:
>        base=(hit.pos.x+5,hit.pos.y+5,hit.pos.z+5)
>        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
>        mx=hit.pos.x
>        my=hit.pos.y
>        mz=hit.pos.z
>
>        house1=House(10,10,6)
>        house2=House(14,5,12)
>        house3=House(18,10,30)
>
>        house1.build(mc,(mx,my,mz))
>        house2.build(mc,(mx+20,my,mz))
>        house3.build(mc,(mx+40,my,mz))
>        break
>
>    time.sleep(0.5)
>```
>![20211117](/wuya/20211117.png)
>    
></details>
