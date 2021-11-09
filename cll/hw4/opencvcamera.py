import cv2
import numpy

cv2.namedWindow("original")
cv2.namedWindow("flipped")
cap = cv2.VideoCapture(0) #调整参数实现读取视频或调用摄像头
while 1:
    ret, frame = cap.read()
    frame2=cv2.flip(frame,1)
    cv2.imshow("original", frame)
    cv2.imshow("flipped",frame2)
    if cv2.waitKey(100) & 0xff == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()