import numpy as np
import cv2
import os

os.chdir("E:\\学校\\硬件\\week6\\hw")

# 作业1：重复鼠标当画笔代码，鼠标右键双击画圆
def draw_circle1(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img1,(x,y),5,(0,0,255),3)

img1 = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image1')
cv2.setMouseCallback('image1',draw_circle1)

while(1):
    cv2.imshow('image1',img1)
    if cv2.waitKey(20)&0xFF == 27:
    # 通过按位取和，只取按键对应ACSII值的后8位，排除其他因素干扰，详见
    # https://blog.csdn.net/hao5119266/article/details/104173400
        break
cv2.destroyAllWindows()


# 作业2：在牛的图片上鼠标右键双击画实心圆
def draw_circle2(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img2,(x,y),5,(0,0,255),-1)

img2 = cv2.imread("bull.jpg")
cv2.namedWindow('image2')
cv2.setMouseCallback('image2',draw_circle2)

while(1):
    cv2.imshow("image2",img2)
    if cv2.waitKey(20)&0xFF == 27:
        break
cv2.imwrite('pic211020.png',img2)
cv2.destroyAllWindows()