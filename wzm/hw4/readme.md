# assignment 2021/11/3
## code
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)#索引摄像头

 # 定义编解码器并创建VideoWriter对象
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('test.avi',fourcc, 40.0, (640,480))#保存录像

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        #0表示绕x轴翻转，正值(例如1)表示绕y轴翻转。负值(例如-1)表示围绕两个轴翻转。

# write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# 释放所有窗口
cap.release()
out.release()
cv2.destroyAllWindows()
```

## result
## video snapshot
![](test.png)
