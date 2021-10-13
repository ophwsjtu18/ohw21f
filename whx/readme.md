import numpy

import cv2

img=cv2.imread('uu.webp',1)

ptLeftTop = (10, 10)

ptRightBottom = (70, 70)

point_color = (0, 255, 0) # BGR

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

ptLeftTop2 = (80, 10)

ptRightBottom2 = (140, 70)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop2, ptRightBottom2, point_color, thickness, lineType)

ptLeftTop3 = (150, 10)

ptRightBottom3 = (210, 70)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop3, ptRightBottom3, point_color, thickness, lineType)

ptLeftTop4 = (10, 80)

ptRightBottom4 = (70, 140)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop4, ptRightBottom4, point_color, thickness, lineType)

ptLeftTop5 = (80, 80)

ptRightBottom5 = (140, 140)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop5, ptRightBottom5, point_color, thickness, lineType)

ptLeftTop6 = (150, 80)

ptRightBottom6 = (210, 140)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop6, ptRightBottom6, point_color, thickness, lineType)

ptLeftTop7 = (10, 150)

ptRightBottom7 = (70, 210)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop7, ptRightBottom7, point_color, thickness, lineType)

ptLeftTop8 = (80, 150)

ptRightBottom8 = (140, 210)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop8, ptRightBottom8, point_color, thickness, lineType)

ptLeftTop9 = (150, 150)

ptRightBottom9 = (210, 210)

thickness = 3 

lineType = 4

cv2.rectangle(img, ptLeftTop9, ptRightBottom9, point_color, thickness, lineType)

cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()

![](https://github.com/ophwsjtu18/ohw21f/blob/main/whx/ew1.PNG)
