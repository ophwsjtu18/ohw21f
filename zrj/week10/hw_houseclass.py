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
                mc.setBlock(self.x+self.l,self.y+j,self.z+i-1,49)
        for i in range(self.l):
            for j in range(self.w):
                mc.setBlock(self.x+i,self.y+self.h-1,self.z+j,20)
        for i in range(2):
            for j in range(2):
                mc.setBlock(self.x-1,self.y+self.h/2-i,self.z+self.w/2-j,20)
        for i in range(2):
            mc.setBlock(self.x+self.l/2,self.y+i+1,self.z-1,0)

x=pos.x
y=pos.y
z=pos.z
MChouse0=House(x,y,z,5,6,7)
MChouse0.createhouse()
MChouse1=House(x+10,y+10,z+10,4,6,8)
MChouse1.createhouse()
MChouse2=House(x+20,y+20,z+20,3,4,5)
MChouse2.createhouse()
