import cv2

img = cv2.imread('cow.jpg',1)
color = (0,255,0)
strokeWeight = 3
size = 50
for i in range(3):
    for j in range(3):
        cv2.rectangle(img, (i*size,j*size), ((i+1)*size, (j+1)*size), color,strokeWeight)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('colorCow.jpg',img)
cv2.destroyAllWindows()