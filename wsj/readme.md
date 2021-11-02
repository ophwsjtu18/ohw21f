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
![sdsd](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/xiaoguotu.png)

## 任务二、
### 代码
```python
from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

print("请输入x0:")
x0=int(input())
print("请输入y0:")
y0=int(input())
print("请输入z0:")
z0=int(input())
print("请输入房屋长L:")
L=int(input())
print("请输入房屋宽W:")
W=int(input())
print("请输入房屋宽高:")
H=int(input())
def house(x0,y0,z0,L,W,H): 
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0,z0+z,41)
    for x in range(L):
        for y in range(H):
            mc.setBlock(x0+x,y0+y,z0,21)
            mc.setBlock(x0+x,y0+y,z0+W-1,21)
    for z in range(W):
        for y in range(H):
            mc.setBlock(x0,y0+y,z0+z,21)
            mc.setBlock(x0+L-1,y0+y,z0+z,21)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0+H,z0+z,20)
    
            
house(x0,y0,z0,L,W,H)
```
### 效果图
![sdsdsd](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/2.png)
![dsfdf](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/3.png)

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
            mc.setBlock(x0+x,y0+y,z0+W-1,21)
    for z in range(W):
        for y in range(H):
            mc.setBlock(x0,y0+y,z0+z,21)
            mc.setBlock(x0+L-1,y0+y,z0+z,21)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0+H,z0+z,20)
    
            
house(pos.x,pos.y,pos.z,10,10,10)
house(pos.x+20,pos.y,pos.z,7,8,13)
house(pos.x+45,pos.y,pos.z,9,9,17)

```
### 效果图
![sdsdsd](https://github.com/ophwsjtu18/ohw21f/blob/main/wsj/4.png)
