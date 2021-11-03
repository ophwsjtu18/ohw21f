# Assignments 10/27
*Adiricast*
## HOMEWORK 2
### 1
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/10271.png)

Code 
```python
from mcpi.minecraft import Minecraft
import time


mc=Minecraft.create()
pos=mc.player.getTilePos()

for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,126)
        mc.setBlock(pos.x+x,pos.y+6,pos.z+z,126)

for x in range(12):
    for y in range(7):
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z-1,46)
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z+10,46)
        mc.setBlock(pos.x-1,pos.y+y,pos.z+x-1,46)
        mc.setBlock(pos.x+10,pos.y+y,pos.z+x-1,46)
for z in range(2):
    for y in range(2):
        mc.setBlock(pos.x-1,pos.y+y+2,pos.z+z+4,20)
mc.setBlock(pos.x+5,pos.y+1,pos.z-1,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z-1,0)


```

### 2
## 实现效果图
![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/10272.PNG)

Code 
```python
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
def house(x0,y0,z0,L,W,H):
    mc.player.setTilePos(x0+1,y0+1,z0+1)
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x,y0,z0+z,126)
            mc.setBlock(x0+x,y0+H,z0+z,20)

    for x in range(L+2):
        for y in range(H+1):
            mc.setBlock(x0+x-1,y0+y,z0-1,46)
            mc.setBlock(x0+x-1,y0+y,z0+W,46)
    for z in range(W+2):
        for y in range(H+1):
            mc.setBlock(x0-1,y0+y,z0+z-1,46)
            mc.setBlock(x0+L,y0+y,z0+z-1,46)
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0-1,y0+y+int((H-1)/2),z0+z+int((W-1)/2),20)
    mc.setBlock(x0+int((L-1)/2),y0+1,z0-1,0)
    mc.setBlock(x0+int((L-1)/2),y0+2,z0-1,0)


house(1,60,40,10,10,10)
house(30,60,40,10,10,7)
house(50,60,40,6,7,8)

```


