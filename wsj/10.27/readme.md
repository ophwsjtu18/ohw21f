# 10.27作业
## 任务一
### 代码
```python
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

for i in range(0,10):
   for j in range(0,10):
       mc.setBlock(pos.x+i,pos.y,pos.z+j,5)
for i in range(0,10):
   for j in range(1,5):
       mc.setBlock(pos.x+i,pos.y+j,pos.z,17)
       mc.setBlock(pos.x+i,pos.y+j,pos.z+9,17)
       mc.setBlock(pos.x,pos.y+j,pos.z+i,17)
       mc.setBlock(pos.x+9,pos.y+j,pos.z+i,17)
for i in range(10):
    for j in range(10):
        mc.setBlock(pos.x+i,pos.y+5,pos.z+j,20)
for i in range(4,6):
   for j in range(1,3):
       mc.setBlock(pos.x+i,pos.y+j,pos.z,0)
for i in range(4,6):
   for j in range(2,4):
       mc.setBlock(pos.x,pos.y+j,pos.z+i,20)
```
### 效果图
![sds](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/10.27/task1.jpg)
## 任务二
### 代码
```python
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

def house(x0,y0,z0,L,W,H):
   for x in range(L):
       for z in range(W):
           mc.setBlock(x0+x,y0,z0+z,41)
   for x in range(L):
       for y in range(H):
           mc.setBlock(x0+x,y0+y,z0,22)
           mc.setBlock(x0+x,y0+y,z0+W-1,22)
   for z in range(W):
       for y in range(H):
           mc.setBlock(x0,y0+y,z0+z,22)
           mc.setBlock(x0+L-1,y0+y,z0+z,22)
   for x in range(L):
       for z in range(W):
           mc.setBlock(x0+x,y0+H,z0+z,20)   
           
house(pos.x,pos.y,pos.z,11,20,18)
```
### 效果图
![sdsa](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/10.27/Task2.jpg)
## 任务三
### 代码
```python
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

def house(x0,y0,z0,L,W,H):
   for x in range(L):
       for z in range(W):
           mc.setBlock(x0+x,y0,z0+z,41)
   for x in range(L):
       for y in range(H):
           mc.setBlock(x0+x,y0+y,z0,21)
           mc.setBlock(x0+x,y0+y,z0+W-1,22)
   for z in range(W):
       for y in range(H):
           mc.setBlock(x0,y0+y,z0+z,21)
           mc.setBlock(x0+L-1,y0+y,z0+z,22)
   for x in range(L):
       for z in range(W):
           mc.setBlock(x0+x,y0+H,z0+z,20)    
            
house(pos.x,pos.y,pos.z,12,19,10)
house(pos.x+20,pos.y,pos.z,7,10,13)
house(pos.x+45,pos.y,pos.z,7,9,17)
```
### 效果图
![sdsds](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/10.27/Task3.jpg)
