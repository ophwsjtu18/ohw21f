from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()

fill=1

class House:
    def __init__(self,x,y,z):
        self.building=[
        (1,(0,0,0),(x-1,y-z,z-1),0),#Remove All Blocks
        (1,(0,0,0),(x-1,0,z-1),5),#Floor
        (1,(0,1,0),(0,y-2,z-1),4),#Wall 1
        (1,(0,1,0),(x-1,y-2,0),4),#Wall 2
        (1,(0,1,9),(x-1,y-2,z-1),4),#Wall 3
        (1,(9,1,0),(x-1,y-2,z-1),4),#Wall 4
        (1,(0,y-1,0),(x-1,y-1,z-1),20)]#Roof
        if y<4:
            return
        if x%2:#Door
            self.building+=[(1,(int((x-1)/2),2,0),(int((x-1)/2),2,0),0)]
            self.building+=[(1,(int((x-1)/2),1,0),(int((x-1)/2),1,0),0)]
        else:
            self.building+=[(1,(int(x/2-1),2,0),(int(x/2),2,0),0)]
            self.building+=[(1,(int(x/2-1),1,0),(int(x/2),1,0),0)]

        if y<5:#Window
            if z%2:
                self.building+=[(1,(x-1,1,int((z-3)/2)),(x-1,2,int((z+1)/2)),20)]
            else:
                self.building+=[(1,(x-1,1,int((z-2)/2)),(x-1,2,int(z/2)),20)]
        else:
            if z%2:
                self.building+=[(1,(x-1,2,int((z-3)/2)),(x-1,3,int((z+1)/2)),20)]
            else:
                self.building+=[(1,(x-1,2,int((z-2)/2)),(x-1,3,int(z/2)),20)]
        return
    
    def build(self,_mc,base):
        for command in self.building:
            if command[0]==1:
                b=command[3]
                x=range(command[1][0],command[2][0]+1)
                y=range(command[1][1],command[2][1]+1)
                z=range(command[1][2],command[2][2]+1)
                print(b,x,y,z)
                for _x in x:
                    for _y in y:
                        for _z in z:
                            _mc.setBlock(base[0]+_x,base[1]+_y,base[2]+_z,b)


while(1):
    pos=mc.player.getTilePos()
    #mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z))

    hits=mc.events.pollBlockHits() 
    for hit in hits:
        base=(hit.pos.x+5,hit.pos.y+5,hit.pos.z+5)
        mc.postToChat("Hit:"+"x"+str(hit.pos.x)+"y"+str(hit.pos.y)+"z"+str(hit.pos.z))
        mx=hit.pos.x
        my=hit.pos.y
        mz=hit.pos.z

        house1=House(10,10,6)
        house2=House(14,5,12)
        house3=House(18,10,30)

        house1.build(mc,(mx,my,mz))
        house2.build(mc,(mx+20,my,mz))
        house3.build(mc,(mx+40,my,mz))
        break

    time.sleep(0.5)
