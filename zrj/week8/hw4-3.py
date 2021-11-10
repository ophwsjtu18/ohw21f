import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("无法打开摄像头")
	exit()

if cap.isOpened():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    videoclip = cv2.VideoWriter('videoclip.avi',fourcc,20.0,(1920,1080))
    while(1):
        ret,frame = cap.read()
        if not ret:
            print("无法获取画面帧")
            break
        
        if ret==True:
             video_new = cv2.flip(frame,1)
             video_turnover =np.hstack((frame,video_new))
             videoclip.write(video_new) 
             cv2.imshow('video_turnover',video_turnover)
             
             if cv2.waitKey(1) == ord('q'):
                break

	
cap.release()
cv2.destroyAllWindows()
