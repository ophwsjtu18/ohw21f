# YOLO算法识别手机，根据手机位置控制我的世界人物前后左右跑动。三张截图为展示效果
## 申荣强
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 00:00:33 2021

@author: 申荣强
"""
print("shenrongqiang")
import cv2 as cv
import numpy as np
import serial
import os
import time
from mcpi.minecraft import Minecraft

def forc6():
    mc=Minecraft.create()
    pos=mc.player.getTilePos()
    
    #ser = serial.Serial("COM21")
    
    yolo_dir = 'D:/dingding/yolov3/yolov3'  # YOLO文件路径一定不能有中文在路径里面
    weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
    configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
    labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
    cap = cv.VideoCapture(0)
    CONFIDENCE = 0.5  # 过滤弱检测的最小概率
    THRESHOLD = 0.4  # 非最大值抑制阈值
    
    with open(labelsPath, 'rt') as f:
        labels = f.read().rstrip('\n').split('\n')
    # 加载网络、配置权重
    net = cv.dnn.readNetFromDarknet(configPath, weightsPath)  ## 利用下载的文件
    
    while(True):
        pos=mc.player.getTilePos()
        
        ret, img = cap.read()
        # 加载图片、转为blob格式、送入网络输入层 获取网络输出层信息（所有输出层的名字），设定并前向传播
        start = time.time()
        (H, W) = img.shape[:2]
        blobImg = cv.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
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
        idxs = cv.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
        # 应用检测结果
        np.random.seed(42)
        COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
        if len(idxs) > 0:
            for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
                (x, y) = (boxes[i][0], boxes[i][1])
                (w, h) = (boxes[i][2], boxes[i][3])
                color = [int(c) for c in COLORS[classIDs[i]]]
                cv.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
                text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
                if text[0] == 'c':
                    print(x,y)
                    if x > 280:
                        #ser.write("ON".encode())
                        mc.player.setTilePos(pos.x + 1, pos.y, pos.z)
                    if x < 140:
                        #ser.write("OFF".encode())
                        mc.player.setTilePos(pos.x - 1, pos.y, pos.z)
                    if y > 210:
                        #ser.write("ON_".encode())
                        mc.player.setTilePos(pos.x, pos.y, pos.z + 1)
                    if y < 70:
                        #ser.write("OFF_".encode())
                        mc.player.setTilePos(pos.x, pos.y, pos.z - 1)
                cv.putText(img, text, (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
        end = time.time()
        print("YOLO1 took {:.6f} seconds".format(end - start))
        cv.imshow('target detect result1', img)
        if(cv.waitKey(500)&0xff==27):
            cap.release()
            break
    cv.destroyAllWindows()



if __name__=="__main__":
    forc6()

cv.waitKey(0)
cv.destroyAllWindows()
```
![](https://s3.bmp.ovh/imgs/2021/11/85a18d14cce450d1.png)
![](https://s3.bmp.ovh/imgs/2021/11/4a3326f7c0970845.png)
![](https://s3.bmp.ovh/imgs/2021/11/b9979f3cdc9d684c.png)
