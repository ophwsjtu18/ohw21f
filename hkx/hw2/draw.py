import cv2
import numpy as np
import pretty_errors


def draw_hollow_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(cow, (x, y), 5, (0, 0, 255), 3)


def draw_solid_circle(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDBLCLK:
        cv2.circle(img2, (x, y), 5, (0, 0, 255), -1)


def draw_1():
    cow_1 = cv2.imread('img/cow.jpeg', 1)
    cv2.namedWindow('cow_1')
    cv2.setMouseCallback('cow_1', draw_hollow_circle)
    print("Press ENTER to continue...")
    while(1):
        cv2.imshow('cow_1', cow_1)
        if cv2.waitKey(20) & 0xFF == 13:
            print("Saving image to path 'img/cow_hollow_circle.jpeg'...")
            cv2.imwrite('img/cow_hollow_circle.jpeg', cow_1)
            break
    cv2.destroyAllWindows()


def draw_2():
    cow_2 = cv2.imread('img/cow.jpeg', 1)
    cv2.namedWindow('cow_2')
    cv2.setMouseCallback('cow_2', draw_solid_circle)
    print("Press ENTER to end...")
    while(1):
        cv2.imshow("cow_2", cow_2)
        if cv2.waitKey(20) & 0xFF == 13:
            print("Saving image to path 'img/cow_solid_circle.jpeg'...")
            cv2.imwrite('img/cow_solid_circle.jpeg', cow_2)
            break
    cv2.destroyAllWindows()


def main():
    draw_1()
    draw_2()


if __name__ == "__main__":
    main()
