```python
from mcpi.minecraft import Minecraft

mc = Minecraft.create()
pos = mc.player.getTilePos()

def house(x0, y0, z0, L, W, H):
    for y in range(H):
        for a in range(L):
            mc.setBlock(x0+a, y0+y, z0, 1)
            mc.setBlock(x0+a, y0+y, z0+L-1, 1)
        for a in range(W-2):
            mc.setBlock(x0, y0+y, z0+1+a, 1)
            mc.setBlock(x0+L-1, y0+y, z0+1+a, 1)

    # build floor
    for x in range(L):
        for z in range(W):
            mc.setBlock(x0+x, y0, z0+z, 5)

    # build ceiling
    for x in range(L-2):
        for z in range(W-2):
            mc.setBlock(x0+x+1, y0+H-1, z0+z+1, 20)

    # build door(air)
    mc.setBlock(x0 + L/2, y0 + 1, z0, 0)
    mc.setBlock(x0 + L/2, y0 + 2, z0, 0)

    # build windows 
    for z in range(2):
        for y in range(2): 
                mc.setBlock(x0+L-1, y0+y+2, z0+z+4, 0)
                mc.setBlock(x0+L-1, y0+y+2, z0+z+4, 20)

x0 = pos.x
y0 = pos.y
z0 = pos.z
house(x0, y0, z0, 10, 10, 6)

for a in [1, 2, 3]:
    house(x0 + a*11, y0, z0, 10 - a, 10 - a, 8 - a)
```
!(HW3_1)[https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW3_1.png]
!(HW3_2)[https://github.com/ophwsjtu18/ohw21f/blob/main/zjw/zjw.assets/HW3_2.png]
