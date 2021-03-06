import random

from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
# print("player pos is",pos)

def house(x0,y0,z0,L,W,H):
     for y in range(H):
         # for wall
         list1 = [4, 5, 24, 98]
         wall = random.sample(list1, 1)
         for x in range(L):
             mc.setBlock(x0 + x, y0 + y, z0, wall[0])
             mc.setBlock(x0 + x, y0 + y, z0 + W-1, wall[0])
         for z in range(W):
             mc.setBlock(x0, y0 + y, z0 + z, 5)
             mc.setBlock(x0 + L - 1, y0 + y, z0 + z, wall[0])
         # for roof and floor
         list2 = [5,4,24]
         floof = random.sample(list2,1)
         for x in range(L):
             for z in range(W):
                mc.setBlock(x0 + x, y0 + H, z0 + z, 20)
         for x in range(L):
             for z in range(W):
                 mc.setBlock(x0 + x, y0 , z0 + z, floof[0])
         # for door
         if L%2 == 0:
             mc.setBlock(x0 + L/2, y0 + 1, z0, 0)
             mc.setBlock(x0 + L/2, y0 + 2, z0, 0)
             mc.setBlock(x0 - 1 + L / 2, y0 + 1, z0, 0)
             mc.setBlock(x0 - 1 + L / 2, y0 + 2, z0, 0)
         else:
             mc.setBlock(x0 + (L - 1)/ 2, y0 + 1, z0, 0)
             mc.setBlock(x0 + (L - 1)/ 2, y0 + 2, z0, 0)
         # for window
         if W%2 == 0:
             for i in range(3):
                 for j in range(3):
                     mc.setBlock(x0, y0 + j + 2, z0 + i + L/2, 20)
         else:
             for i in range(3):
                 for j in range(3):
                     mc.setBlock(x0, y0 + j + 2, z0 + i + (L - 1)/2, 20)

for i in range(3):
    l = random.randint(15,25)
    w = random.randint(15,30)
    h = random.randint(7,12)
    house(pos.x + i*35, pos.y, pos.z,l,w,h)
