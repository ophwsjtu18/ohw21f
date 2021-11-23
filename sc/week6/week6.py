from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

class House(object):
    def __init__(self,L,W,H):
        self.l=L
        self.w=W
        self.h=H

    def creat(self,x,y,z):
        for i in range(self.l):
            for j in range(self.w):
                mc.setBlock(x+i,y,z+j,5)

        for i in range(self.l+2):
            for j in range(self.h):
                mc.setBlock(x+i-1,y+j,z-1,1)
                mc.setBlock(x+i-1,y+j,z+self.w,1)

        for i in range(self.w+2):
            for j in range(self.h):
                mc.setBlock(x-1,y+j,z+i-1,1)
                mc.setBlock(x+self.l,y+j,z+i-1,1)

        for i in range(self.l):
            for j in range(self.w):
                mc.setBlock(x+i,y+self.h-1,z+j,20)

        for i in range(2):
            mc.setBlock(x+self.l/2,y+i+1,z-1,0)

        for i in range(2):
            for j in range(2):
                mc.setBlock(x-1,y+self.h/2-i,z+self.w/2-j,20)


house1=House(10,10,6)
house2=House(8,7,4)
house3=House(13,15,9)
house1.creat(pos.x,pos.y,pos.z)
house2.creat(pos.x+15,pos.y,pos.z)
house3.creat(pos.x+30,pos.y,pos.z)

stayed_time=0
