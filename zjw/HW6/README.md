```python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getTilePos()

class House(object):
    def __init__(self, x0, y0, z0, L, W, H):
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.L = L
        self.W = W
        self.H = H
    
    def buildHouse(self):
        for y in range(self.H):
            for a in range(self.L):
                mc.setBlock(self.x0+a, self.y0+y, self.z0, 1)
                mc.setBlock(self.x0+a, self.y0+y, self.z0+self.L-1, 1)
            for a in range(self.W-2):
                mc.setBlock(self.x0,self.y0+y,self.z0+1+a, 1)
                mc.setBlock(self.x0+self.L-1, self.y0+y, self.z0+1+a, 1)

        # build floor
        for x in range(self.L):
           for z in range(self.W):
            mc.setBlock(self.x0+x, self.y0, self.z0+z, 5)

        # build ceiling
        for x in range(self.L-2):
            for z in range(self.W-2):
               mc.setBlock(self.x0+x+1, self.y0 + self.H-1, self.z0+z+1, 20)

        # build door(air)
        mc.setBlock(self.x0 + self.L/2, self.y0 + 1, self.z0, 0)
        mc.setBlock(self.x0 + self.L/2, self.y0 + 2, self.z0, 0)

        # build windows 
        for z in range(2):
           for y in range(2): 
                mc.setBlock(self.x0 + self.L-1, self.y0+y+2, self.z0+z+4, 0)
                mc.setBlock(self.x0 + self.L-1, self.y0+y+2, self.z0+z+4, 20)
x0 = pos.x
y0 = pos.y
z0 = pos.z
house1 = House(x0, y0, z0, 10, 10, 6)

for a in [1, 2, 3]:
    house = House(x0 + a*11, y0, z0, 10 - a, 10 - a, 8 - a)
    house.buildHouse()
```
![HW6_.png](https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW6_1.png)
