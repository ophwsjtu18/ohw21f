from mcpi.minecraft import Minecraft
import mcpi.block as block


class House():
    x, y, z, w, l, h = 0, 0, 0, 0, 0, 0

    def __init__(self, _x, _y, _z, _w, _l, _h):
        self.x = _x
        self.y = _y
        self.z = _z
        self.w = _w
        self.h = _h
        self.l = _l

    def create_roof(self):
        for dx in range(self.l+1):
            for dz in range(self.w+1):
                mc.setBlock(self.x+dx, self.y+self.h,
                            self.z+dz, block.GLASS.id)

    def create_ground(self):
        for dx in range(self.l):
            for dz in range(self.w):
                mc.setBlock(self.x+dx, self.y, self.z +
                            dz, block.WOOD_PLANKS.id, 0)

    def create_wall(self):
        for dy in range(self.h):
            for da in range(self.l+1):
                mc.setBlock(self.x+da, self.y+dy, self.z, block.BRICK_BLOCK.id)
                mc.setBlock(self.x+da, self.y+dy, self.z +
                            self.w, block.BRICK_BLOCK.id)
            for da in range(self.w):
                mc.setBlock(self.x, self.y+dy, self.z +
                            da+1, block.BRICK_BLOCK.id)
                mc.setBlock(self.x+self.l, self.y+dy,
                            self.z+da+1, block.BRICK_BLOCK.id)

    def create_door(self):
        mc.setBlock(self.x+4, self.y+1, self.z, block.AIR.id)
        mc.setBlock(self.x+4, self.y+2, self.z, block.AIR.id)

    def create_window(self):
        for dx in range(2):
            for dy in range(2):
                mc.setBlock(self.x+dx+6, self.y+dy+2, self.z, 20)

    def build(self):
        self.create_ground()
        self.create_wall()
        self.create_roof()
        self.create_door()
        self.create_window()


def main():
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    mc.postToChat(f"Current postion: ({pos.x}, {pos.y}, {pos.z})")
    house_1 = House(pos.x, pos.y, pos.z, 10, 10, 6)
    house_1.build()
    house_2 = House(pos.x+50, pos.y, pos.z, 40, 30, 20)
    house_2.build()
    house_3 = House(pos.x-50, pos.y, pos.z, 20, 15, 10)
    house_3.build()


if __name__ == "__main__":
    main()
