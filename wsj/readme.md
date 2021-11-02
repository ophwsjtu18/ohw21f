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

