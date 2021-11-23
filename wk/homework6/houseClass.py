from mcpi.minecraft import Minecraft
import random
import time

mc = Minecraft.create()
pos = mc.player.getTilePos()

class house():
    def __init__(self,pos,width_,length_,height_):
        self.pos = pos
        self.W = width_
        self.L = length_
        self.H = height_

    def buildWall(self):
        x0 = self.pos[0]
        y0 = self.pos[1]
        z0 = self.pos[2]
        listWall = [4, 5, 24, 98]
        wall = random.sample(listWall, 1)
        for y in range(self.H):
            for x in range(self.L):
                mc.setBlock(x0 + x, y0 + y, z0, wall[0])
                mc.setBlock(x0 + x, y0 + y, z0 + self.W - 1, wall[0])
            for z in range(self.W):
                mc.setBlock(x0, y0 + y, z0 + z, 5)
                mc.setBlock(x0 + self.L - 1, y0 + y, z0 + z, wall[0])

    def buildFloor(self):
        x0 = self.pos[0]
        y0 = self.pos[1]
        z0 = self.pos[2]
        listFloor = [4,5,24]
        floor = random.sample(listFloor,1)
        for x in range(self.L):
            for z in range(self.W):
                mc.setBlock(x0 + x, y0, z0 + z, floor[0])

    def buildRoof(self):
        x0 = self.pos[0]
        y0 = self.pos[1]
        z0 = self.pos[2]
        for x in range(self.L):
            for z in range(self.W):
                mc.setBlock(x0 + x, y0 + self.H, z0 + z, 20)

    def buildDoor(self):
        x0 = self.pos[0]
        y0 = self.pos[1]
        z0 = self.pos[2]
        if self.L % 2 == 0:
            mc.setBlock(x0 + self.L / 2, y0 + 1, z0, 0)
            mc.setBlock(x0 + self.L / 2, y0 + 2, z0, 0)
            mc.setBlock(x0 - 1 + self.L / 2, y0 + 1, z0, 0)
            mc.setBlock(x0 - 1 + self.L / 2, y0 + 2, z0, 0)
        else:
            mc.setBlock(x0 + (self.L - 1) / 2, y0 + 1, z0, 0)
            mc.setBlock(x0 + (self.L - 1) / 2, y0 + 2, z0, 0)

    def buildWindow(self):
        x0 = self.pos[0]
        y0 = self.pos[1]
        z0 = self.pos[2]
        if self.W % 2 == 0:
            for i in range(3):
                for j in range(3):
                    mc.setBlock(x0, y0 + j + 2, z0 + i + self.L / 2, 20)
        else:
            for i in range(3):
                for j in range(3):
                    mc.setBlock(x0, y0 + j + 2, z0 + i + (self.L - 1) / 2, 20)

    def build(self):
        self.buildWall()
        self.buildFloor()
        self.buildRoof()
        self.buildWindow()
        self.buildDoor()

def main():

    houses = ["house1", "house2", "house3"]
    for i in range(3):
        l = random.randint(15, 25)
        w = random.randint(15, 30)
        h = random.randint(7, 12)
        houses[i] = house([pos.x + 35*i, pos.y, pos.z], l, w, h)
        houses[i].build()

if __name__ == "__main__":
    main()