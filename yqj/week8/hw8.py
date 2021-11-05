import cv2
import os

os.chdir("E:\\学校\\硬件\\week8")

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M', 'P', '4', '2')
out = cv2.VideoWriter('yqj_video.avi',fourcc, 20.0, (640,480))

while(1):
# 参数ret 为True 或者False,代表有没有读取到图片
# 第二个参数frame表示截取到一帧的图片
    ret,frame = cap.read()
    
    if ret == True:
            
    # 每一帧绕y轴翻转
        mirror = cv2.flip(frame,1)
        
        cv2.imshow('my_video',mirror)
        out.write(mirror)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()