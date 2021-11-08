# 11.4作业
## 要求：摄像头同时显示原图像和镜像图像，按s键保存摄像头当前两张画面，按q键退出
### 代码
```python
import cv2
import numpy as np
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
flag=cap.isOpened()
index=1
while(flag):
    ret,frame=cap.read()
    cv2.imshow("Capture_Paizhao",frame)
    h_frame=cv2.flip(frame,1)
    cv2.imshow("Capture_Paizhao2",h_frame)
    k=cv2.waitKey(1)&0xFF
    if k==ord('s'):    #按下s键，进入下面的保存图片操作
        cv2.imwrite(str(index)+".jpg",frame)
        cv2.imwrite("fan"+str(index)+".jpg",frame)
        print("save tupian successfully!")
        index+=1
    elif k==ord('q'):  #按下q键，程序退出
        break
cap.release()
cv2.destroyAllWindows()
```
### 效果图
