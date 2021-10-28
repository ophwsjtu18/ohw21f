# 第三次作业
## 申荣强
```python
from mcpi.minecraft import Minecraft
import time
import serial
import numpy as np


mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)
def forc1():
    mc.setBlock(pos.x,pos.y,pos.z,5)
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [1, 2, 3, 4, 5, 6]
    for num in list1:
        for numy in list1:
            mc.setBlock(pos.x + num,pos.y,pos.z+numy,5)
            if num == 1 or num == 9 or numy == 1 or numy == 9:
                for numpz in list2:
                    mc.setBlock(pos.x + num,pos.y+numpz,pos.z+numy,4)
                    numpz += 1
            numy += 1
        num +=1
    for num in list1:
        for numy in list1:
            mc.setBlock(pos.x + num,pos.y+7,pos.z+numy,20)
            numy += 1
        num +=1

#在人物位置处造一个房子
def forc2():
    #mc.setBlock(pos.x,pos.y,pos.z,5)
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [1, 2, 3, 4, 5, 6]
    for num in list1:
        for numy in list1:
            #放置地板
            mc.setBlock(pos.x + num,pos.y,pos.z+numy,5)
            #放置墙面
            if num == 1 or num == 9 or numy == 1 or numy == 9:
                for numpz in list2:
                    mc.setBlock(pos.x + num,pos.y+numpz,pos.z+numy,4)
                    numpz += 1
            #放置门
            if (num == 4 or num == 5) and numy == 1:
                for numi in [1,2]:
                    mc.setBlock(pos.x + num,pos.y + numi,pos.z+numy,0)
                mc.setBlock(pos.x + num,pos.y + 1,pos.z+numy,64)
            #放置窗户
            if num == 1 and (numy == 4 or numy == 5):
                for numi in [2,3]:
                    mc.setBlock(pos.x + num,pos.y + numi,pos.z+numy,20)
            numy += 1
        num +=1
    
    #放置屋顶
    for num in list1:
        for numy in list1:
            mc.setBlock(pos.x + num,pos.y+7,pos.z+numy,20)
            numy += 1
        num +=1

#在(x,y,z)位置创造一个长宽高分别为l,w,h的房子
def forc3(x ,y, z, l, w, h):
    list1 = np.arange(1, l)
    list2 = np.arange(1, w)
    list3 = np.arange(1, h)
    for num in list1:
        for numy in list2:
            #放置地板
            mc.setBlock(x + num,y,z+numy,5)
            #放置墙面
            if num == 1 or num == 9 or numy == 1 or numy == 9:
                for numpz in list3:
                    mc.setBlock(x + num,y+numpz,z+numy,4)
                    numpz += 1
            #放置门
            if (num == l//2 - 1 or num == l//2) and numy == 1:
                for numi in [1,2]:
                    mc.setBlock(x + num,y + numi,z+numy,0)
                mc.setBlock(x + num,y + 1,z+numy,64)
            #放置窗户
            if num == 1 and (numy == w//2 - 1 or numy == w//2):
                for numi in np.arange(h//2 - 2, h//2):
                    mc.setBlock(x + num,y + numi,z+numy,20)
            numy += 1
        num +=1
    
    #放置屋顶
    for num in list1:
        for numy in list1:
            mc.setBlock(x + num,y + h,z+numy,20)
            numy += 1
        num +=1
    
#创建3个房屋
forc3(pos.x, pos.y, pos.z, 10, 10, 10)
forc3(pos.x + 20, pos.y, pos.z, 16, 16, 10)
forc3(pos.x + 50, pos.y, pos.z, 10, 10, 10)

stayed_time=0
while True:
    #print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    #mc.postToChat("please go to home x=58 y=6 z=-103 for 15s to fly")
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    if pos.x==58 and pos.z==-103 and pos.y==6:
        mc.postToChat("welcome home,count down"+str(30-stayed_time))
        stayed_time=stayed_time+1
        if stayed_time==1:
            ser = serial.Serial("COM7")
            ser.write("ON".encode())
        if stayed_time>=10:
            ser.write("OFF".encode())
            ser.close()
            mc.player.setTilePos(58,26,-103)
            stayed_time=0
    else:
        stayed_time=0
        
```
![20211028202223.png](https://i.loli.net/2021/10/28/6dWBv3tkwVquZXz.png)
