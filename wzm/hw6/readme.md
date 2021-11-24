## assignment 2021/11/17
### 创建class类在我的世界里构建房子
```python
import numpy as np
from mcpi.minecraft import Minecraft
class House(object):
    def __init__(self,x,y,z):
        self.x0 = x
        self.y0 = y
        self.z0 = z
        
    def buildhouse(self,l,w,h):
        self.l = l #默认的房子参数
        self.w = w
        self.h = h
        for i in range(self.l):
            for j in range(self.w):
                mc.setBlock(self.x0+i,self.y0,self.z0+j,17) #创造橡木地板
                mc.setBlock(self.x0+i,self.y0+self.h+1,self.z0+j,20)#创造玻璃天花板
            #建造四周围墙
        for y in range(self.h):
            for a in range(self.l):
                mc.setBlock(self.x0+a,self.y0+1+y,self.z0,98)
                mc.setBlock(self.x0+a,self.y0+1+y,self.z0+self.w-1,98)
            for a in range(self.w-2):
                mc.setBlock(self.x0,self.y0+1+y,self.z0+1+a,98)
                mc.setBlock(self.x0+self.l-1,self.y0+1+y,self.z0+1+a,98)
        #建造空气门
        mc.setBlock(self.x0+int(self.l/2), self.y0+1, self.z0,0)
        mc.setBlock(self.x0+int(self.l/2), self.y0+2, self.z0,0)

        #创造窗户2*2
        for z in range(2):
            for y in range(2): 
                mc.setBlock(self.x0, self.y0+y+int(self.h/2)-1, self.z0+z+int(self.w/2)-1, 20)
mc=Minecraft.create()
pos=mc.player.getTilePos()
#确定house位置
house1=House(pos.x+10,pos.y,pos.z)
house2=House(pos.x+25,pos.y,pos.z)
house3=House(pos.x+40,pos.y,pos.z)
#定义房子的长宽高然后建造
house1.buildhouse(10,10,6)
house2.buildhouse(8,8,5)
house3.buildhouse(4,5,10)

```

### 效果图
![](houseclass.png)
