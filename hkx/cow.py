import cv2

cow = cv2.imread("cow.jpeg", 1)

x = [i*50 for i in range(3)]
y = [i*50 for i in range(3)]

point = []

for a in x:
    for b in y:
        point.append(([a, b],[a+50,b+50]))

color = (0, 255, 0)
thickness = 3

for item in point:
    cow = cv2.rectangle(cow, item[0], item[1], color, thickness)


cv2.imshow('cow',cow)

cv2.waitKey(0)
