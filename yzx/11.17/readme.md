**Task**

**Code**

```python
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()

class house():
    def __init__(self,data):
        self.data=data
    def buildhouse(self):
     #定义初始位置
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]   
     #定义长宽高
        len=self.data[3]    
        wid=self.data[4]    
        hig=self.data[5]    
     #建造地板
        for x in range(len):
            for z in range(wid):
                mc.setBlock(x0+x,y0,z0+z,44)
     #建造墙
        for y in range(hig):
            for a in range(len):
                mc.setBlock(x0+a,y0+y,z0,41)
                mc.setBlock(x0+a,y0+y,z0+wid-1,41)
            for a in range(wid-2):
                mc.setBlock(x0,y0+y,z0+1+a,41)
                mc.setBlock(x0+L-1,y0+y,z0+1+a,41)
     #建造天花板
        for x in range(len):
            for z in range(wid):
                mc.setBlock(x0+x,y0+hig,z0+z,20)
     #建造门
        mc.setBlock(x0+L/2,y0+1,z0,0)
        mc.setBlock(x0+L/2,y0+2,z0,0)
        mc.setBlock(x0+L/2-1,y0+1,z0,0)
        mc.setBlock(x0+L/2-1,y0+2,z0,0)
     #建造窗户
        for z in range(2):
            for y in range(2):
                mc.setBlock(x0+L-1,y0+y+2,z0+z+wid/2-1,20)

pos1=house([pos.x,pos.y,pos.z,7,8,10])
pos2=house([pos.x+20,pos.y,pos.z,8,13,6])
pos3=house([pos.x+40,pos.y,pos.z,9,9,17])
pos1.buildhouse()
pos2.buildhouse()
pos3.buildhouse()
```

**Picture**

![three-house](https://github.com/ophwsjtu18/ohw21f/blob/f91cb8a7cc3a658833725cddcfe3fc87e7ea2fee/yzx/11.17/three-house.png)

**Note**

This code contains all the requirements for the three tasks of this assignment.
        

        

