## 2021.10.15 
### HOMEWORK

#### 导入图片
```python
import numpy as np
import cv2
img = cv2.imread('niutou.jpg',cv2.IMREAD_COLOR)
# cv2.IMREAD_COLOR：读入一副彩色图像。图像的透明度会被忽略，这是默认参数。
# cv2.IMREAD_GRAYSCALE：以灰度模式读入图像
# cv2.IMREAD_UNCHANGED：读入一幅图像，并且包括图像的 alpha 通道
```

#### 在左上角画9个矩形
```python
for i in range(0,3):
    for j in range(0,3):
        cv2.rectangle(img,(50*i,50*j),(50*i+50,50*j+50),(0,255,0),3)
```
#### 展示
```python
cv2.imshow("Image",img)
cv2.waitKey (0)
cv2.destroyAllWindows()
```
