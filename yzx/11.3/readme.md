**Code**

```python
import cv2
import numpy as np

cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
flag=cap.isOpened()
goal=1

while(flag):
    ret,image=cap.read()
    cv2.imshow("Capture_Paizhao",image)
    h_image=cv2.flip(image,1)
    cv2.imshow("Capture_Paizhao2",h_image)
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

**Notes**

1.Press the s key to save the picture to the desktop

2.Press ESC to exit the program

**Picture**
