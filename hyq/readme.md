###2021.10.15 HOMEWORK###

import cv2
import numpy as np
img = cv2.imread("C:/Users/skywang/Desktop/1.jpeg")
for i in range(0,3):
    for j in range(0,3):
        cv2.rectangle(img,(50*i,50*j),(50*i+50,50*j+50),(0,255,0),3)
cv2.imshow("Image",img)
# emptyImage = np.zeros(img.shape, np.uint8)
# cv2.imshow("EmptyImage",emptyImage)
# empty2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",empty2)
cv2.waitKey (0)
cv2.destroyAllWindows()
