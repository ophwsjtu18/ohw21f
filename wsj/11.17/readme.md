# 11.17作业
## 任务：创建3个House类的实例，通过参数，建造3个房子
### 代码
```python
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()

class house():
    def __init__(self,data):
        self.data=data
    def buildhouse(self):
        x0=self.data[0]
        y0=self.data[1]
        z0=self.data[2]   #定义初始位置
        L=self.data[3]    #定义长
        W=self.data[4]    #定义宽
        H=self.data[5]    #定义高
        #建造地板
        for x in range(L):
            for z in range(W):
                mc.setBlock(x0+x,y0,z0+z,44)
        #建造墙
        for y in range(H):
            for a in range(L):
                mc.setBlock(x0+a,y0+y,z0,57)
                mc.setBlock(x0+a,y0+y,z0+W-1,57)
            for a in range(W-2):
                mc.setBlock(x0,y0+y,z0+1+a,57)
                mc.setBlock(x0+L-1,y0+y,z0+1+a,57)
        #建造天花板
        for x in range(L):
            for z in range(W):
                mc.setBlock(x0+x,y0+H,z0+z,20)
        #建造门
        mc.setBlock(x0+L/2,y0+1,z0,0)
        mc.setBlock(x0+L/2,y0+2,z0,0)
        mc.setBlock(x0+L/2-1,y0+1,z0,0)
        mc.setBlock(x0+L/2-1,y0+2,z0,0)
        #建造窗户
        for z in range(2):
            for y in range(2):
                mc.setBlock(x0+L-1,y0+y+2,z0+z+W/2-1,20)

op1=house([pos.x,pos.y,pos.z,6,8,10])
op2=house([pos.x+20,pos.y,pos.z,7,13,6])
op3=house([pos.x+40,pos.y,pos.z,9,10,17])
op1.buildhouse()
op2.buildhouse()
op3.buildhouse()
```
### 效果图
