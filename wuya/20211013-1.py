import cv2
img=cv2.imread("xixihaha.jpg",cv2.IMREAD_UNCHANGED)
a=[10,70,130]
for i in a:
    for j in a:
        cv2.rectangle(img,(i,j),(i+50,j+50),(0,255,0),3)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
