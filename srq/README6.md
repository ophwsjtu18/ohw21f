# 在python里创建一个类用于建造房屋，下面的例子分别建造了一个房子和三个房子
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 22:04:36 2021

@author: 申荣强
"""
from mcpi.minecraft import Minecraft
import time
import numpy as np

mc=Minecraft.create()
pos=mc.player.getTilePos()


class MCBuildingHouse:
    """建造房子"""
    
    def __init__(self, x, y, z):
        """初始化房子，参数为建造房子的起点"""
        self.x = x
        self.y = y
        self.z = z
    
    def update_point(self, x, y, z):
        """更新参数为建造房子的起点"""
        self.x = x
        self.y = y
        self.z = z
    
    
    def build_1_house(self):
        """在建造房子的起点处建造一个房子"""
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list2 = [1, 2, 3, 4, 5, 6]
        for num in list1:
            for numy in list1:
                #放置地板
                mc.setBlock(self.x + num,self.y,self.z+numy,5)
                #放置墙面
                if num == 1 or num == 9 or numy == 1 or numy == 9:
                    for numpz in list2:
                        mc.setBlock(self.x + num,self.y+numpz,self.z+numy,4)
                        numpz += 1
                #放置门
                if (num == 4 or num == 5) and numy == 1:
                    for numi in [1,2]:
                        mc.setBlock(self.x + num,self.y + numi,self.z+numy,0)
                    mc.setBlock(self.x + num,self.y + 1,self.z+numy,64)
                #放置窗户
                if num == 1 and (numy == 4 or numy == 5):
                    for numi in [2,3]:
                        mc.setBlock(self.x + num,self.y + numi,self.z+numy,20)
                numy += 1
            num +=1
        
        #放置屋顶
        for num in list1:
            for numy in list1:
                mc.setBlock(self.x + num,self.y+7,self.z+numy,20)
                numy += 1
            num +=1
    
    def build_3_house(self):
        """在建造房子的起点处建造三个房子"""
        self.build_1_house()
        self.update_point(self.x + 20, self.y, self.z)
        self.build_1_house()
        self.update_point(self.x + 20, self.y, self.z)
        self.build_1_house()
        self.update_point(self.x - 40, self.y, self.z)
        

print("player pos is",pos)
myMCHouse = MCBuildingHouse(pos.x, pos.y, pos.z)

#在起点处建造一个房子
myMCHouse.build_1_house()

#上移房子起点20个单位并建造三个房子
myMCHouse.update_point(pos.x, pos.y + 20, pos.z)
myMCHouse.build_3_house()

```
![](https://s3.bmp.ovh/imgs/2021/11/cc7b2f4d4471f32e.png)
