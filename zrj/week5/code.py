import numpy as np
import cv2

img=cv2.imread('Ox.jpg',cv2.IMREAD_UNCHANGED)
# load a pic with color

for i in range(0,150,50):
 for j in range(0,150,50):
  left=(i,j)
  right=(i+50,j+50)
  cv2.rectangle(img,left,right,(0,255,0),3,4)
cv2.imshow('Output_image',img)
cv2.waitKey(0)
cv2.destroyALLWindows()
