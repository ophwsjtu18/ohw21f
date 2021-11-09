import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        check, frame = cap.read()
        if check:
            frame = cv2.flip(frame, 1)
            cv2.imshow('frame', frame)
        if cv2.waitKey(20) & 0xFF == 13:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
