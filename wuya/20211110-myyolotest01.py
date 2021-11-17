from math import sqrt
import numpy as np
import cv2
import os
import time
from mcpi.minecraft import Minecraft
import serial

yolo_dir = 'E:/python/yolov3/yolov3'  # YOLO文件路径一定不能有中文在路径里面
weightsPath = os.path.join(yolo_dir, 'yolov3.weights')  # 权重文件
configPath = os.path.join(yolo_dir, 'yolov3.cfg')  # 配置文件
labelsPath = os.path.join(yolo_dir, 'coco.names')  # label名称
imgPath = os.path.join(yolo_dir, 'person.jpg')  # 测试图像
CONFIDENCE = 0.5  # 过滤弱检测的最小概率
THRESHOLD = 0.4  # 非最大值抑制阈值

with open(labelsPath, 'rt') as f:
    labels = f.read().rstrip('\n').split('\n')
# 加载网络、配置权重
net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)  ## 利用下载的文件

cap=cv2.VideoCapture(0)
mc=Minecraft.create()
#ser=serial.Serial('COM5')

while True:
    # 加载图片、转为blob格式、送入网络输入层 获取网络输出层信息（所有输出层的名字），设定并前向传播
    start = time.time()
    #img = cv2.imread(imgPath)
    ret,frame=cap.read()
    img=cv2.flip(frame,1)
    (H, W) = img.shape[:2]
    blobImg = cv2.dnn.blobFromImage(img, 1.0/255.0, (416, 416), None, True, False)  ## net需要的输入是blob格式的，用blobFromImage这个函数来转格式
    net.setInput(blobImg)  ## 调用setInput函数将图片送入输入层
    #net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
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
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            color = [int(c) for c in COLORS[classIDs[i]]]
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
            text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
            cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
            
            if classIDs[i]==67:
                #img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                if h>0.7*H:
                    pos=mc.player.getPos()
                    yaw=mc.player.getDirection()
                    mc.player.setPos(pos.x+yaw.x*1.5,pos.y+yaw.y*1.5,pos.z+yaw.z*1.5)
                    #ser.write('Fa'.encode())
                elif(w<0.3*H):
                    pos=mc.player.getPos()
                    yaw=mc.player.getDirection()
                    mc.player.setPos(pos.x-yaw.x*1.5,pos.y-yaw.y*1.5,pos.z-yaw.z*1.5)
                    #ser.write('Ba'.encode())
                elif x<(W-w)*0.2:
                    pos=mc.player.getPos()
                    yaw=mc.player.getDirection()
                    length=sqrt(yaw.x*yaw.x+yaw.z*yaw.z)
                    yaw2=[-yaw.z/length,0,yaw.x/length]
                    mc.player.setPos(pos.x-yaw2[0]*1.5,pos.y+yaw2[1]*1.5,pos.z-yaw2[2]*1.5)
                    #ser.write('La'.encode())
                elif x>W-w-(W-w)*0.2:
                    qpos=mc.player.getPos()
                    yaw=mc.player.getDirection()
                    length=sqrt(yaw.x*yaw.x+yaw.z*yaw.z)
                    yaw2=[yaw.z/length,0,-yaw.x/length]
                    mc.player.setPos(pos.x-yaw2[0]*1.5,pos.y+yaw2[1]*1.5,pos.z-yaw2[2]*1.5)
                    #ser.write('Ra'.encode())

    end = time.time()
    print("YOLO1 took {:.6f} seconds".format(end - start))
    cv2.imshow('target detect result1', img)
    if(cv2.waitKey(100)&0xff==ord('q')):
        break
    time.sleep(2)
#
##以下是给插了Intel 的神经计算棒加速棒使用的速度比对代码，没有插的话请从此行以后全部删除
#net.setPreferableBackend(cv2.dnn.DNN_BACKEND_INFERENCE_ENGINE)
#net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
#outInfo = net.getUnconnectedOutLayersNames()  ## 前面的yolov3架构也讲了，yolo在每个scale都有输出，outInfo是每个scale的名字信息，供net.forward使用
#layerOutputs = net.forward(outInfo)  # 得到各个输出层的、各个检测框等信息，是二维结构。
#boxes = [] # 所有边界框（各层结果放一起）
#confidences = [] # 所有置信度
#classIDs = [] # 所有分类ID
#for out in layerOutputs:  # 各个输出层
#    for detection in out:  # 各个框框
#        # 拿到置信度
#        scores = detection[5:]  # 各个类别的置信度
#        classID = np.argmax(scores)  # 最高置信度的id即为分类id
#        confidence = scores[classID]  # 拿到置信度
#        # 根据置信度筛查
#        if confidence > CONFIDENCE:
#            box = detection[0:4] * np.array([W, H, W, H])  # 将边界框放会图片尺寸
#            (centerX, centerY, width, height) = box.astype("int")
#            x = int(centerX - (width / 2))
#            y = int(centerY - (height / 2))
#            boxes.append([x, y, int(width), int(height)])
#            confidences.append(float(confidence))
#            classIDs.append(classID)
##应用非最大值抑制(non-maxima suppression，nms)进一步筛掉
#idxs = cv2.dnn.NMSBoxes(boxes, confidences, CONFIDENCE, THRESHOLD) # boxes中，保留的box的索引index存入idxs
## 应用检测结果
#np.random.seed(42)
#COLORS = np.random.randint(0, 255, size=(len(labels), 3), dtype="uint8")  # 框框显示颜色，每一类有不同的颜色，每种颜色都是由RGB三个值组成的，所以size为(len(labels), 3)
#if len(idxs) > 0:
#    for i in idxs.flatten(): # indxs是二维的，第0维是输出层，所以这里把它展平成1维
#        (x, y) = (boxes[i][0], boxes[i][1])
#        (w, h) = (boxes[i][2], boxes[i][3])
#        color = [int(c) for c in COLORS[classIDs[i]]]
#        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)  # 线条粗细为2px
#        text = "{}: {:.4f}".format(labels[classIDs[i]], confidences[i])
#        cv2.putText(img, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)  # cv.FONT_HERSHEY_SIMPLEX字体风格、0.5字体大小、粗细2px
#end = time.time()
#print("YOLO2 took {:.6f} seconds".format(end - start))
#cv2.imshow('target detect result2', img)
#cv2.waitKey()
#
#
#
#