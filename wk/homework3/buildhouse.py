from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

def buildHouse():
     for i in range(6):
         for j in range(10):
             mc.setBlock(pos.x + j, pos.y + i, pos.z, 5)
             mc.setBlock(pos.x + j, pos.y + i, pos.z+9, 5)
             mc.setBlock(pos.x, pos.y + i, pos.z + j, 5)
             mc.setBlock(pos.x + 9, pos.y + i, pos.z + j, 5)
             for k in range(10):
                mc.setBlock(pos.x + j, pos.y + 6, pos.z + k, 20)
             for k in range(10):
                mc.setBlock(pos.x + j, pos.y, pos.z + k, 5)
             mc.setBlock(pos.x + 5, pos.y + 1, pos.z, 0)
             mc.setBlock(pos.x + 5, pos.y + 2, pos.z, 0)
     for i in range(2):
         for j in range(2):
             mc.setBlock(pos.x, pos.y + j + 2, pos.z + i + 4, 20)

buildHouse()
stayed_time=0
while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please go to home x=58 y=6 z=-103 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))
    if pos.x==58 and pos.z==-103 and pos.y==6:
        mc.postToChat("welcome home,count down"+str(30-stayed_time))
        stayed_time=stayed_time+1
        if stayed_time>=30:
            mc.player.setTilePos(58,26,-103)
            stayed_time=0
    else:
        stayed_time=0
