import numpy as np
import cv2

# 作业1：读取并显示彩色图片
img1 = cv2.imread("E:\\hardware course\\bull.jpg")
# 路径中存在中文会报错
cv2.imshow("image1",img1)
cv2.waitKey(0)

# 作业2：画布左上角画9个绿色矩形
img2 = np.zeros((512,512,3),np.uint8)

for row in range(0,3):
    for col in range(0,3):
        x1 = 2+row*60
        y1 = 2+col*60
        x2 = x1+50
        y2 = y1+50
        cv2.rectangle(img2,(x1,y1),(x2,y2),(0,255,0),3)

# 颜色通道顺序BGR，(x1,y1)和(x2,y2)分别是矩形的左上角和右上角，
# 画布的左上角是原点，横轴x纵轴y，详见：
# https://blog.csdn.net/sinat_41104353/article/details/85171185

cv2.imshow("image2",img2)
cv2.waitKey(0)
cv2.imwrite('pic211013.png',img2)
cv2.destroyAllWindows()
