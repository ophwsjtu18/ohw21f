from mcpi.minecraft import Minecraft
import mcpi.block as block
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()

class House(object):
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        
    def createhouse(self):
        for i in range(self.l):
            for j in range(self.w):
                mc.setBlock(self.x+i,self.y,self.z+j,5)
        for i in range(self.l+2):
            for j in range(self.h):
                mc.setBlock(self.x+i-1,self.y+j,self.z-1,49)
                mc.setBlock(self.x+i-1,self.y+j,self.z+self.w,49)
        for i in range(self.w+2):
            for j in range(self.h):
                mc.setBlock(self.x-1,self.y+j,self.z+i-1,49)
                mc.setBlock(self.x+l,self.y+j,self.z+i-1,49)
        for i in range(self.l):
            for j in range(self.w):
                mc.setBlock(self.x+i,self.y+self.h-1,self.z+j,20)
        for i in range(2):
            for j in range(2):
                mc.setBlock(self.x-1,self.y+self.h/2-i,self.z+self.w/2-j,20)
        for i in range(2):
            mc.setBlock(self.x+l/2,self.y+i+1,self.z-1,0)

x=pos.x
y=pos.y
z=pos.z
l=[10,12,15]
w=[12,15,15]
h=[6,9,9]
for i in range(2):
    MChouse=house(x,y,z,l[i],w[i],h[i])
    MChouse.createhouse()
