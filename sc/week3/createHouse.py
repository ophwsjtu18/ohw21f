from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

mc.setBlock(pos.x,pos.y,pos.z,1)


def house(x,y,z,l,w,h):

    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y,z+j,5)

    for i in range(l+2):
        for j in range(h):
            mc.setBlock(x+i-1,y+j,z-1,1)
            mc.setBlock(x+i-1,y+j,z+w,1)

    for i in range(w+2):
        for j in range(h):
            mc.setBlock(x-1,y+j,z+i-1,1)
            mc.setBlock(x+l,y+j,z+i-1,1)

    for i in range(l):
        for j in range(w):
            mc.setBlock(x+i,y+h-1,z+j,20)

    for i in range(2):
        mc.setBlock(x+l/2,y+i+1,z-1,0)

    for i in range(2):
        for j in range(2):
            mc.setBlock(x-1,y+h/2-i,z+w/2-j,20)

house(pos.x,pos.y,pos.z,10,10,6)
house(pos.x+15,pos.y,pos.z,8,8,4)
house(pos.x+30,pos.y,pos.z,13,15,9)

stayed_time=0
