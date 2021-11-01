# HW 3 for BE002
Run ```build_house.py```


``` python
class house():
    def __init__(self,pos,W,L,H):
        self.pos=pos
        self.W=W
        self.H=H
        self.L=L
    def roof(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for x in range(self.L+1):
            for z in range(self.W+1):
                    mc.setBlock(x0+x, y0+self.H, z+z0, block.GLASS.id)

    def buildGround(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for x in range(self.L):
            for z  in range(self.W):
                mc.setBlock(x0+x, y0, z0+z, block.WOOD_PLANKS.id,0)  

    def buildWall(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for y in range(self.H):
            for a in range(self.L+1):
                mc.setBlock(x0+a, y0+y, z0, block.BRICK_BLOCK.id)
                mc.setBlock(x0+a, y0+y, z0+self.W, block.BRICK_BLOCK.id)
            for a in range(self.W):
                mc.setBlock(x0, y0+y, z0+1+a, block.BRICK_BLOCK.id)
                mc.setBlock(x0+self.L, y0+y, z0+1+a, block.BRICK_BLOCK.id)

    def buildDoor(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        mc.setBlock(x0+4, y0+1, z0,block.AIR.id)
        mc.setBlock(x0+4, y0+2, z0,block.AIR.id)
  
    def buidWindow(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for x in range(2):
            for y in range(2): 
                mc.setBlock(x0+6+x, y0+y+2, z0, 20)
    
    def buildAll(self):
        self.buildGround()
        self.buildWall()
        self.roof()
        self.buildDoor()
        self.buidWindow()
```
## Output
### Q1
<img src="https://github.com/ophwsjtu18/ohw21f/blob/main/cll/hw3/minecraft%E6%88%BF%E5%AD%901.png"  width= "50%" alt="Input" align=center />

### Q2
<img src="https://github.com/ophwsjtu18/ohw21f/blob/main/cll/hw3/minecraft%E6%88%BF%E5%AD%902.2.png"  width= "50%"  alt="Q2" align=center />

<img src="https://github.com/ophwsjtu18/ohw21f/blob/main/cll/hw3/%E6%88%BF%E5%AD%902.png"  width= "50%"  alt="Q2" align=center />

