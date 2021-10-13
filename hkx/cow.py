import cv2

cow = cv2.imread("cow.jpeg", 1)

x = [i*50 for i in range(3)]
y = [i*50 for i in range(3)]

point = []

for i in x:
    for j in y:
        point.append(([i, j], [i+50, j+50]))

color = (0, 255, 0)
thickness = 3

for item in point:
    cow = cv2.rectangle(cow, item[0], item[1], color, thickness)

cv2.imshow('cow',cow)

cv2.waitKey(0)
cv2.destroyAllWindows()
