import cv2

cow = cv2.imread("cow.jpeg", 1)

point = []

for x in range(3):
    for y in range(3):
        point.append(([x, y],[x+50, y+50]))

color = (0, 255, 0)
thickness = 3

for item in point:
    cow = cv2.rectangle(cow, item[0], item[1], color, thickness)

cv2.imshow('cow',cow)

cv2.waitKey(0)
cv2.destroyAllWindows()
