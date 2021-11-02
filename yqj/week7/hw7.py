# 由于作业的最后一个要求在功能上兼容前两个，
# 因此最后只展示了造一排三个房子

from mcpi.minecraft import Minecraft
import mcpi.block as block

def house(x0,y0,z0,l,w,h,m=17):
# m:material, default=17--log
    
    if min(l,w,h)<=0:
        print("min(l,w,h)<=0 !!!")
        return -1
    
    #造地板
    for x in range(l):
        for z in range(w):
            mc.setBlock(x0+x, y0, z0+z, m)

    #造围墙
    for y in range(h):
        for x in range(l):
            mc.setBlock(x0+x, y0+y, z0, m)
            mc.setBlock(x0+x, y0+y, z0+w-1, m)
        for z in range(w):
            mc.setBlock(x0, y0+y, z0+z, m)
            mc.setBlock(x0+l-1, y0+y, z0+z, m)

    #造天花板
    for x in range(l-2):
        for z in range(w-2):
            mc.setBlock(x0+x+1, y0+h-1, z0+z+1, 20) # glass

    #造门
    mc.setBlock(x0+l//2, y0+1, z0,0) # air
    mc.setBlock(x0+l//2, y0+2, z0,0)

    #造窗户
    for z in range(2):
        for y in range(2): 
                mc.setBlock(x0, y0+h//2+y-1, z0+w//2+z-1, 20) #glass


mc=Minecraft.create()
pos=mc.player.getTilePos()

x0 = pos.x
y0 = pos.y
z0 = pos.z


house(x0,y0,z0,10,10,6)
house(x0+20,y0,z0,15,15,9)
house(x0+20+25,y0,z0,20,20,12)