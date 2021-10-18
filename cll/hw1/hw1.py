# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:42:05 2021

Assignment 1 for BE002

@author: LilyChang
"""

import cv2
import numpy as np


#%%
img=cv2.imread("input_pic.png")
# Too big, resize it
height,width=img.shape[:2]
img=cv2.resize(img,np.uint((width/3,height/3)),interpolation=cv2.INTER_CUBIC)

# Draw 3*3 rectangles, with thickness=3, size 50*50,
rec_sz=50
thickness=3
color=[0,255,0]
pos_range=np.arange(0,3*rec_sz,rec_sz)
for x1 in pos_range:
    for y1 in pos_range:
        leftUp=[x1,y1]
        rightDown=[x1+rec_sz,y1+rec_sz]
        cv2.rectangle(img,leftUp,rightDown,color=color,thickness=thickness)

cv2.imwrite('result.png',img)

cv2.imshow("Bear",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
