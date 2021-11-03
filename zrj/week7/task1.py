from mcpi.minecraft import Minecraft
import time
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()

for x in range(10):
    for z in range(10):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,5)
        mc.setBlock(pos.x+x,pos.y+6,pos.z+z,20)

for x in range(12):
    for y in range(7):
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z-1,49)
        mc.setBlock(pos.x+x-1,pos.y+y,pos.z+10,49)
        mc.setBlock(pos.x-1,pos.y+y,pos.z+x-1,49)
        mc.setBlock(pos.x+10,pos.y+y,pos.z+x-1,49)
        
for z in range(2):
    for y in range(2):
        mc.setBlock(pos.x-1,pos.y+y+2,pos.z+z+4,20)
mc.setBlock(pos.x+5,pos.y+1,pos.z-1,0)
mc.setBlock(pos.x+5,pos.y+2,pos.z-1,0)
