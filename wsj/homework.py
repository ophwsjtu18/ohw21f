import numpy as np
import cv2
img=cv2.imread("niu.webp",1)
cv2.rectangle(img,(0,0),(50,50),(0,255,0),3)
cv2.rectangle(img,(50,0),(100,50),(0,255,0),3)
cv2.rectangle(img,(100,0),(150,50),(0,255,0),3)
cv2.rectangle(img,(0,50),(50,100),(0,255,0),3)
cv2.rectangle(img,(0,100),(50,150),(0,255,0),3)
cv2.rectangle(img,(50,50),(100,100),(0,255,0),3)
cv2.rectangle(img,(100,50),(150,100),(0,255,0),3)
cv2.rectangle(img,(50,100),(100,150),(0,255,0),3)
cv2.rectangle(img,(100,100),(150,150),(0,255,0),3)
cv2.imshow('homework',img)
cv2.waitKey(0)
cv2.destroyAllWindows()