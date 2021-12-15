# 11.3作业
## 代码
```python
import cv2
import numpy as np

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
flag=cap.isOpened()
goal=1

while(flag):
    ret,image=cap.read()
    cv2.imshow("picture1",image)
    h_image=cv2.flip(image,1)
    cv2.imshow("picture2",h_image)
    k=cv2.waitKey(1)&0xFF
    
    if k==ord('s'):  
        cv2.imwrite(str(goal)+".jpg",image)
        cv2.imwrite("fan"+str(goal)+".jpg",h_image)
        print("save!")
        goal+=1
    elif k==27: 
        break
        
cap.release()
cv2.destroyAllWindows()
```
## 效果图
![yuan](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/11.3/1.jpg)
![fan](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/11.3/fan1.jpg)
