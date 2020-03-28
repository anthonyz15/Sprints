


class building:
    wallstr = []
    building_name=""
    wall_num=1

    def buildingname(self,name):
        temp ="Building:%s" %(name)
        self.building_name+=temp

    def wall(self,x1,y1,x2,y2,height,texture):
        temp= 'Wall:x1=%d, y1=%d, x2=%d, y2=%d, Height=%d, Texture: %s \n'% (self.wall_num,x1,y1,x2,y2,height,texture)
        self.wallstr.append(temp)
        self.wall_num+=1
        print(self.wall_num)
        print(*self.wallstr)

    def SaveBuilding(self):
        temp=""
        temp=self.building_name+ "\n" + temp.join(self.wallstr)
        return temp

    def DeleteBuilding(self):
        self.building_name=""
        self.wallstr=[]
        self.wall_num=1

