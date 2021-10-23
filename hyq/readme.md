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

