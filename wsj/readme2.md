#作业
import cv2
import numpy as np
#要求：拖动鼠标来绘制一个矩形或圆形，用'k'键来切换。
img=cv2.imread('picture.jfif',1)#导入图像
drawing=False #当鼠标按下时变为Tue
mode=True #如果mode为True表示绘制矩形，按下k键绘制圆形
ix,iy=-1,-1
#创建回调函数
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y #记录起始位置
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(100,255,0),-1)
            else:
                r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                cv2.circle (img,(ix,iy),r,(0,75,255),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    a=cv2.waitKey(1)&0xFF
    if a==ord('k'):
        mode=not mode
    elif a==27:
        break
cv2.destroyAllWindows()
#效果展示
[视频连接](https://link.clashofclans.com/cn?action=OpenLayout&id=TH7%3AHV%3AAAAARwAAAAFf_j_0ii2W5yWoagwY2wn3&platform=tencent)
