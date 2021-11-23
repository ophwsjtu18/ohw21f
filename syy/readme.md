# Assignments 11/17
*Adiricast*
## HOMEWORK 5

CODE

``` 
from mcpi.minecraft import Minecraft

class House():
    def __init__(self,x0,y0,z0,l,w,h,m=46):
    #m=buiding material       
        if (min(l,w,h)<=0):
            raise AssertionError("min(l,w,h)<=0 !!!")
        self.x0 = x0
        self.y0 = y0
        self.z0 = z0
        self.l = l
        self.w = w
        self.h = h
        self.m = m
   
        #Ground
        for x in range(self.l):
            for z in range(self.w):
                mc.setBlock(self.x0+x, self.y0, self.z0+z, self.m)

        #Wall
        for y in range(self.h):
            for x in range(self.l):
                mc.setBlock(self.x0+x, self.y0+y, self.z0, self.m)
                mc.setBlock(self.x0+x, self.y0+y, self.z0+self.w-1, self.m)
            for z in range(self.w):
                mc.setBlock(self.x0, self.y0+y, self.z0+z, self.m)
                mc.setBlock(self.x0+self.l-1, self.y0+y, self.z0+z, self.m)

        #Ceil
        for x in range(self.l-2):
            for z in range(self.w-2):
                mc.setBlock(self.x0+x+1, self.y0+self.h-1, self.z0+z+1, 20) # glass

        #Door
        mc.setBlock(self.x0+self.l//2, self.y0+1, self.z0,0) # air
        mc.setBlock(self.x0+self.l//2, self.y0+2, self.z0,0)

        #Window
        for z in range(2):
            for y in range(2): 
                    mc.setBlock(self.x0, self.y0+self.h//2+y-1, self.z0+self.w//2+z-1, 20) #glass


mc=Minecraft.create()
pos=mc.player.getTilePos()

x0 = pos.x
y0 = pos.y
z0 = pos.z


house1 = House(x0,y0,z0,5,5,5)
house2 = House(x0+20,y0,z0,15,15,15)
house3 = House(x0+20+25,y0,z0,27,27,27)
```

![me](https://github.com/ophwsjtu18/ohw21f/blob/main/syy/11171.png)
