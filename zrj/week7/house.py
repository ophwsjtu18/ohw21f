from mcpi.minecraft import Minecraft
import mcpi.block as block
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()

def house(x,y,z,l,w,h):
    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y,z+j,5)
    for i in range(l+2):
        for j in range(h):
            mc.setBlock(x+i-1,y+j,z-1,49)
            mc.setBlock(x+i-1,y+j,z+w,49)
    for i in range(w+2):
        for j in range(h):
            mc.setBlock(x-1,y+j,z+i-1,49)
            mc.setBlock(x+l,y+j,z+i-1,49)
    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y+h-1,z+j,20)
    for i in range(2):
        for j in range(2):
            mc.setBlock(x-1,y+h/2-i,z+w/2-j,20)
    for i in range(2):
        mc.setBlock(x+l/2,y+i+1,z-1,0)


house(pos.x,pos.y,pos.z,15,15,9)
house(pos.x+20,pos.y+20,pos.z,10,12,9)
house(pos.x+40,pos.y+40,pos.z,12,15,6)
