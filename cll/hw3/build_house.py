# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:38:45 2021
Assignment 3 for BE002
@author: LilyChang
"""
# %%
import mcpi.minecraft as minecraft
import mcpi.block as block

# %%
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+" y="+str(pos.y)+" z="+str(pos.z))

# %%
class house():
    def __init__(self,pos,W,L,H):
        self.pos=pos
        self.W=W
        self.H=H
        self.L=L
    def roof(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for x in range(self.L+1):
            for z in range(self.W+1):
                    mc.setBlock(x0+x, y0+self.H, z+z0, block.GLASS.id)

    def buildGround(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for x in range(self.L):
            for z  in range(self.W):
                mc.setBlock(x0+x, y0, z0+z, block.WOOD_PLANKS.id,0)  

    def buildWall(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for y in range(self.H):
            for a in range(self.L+1):
                mc.setBlock(x0+a, y0+y, z0, block.BRICK_BLOCK.id)
                mc.setBlock(x0+a, y0+y, z0+self.W, block.BRICK_BLOCK.id)
            for a in range(self.W):
                mc.setBlock(x0, y0+y, z0+1+a, block.BRICK_BLOCK.id)
                mc.setBlock(x0+self.L, y0+y, z0+1+a, block.BRICK_BLOCK.id)

    def buildDoor(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        mc.setBlock(x0+4, y0+1, z0,block.AIR.id)
        mc.setBlock(x0+4, y0+2, z0,block.AIR.id)
        #Add Light

    
    def buidWindow(self):
        x0=self.pos[0]
        y0=self.pos[1]
        z0=self.pos[2]
        for x in range(2):
            for y in range(2): 
                mc.setBlock(x0+6+x, y0+y+2, z0, 20)
    

    def buildAll(self):
        self.buildGround()
        self.buildWall()
        self.roof()
        self.buildDoor()
        self.buidWindow()
        

#%% Assignment 1
house1=house([pos.x,pos.y,pos.z],10,10,6)
house1.buildAll()

#%% Assignment 2
house2=house([pos.x+15,pos.y,pos.z],19,10,10)
house2.buildAll()
house3=house([pos.x-33,pos.y,pos.z],23,20,7)
house3.buildAll()

# %%
